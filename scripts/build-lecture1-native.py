"""Build only Lecture 1 from the original objects, without writing new slide copy.

Refresh the read-only object exports with export-lecture1-native.ps1 first.
SVG text stays text. Equations, connectors and graph shapes stay native SVG
vectors. Only the source deck's original bitmap artwork remains bitmap artwork.
There is no exported slide screenshot, animation layer image or final-frame swap.
"""
from pathlib import Path
import base64
import hashlib
import json
import posixpath
import re
import zipfile
from lxml import etree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'svg': 'http://www.w3.org/2000/svg',
}
XLINK = 'http://www.w3.org/1999/xlink'
ASSET_DIRECTORY = 'lecture1-assets'


def save_asset(data, extension):
    filename = hashlib.sha256(data).hexdigest()[:20] + '.' + extension
    path = ROOT / ('public/sources/' + ASSET_DIRECTORY) / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_bytes(data)
    return '/sources/' + ASSET_DIRECTORY + '/' + filename


def clean_svg(path, prefix, math_tokens=None):
    svg = ET.fromstring(path.read_bytes())
    # Shape.Export adds a crop translation around global slide coordinates.
    # Remove that export-only wrapper; all original object coordinates remain.
    children = [n for n in svg if ET.QName(n).localname not in ('defs', 'title', 'desc')]
    if len(children) == 1 and ET.QName(children[0]).localname == 'g':
        group = children[0]
        if re.fullmatch(r'translate\([-.\d]+[ ,]+[-.\d]+\)', group.get('transform', '')):
            group.attrib.pop('transform')
    identifiers = {n.get('id'): prefix + '-' + n.get('id') for n in svg.iter() if n.get('id')}
    for element in svg.iter():
        if element.get('id'):
            element.set('id', identifiers[element.get('id')])
        for key, value in list(element.attrib.items()):
            for previous, current in identifiers.items():
                value = value.replace('url(#' + previous + ')', 'url(#' + current + ')')
                if value == '#' + previous:
                    value = '#' + current
            if value.startswith('data:image/'):
                header, encoded = value.split(',', 1)
                extension = header.split('/')[1].split(';')[0].replace('jpeg', 'jpg')
                value = save_asset(base64.b64decode(encoded), extension)
                # Keep references relative to the configured Slidev base URL.
                element.set('data-source-asset', value)
            element.set(key, value)
    # Office exports some equation glyphs as outlines followed by hidden text.
    # Restore those glyphs to actual editable SVG text, in the original math
    # font, at the measured original positions. Brackets/arrows stay vectors.
    measured = {t['index']: t for t in math_tokens or []}
    for index, element in enumerate(svg.xpath('.//svg:text[@fill-opacity="0"]', namespaces=NS)):
        token = measured.get(index)
        if token and element.text not in ('Ԧ', 'ቮ'):
            previous = element.getprevious()
            if previous is None or ET.QName(previous).localname != 'path':
                raise ValueError(f'Unexpected equation glyph structure: {path}, token {index}')
            previous.getparent().remove(previous)
            element.attrib.clear()
            element.set('fill', token['fill'])
            element.set('font-family', 'Cambria Math')
            element.set('font-size', f'{token["size"]:.6f}')
            element.set('font-weight', str(token['weight']))
            element.set('transform', 'matrix(' + ' '.join(f'{n:.9f}' for n in token['matrix']) + ')')
            element.set('data-native-equation', 'true')
            element.text = token['text']
        elif element.text in ('Ԧ', 'ቮ'):
            # Office uses accessibility placeholders for vector accents and
            # augmented-matrix dividers. Their actual native vectors remain.
            element.getparent().remove(element)
    for text in list(svg.xpath('.//svg:text', namespaces=NS)):
        value = ''.join(text.itertext()).strip()
        if value.startswith(('http://', 'https://')):
            link = ET.Element('{' + NS['svg'] + '}a', href=value, target='_blank', rel='noopener noreferrer')
            parent = text.getparent()
            parent.replace(text, link)
            link.append(text)
    return ''.join(ET.tostring(n, encoding='unicode') for n in svg)


def background_for(source, part, visited=None):
    visited = set() if visited is None else visited
    if part in visited:
        return None
    visited.add(part)
    xml = ET.fromstring(source.read(part))
    relationships = posixpath.join(posixpath.dirname(part), '_rels', posixpath.basename(part) + '.rels')
    rels = ET.fromstring(source.read(relationships)) if relationships in source.namelist() else []
    targets = {n.get('Id'): posixpath.normpath(posixpath.join(posixpath.dirname(part), n.get('Target'))) for n in rels}
    blip = xml.find('p:cSld/p:bg/p:bgPr/a:blipFill/a:blip', NS)
    if blip is not None:
        target = targets[blip.get('{' + NS['r'] + '}embed')]
        return save_asset(source.read(target), Path(target).suffix[1:])
    for relation in rels:
        if relation.get('Type', '').endswith(('slideLayout', 'slideMaster')):
            if part.startswith('ppt/slideMasters/'):
                continue
            inherited = background_for(source, targets[relation.get('Id')], visited)
            if inherited:
                return inherited
    return None


