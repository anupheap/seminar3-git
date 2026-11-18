"""Retain embedded video, hyperlinks, original text and animation geometry."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json
import posixpath

ROOT = Path(__file__).resolve().parents[1]
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'p14': 'http://schemas.microsoft.com/office/powerpoint/2010/main'}


def main():
    path = ROOT / 'sources/powerpoint.json'
    decks = json.loads(path.read_text(encoding='utf-8-sig'))
    if isinstance(decks, dict):
        decks = [decks]
    for deck in decks:
        with ZipFile(ROOT / ('public' + deck['source'])) as archive:
            for slide in deck['slides']:
                number = slide['number']
                xml = ET.fromstring(archive.read(f'ppt/slides/slide{number}.xml'))
                relations = ET.fromstring(archive.read(f'ppt/slides/_rels/slide{number}.xml.rels'))
                rels = {r.get('Id'): r for r in relations}
                slide['text'] = ' '.join(t.text or '' for t in xml.findall('.//a:t', NS))
                slide['links'] = list(dict.fromkeys(r.get('Target') for r in relations
                    if r.get('Type', '').endswith('/hyperlink') and r.get('Target', '').startswith('https://')))
                slide['media'] = []
                for pic in xml.findall('.//p:pic', NS):
                    video = pic.find('.//p14:media', NS)
                    if video is None:
                        continue
                    rel = rels[video.get('{' + NS['r'] + '}embed')]
                    member = posixpath.normpath(posixpath.join('ppt/slides', rel.get('Target')))
                    target = ROOT / 'public/sources/media' / f'{deck["id"]}-{Path(member).name}'
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(archive.read(member))
                    transform = pic.find('p:spPr/a:xfrm', NS)
                    offset = transform.find('a:off', NS)
                    size = transform.find('a:ext', NS)
                    trim = video.find('p14:trim', NS)
                    shape_id = int(pic.find('p:nvPicPr/p:cNvPr', NS).get('id'))
                    crop = pic.find('p:blipFill/a:srcRect', NS)
                    slide['media'].append({
                        'shape': shape_id, 'src': '/sources/media/' + target.name,
                        'start': float(trim.get('st', 0)) / 1000 if trim is not None else 0,
                        'end': float(trim.get('end', 0)) / 1000 if trim is not None else 0,
                        'crop': {k: float(v) / 100000 for k, v in crop.attrib.items()} if crop is not None else {},
                        'left': int(offset.get('x')) / 12700 / deck['width'] * 100,
                        'top': int(offset.get('y')) / 12700 / deck['height'] * 100,
                        'width': int(size.get('cx')) / 12700 / deck['width'] * 100,
                        'height': int(size.get('cy')) / 12700 / deck['height'] * 100,
                    })
                # XML also supplies exact shape order and effect class/subtype.
                order = {}
                for i, shape in enumerate(xml.find('p:cSld/p:spTree', NS)):
                    for element in shape.iter():
                        if element.tag.endswith('}cNvPr'):
                            order[int(element.get('id'))] = i
                for layer in slide['layers']:
                    layer['order'] = order.get(layer['shape'], 0)
                    for shape in xml.find('p:cSld/p:spTree', NS):
                        ids = [el.get('id') for el in shape.iter() if el.tag.endswith('}cNvPr')]
                        if str(layer['shape']) not in ids:
                            continue
                        xfrm = shape.find('p:spPr/a:xfrm', NS)
                        if xfrm is None:
                            xfrm = shape.find('p:grpSpPr/a:xfrm', NS)
                        if xfrm is not None:
                            off, ext = xfrm.find('a:off', NS), xfrm.find('a:ext', NS)
                            if off is not None and ext is not None:
                                left = int(off.get('x')) / 12700 / deck['width'] * 100
                                top = int(off.get('y')) / 12700 / deck['height'] * 100
                                width = int(ext.get('cx')) / 12700 / deck['width'] * 100
                                height = int(ext.get('cy')) / 12700 / deck['height'] * 100
                                layer['bounds'] = [left, top, width, height]
                                layer['origin'] = [left + width / 2, top + height / 2]
                slide['layers'].sort(key=lambda layer: layer['order'])
    path.write_text(json.dumps(decks, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('Preserved original text, hyperlinks, shape order and embedded media.')


if __name__ == '__main__':
    main()
