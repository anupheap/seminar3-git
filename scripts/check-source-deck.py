"""Compare the native presentation's text and equations with original sources."""
from pathlib import Path
from lxml import etree as ET
import hashlib,json,re,unicodedata,zipfile
ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://www.w3.org/2000/svg','a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
def norm(text):
    return re.sub(r'\s+','',unicodedata.normalize('NFKC',text)).replace('\u200b','').replace('\u2061','')
issues=[];objects=0;equations=0
for lecture in [1,2,3,5]:
    native=json.loads((ROOT/f'sources/lecture{lecture}-native.json').read_text(encoding='utf-8'))
    path=ROOT/'public/sources/powerpoint'/native['source']
    assert hashlib.sha256(path.read_bytes()).hexdigest()==native['sha256']
    parent=ROOT.parent/native['source']
    if parent.exists():assert hashlib.sha256(parent.read_bytes()).digest()==hashlib.sha256(path.read_bytes()).digest()
    with zipfile.ZipFile(path) as archive:
        for page in native['slides']:
            xml=ET.fromstring(archive.read(f'ppt/slides/slide{page["number"]}.xml'))
            for item in page['objects']:
                original=ET.fromstring(archive.read(item['sourcePart'])) if 'sourcePart' in item else xml
                ident=item.get('sourceShapeId',item['id'])
                node=original.xpath(f'//p:cNvPr[@id="{ident}"]',namespaces=NS)[0].getparent().getparent()
                svg=ET.fromstring(('<svg xmlns="http://www.w3.org/2000/svg">'+item['svg']+'</svg>').encode())
                actual=norm(''.join(''.join(t.itertext()) for t in svg.xpath('//s:text[not(@fill-opacity="0")]',namespaces=NS)))
                if item['omml']:
                    for equation in node.xpath('.//m:oMath',namespaces=NS):
                        expected=norm(''.join(equation.xpath('.//m:t/text()',namespaces=NS)))
                        if expected not in actual:issues.append({'lecture':lecture,'slide':page['number'],'shape':ident,'kind':'equation','expected':expected,'actual':actual})
                    equations+=len(item['omml'])
                for p in node.xpath('.//a:p',namespaces=NS):
                    text=p.xpath('.//a:t/text()',namespaces=NS)
                    # Equation glyphs can separate ordinary runs in one paragraph.
                    for part in text if item['omml'] else [''.join(text)]:
                        expected=norm(part)
                        if expected not in actual and expected.casefold() not in actual.casefold():
                            issues.append({'lecture':lecture,'slide':page['number'],'shape':ident,'kind':'text','expected':expected,'actual':actual})
                objects+=1
canva=json.loads((ROOT/'sources/canva-native.json').read_text(encoding='utf-8'))
gold=json.loads((ROOT/'sources/verbatim-canva.json').read_text(encoding='utf-8'))
for page in canva['pages']:
    html=ET.HTML((ROOT/f'sources/canva-native/{page["number"]:02}.html').read_text(encoding='utf-8'))
    actual=norm(''.join(html.itertext())).casefold()
    original=next(p for p in gold if p['number']==page['number'])
    for paragraph in original['paragraphs']:
        expected=norm(paragraph).casefold()
        if expected not in actual:issues.append({'lecture':9,'slide':page['number'],'kind':'text','expected':expected,'actual':actual})
print(json.dumps({'nativePowerPointObjects':objects,'sourceEquations':equations,'CanvaPages':len(canva['pages']),'issues':issues},ensure_ascii=False,indent=2))
if issues:raise SystemExit(1)