def source_shape(slide, ident):
    found = slide.xpath(f'//p:cNvPr[@id="{ident}"]', namespaces=NS)
    return found[0].getparent().getparent() if found else None


def build(prepare_math=False):
    export_dir = ROOT / '.cache/lecture1-native'
    if not (export_dir / 'manifest.json').exists():
        raise SystemExit('Run scripts/export-lecture1-native.ps1 first (read-only PowerPoint export).')
    objects = json.loads((export_dir / 'manifest.json').read_text(encoding='utf-8-sig'))
    metric_path = ROOT / 'sources/lecture1-math-metrics.json'
    math_metrics = {(m['slide'], m['shape']): m['tokens'] for m in json.loads(metric_path.read_text(encoding='utf-8'))} if metric_path.exists() and not prepare_math else {}
    old = json.loads((ROOT / 'sources/powerpoint.json').read_text(encoding='utf-8-sig'))
    original = next(deck for deck in old if deck['id'] == 'Seminar')
    edits = json.loads((ROOT / 'sources/deck-edits.json').read_text(encoding='utf-8'))
    source_path = ROOT / 'public/sources/powerpoint/Seminar.pptx'
    native = {'source': 'Seminar.pptx', 'sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
              'width': 1280, 'height': 720, 'slides': []}
    lecture = []
    with zipfile.ZipFile(source_path) as source:
        for page in objects:
            number = page['number']
            if number in edits['excludedSourceSlides'].get('Seminar', []):
                continue
            xml = ET.fromstring(source.read(f'ppt/slides/slide{number}.xml'))
            background = background_for(source, f'ppt/slides/slide{number}.xml')
            previous = original['slides'][number - 1]
            entry = {'number': number, 'background': background, 'clicks': previous['clicks'],
                     'objects': [], 'effects': previous['effects']}
            if number in edits.get('staticScreenshotSlides', {}).get('Seminar', []):
                entry['clicks'] = 0
                entry['effects'] = []
            for item in page['objects']:
                if number == 3 and item['id'] in edits['hiddenObjectiveShapes']:
                    continue
                shape = source_shape(xml, item['id'])
                prose = shape.xpath('.//a:p[not(ancestor::mc:Fallback)]', namespaces={**NS, 'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006'}) if shape is not None else []
                paragraphs = [''.join(p.xpath('.//a:t/text()', namespaces=NS)) for p in prose]
                equations = [ET.tostring(n, encoding='unicode') for n in shape.xpath('.//m:oMath', namespaces=NS)] if shape is not None else []
                if number == 3 and item['id'] == 3:
                    # PowerPoint rasterizes its bevel on export. The original
                    # white divider is rebuilt here as a native SVG rectangle.
                    svg = '<rect x="18.6667" y="115.3333" width="9.3333" height="480" fill="#FFFFFF" />'
                else:
                    svg = clean_svg(export_dir / item['file'], f'l1-s{number}-o{item["id"]}', math_metrics.get((number, item['id'])))
                media = next((m for m in previous.get('media', []) if m['shape'] == item['id']), None)
                entry['objects'].append({
                    'id': item['id'], 'name': item['name'], 'bounds': item['bounds'],
                    'svg': svg, 'paragraphs': paragraphs, 'omml': equations,
                    **({'media': media} if media else {}),
                })
            # Requested objective fix: animate every surviving element, in pairs.
            # Only timing changes. Original text, style and coordinates stay intact.
            if number == 3:
                entry['effects'] = []
                groups = [(1486, 0), (3, .08), (1478, .18), (1476, .18),
                          (1481, .34), (6, .34), (1484, .50), (2, .50),
                          (4, .66), (5, .66), (1500, .82), (1519, .82)]
                for ident, delay in groups:
                    entry['effects'].append({'shape': ident, 'type': 2, 'step': 0,
                                             'direction': 2, 'duration': .55, 'delay': delay, 'exit': False})
            native['slides'].append(entry)
            fields = {'layout': 'none', 'lecture': 1, 'title': f'Lecture 1 · original slide {number}',
                      'clicks': entry['clicks'], 'sourceDeck': 'Seminar', 'sourceSlide': number}
            if not lecture:
                fields.update(routeAlias='lecture-1', section=True)
            lecture.append('---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fields.items())
                           + '\n---\n\n' + f'<LectureOneSource :slide="{number}" />\n'
                           + f'\n<!-- Original Seminar.pptx slide {number}. Native SVG objects; no rewritten slide copy. -->\n')
    (ROOT / 'sources/lecture1-native.json').write_text(json.dumps(native, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'lectures/01-geometry.md').write_text('\n'.join(lecture), encoding='utf-8')
    index_path = ROOT / 'sources/lecture-index.json'
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding='utf-8'))
        item = next(i for i in index if i['lecture'] == 1)
        item.update(originals=len(lecture), total=len(lecture), new_labs=0, rendering='source-native-svg')
        index_path.write_text(json.dumps(index, indent=2) + '\n', encoding='utf-8')
    print(f'Lecture 1: {len(lecture)} slides, {sum(len(p["objects"]) for p in native["slides"])} original native objects; no rewritten text.')
    return native


if __name__ == '__main__':
    import sys
    build(prepare_math='--prepare-math' in sys.argv)
