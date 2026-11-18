"""Guard original Lecture 1 wording, equations, removals and source integrity."""
from pathlib import Path
from lxml import etree as ET
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://www.w3.org/2000/svg',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math'}
normalize = lambda text: re.sub(r'\s+', '', text)
source = ROOT / 'public/sources/powerpoint/Seminar.pptx'
native = json.loads((ROOT / 'sources/lecture1-native.json').read_text(encoding='utf-8'))
assert native['sha256'] == hashlib.sha256(source.read_bytes()).hexdigest(), 'Original source has changed'
assert [s['number'] for s in native['slides']] == list(range(1, 18)), 'Source order/removals changed'
tokens = 0
with zipfile.ZipFile(source) as deck:
    for page in native['slides']:
        original = ET.fromstring(deck.read(f'ppt/slides/slide{page["number"]}.xml'))
        for item in page['objects']:
            assert not (page['number'] == 3 and item['id'] in (1499, 1501)), 'Removed objective icon returned'
            node = original.xpath(f'//p:cNvPr[@id="{item["id"]}"]', namespaces=NS)[0].getparent().getparent()
            svg = ET.fromstring(('<svg xmlns="http://www.w3.org/2000/svg">' + item['svg'] + '</svg>').encode())
            visible = normalize(''.join(svg.xpath('//s:text[not(@fill-opacity="0")]/text()', namespaces=NS)))
            if item['omml']:
                expected = normalize(''.join(node.xpath('.//m:t/text()', namespaces=NS)))
                assert expected in visible, f'Equation changed: slide {page["number"]}, object {item["id"]}'
            for paragraph in node.xpath('.//a:p', namespaces=NS):
                parts = paragraph.xpath('.//a:t/text()', namespaces=NS)
                # Inline equations can separate two ordinary text runs.
                expected_parts = parts if item['omml'] else [''.join(parts)]
                for part in expected_parts:
                    assert normalize(part) in visible, f'Text changed: slide {page["number"]}, object {item["id"]}'
            tokens += len(svg.xpath('//*[@data-native-equation]'))
assert tokens == 180, 'Native equation lettering was replaced or omitted'
lecture = (ROOT / 'lectures/01-geometry.md').read_text(encoding='utf-8')
assert lecture.count('<LectureOneSource ') == 17
assert not any(word in lecture for word in ('<OriginalSlide', '<NativeObjectives', '<NativeMathDiagram', '<MathFilm'))
print('Lecture 1 source checks passed: 17 slides, original prose/equations, 180 native equation tokens, approved removals and intact PPTX.')
