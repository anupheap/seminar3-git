"""Source-faithful native PowerPoint objects for Lectures 2, 3 and 5."""
from pathlib import Path
import importlib.util
import json
import hashlib
import zipfile
from lxml import etree as ET

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('source_objects',ROOT/'scripts/build-lecture1-native.py')
helpers=importlib.util.module_from_spec(spec);spec.loader.exec_module(helpers)
helpers.ASSET_DIRECTORY='native-assets'
NS=helpers.NS
FILES={2:'02-elimination.md',3:'03-products-inverses.md',5:'05-permutations-spaces.md'}

def build(prepare_math=False):
    originals=json.loads((ROOT/'sources/powerpoint.json').read_text(encoding='utf-8-sig'))
    for lecture,file in FILES.items():
        directory=ROOT/f'.cache/lecture{lecture}-native'
        manifest=json.loads((directory/'manifest.json').read_text(encoding='utf-8-sig'))
        original=next(d for d in originals if d['id']==manifest['deck'])
        metric_path=ROOT/f'sources/lecture{lecture}-math-metrics.json'
        metrics={(m['slide'],m['shape']):m['tokens'] for m in json.loads(metric_path.read_text(encoding='utf-8'))} if metric_path.exists() and not prepare_math else {}
        source_path=ROOT/f'public/sources/powerpoint/{manifest["deck"]}.pptx'
        result={'source':manifest['deck']+'.pptx','lecture':lecture,'width':manifest['width'],'height':manifest['height'],
                'sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),'slides':[]}
        markdown=[]
        with zipfile.ZipFile(source_path) as source:
            for page in manifest['slides']:
                number=page['number'];xml=ET.fromstring(source.read(f'ppt/slides/slide{number}.xml'))
                previous=original['slides'][number-1]
                entry={'number':number,'background':helpers.background_for(source,f'ppt/slides/slide{number}.xml'),
                       'backgroundColor':page['backgroundColor'],'clicks':previous['clicks'],'effects':previous['effects'],'objects':[]}
                for item in page.get('inherited',[])+page['objects']:
                    shape_xml=ET.fromstring(source.read(item['part'])) if 'part' in item else xml
                    shape=helpers.source_shape(shape_xml,item.get('shapeId',item['id']))
                    paragraphs=[''.join(p.xpath('.//a:t/text()',namespaces=NS)) for p in shape.xpath('.//a:p',namespaces=NS)]
                    equations=[ET.tostring(n,encoding='unicode') for n in shape.xpath('.//m:oMath',namespaces=NS)]
                    svg=helpers.clean_svg(directory/item['file'],f'l{lecture}-s{number}-o{item["id"]}',metrics.get((number,item['id'])))
                    if lecture==2 and number==20 and item['id']==7:
                        exported=ET.parse(directory/item['file'])
                        rect=exported.xpath('//svg:clipPath/svg:rect',namespaces=NS)[0]
                        x,y,w,h=(float(rect.get(a)) for a in ('x','y','width','height'))
                        svg=f'<rect x="{x+1}" y="{y+1}" width="{w-2}" height="{h-2}" fill="#FFFFFF" />'
                    entry['objects'].append({'id':item['id'],'name':item['name'],'bounds':item['bounds'],'paragraphs':paragraphs,'omml':equations,'svg':svg,
                                             **({'sourcePart':item['part'],'sourceShapeId':item['shapeId']} if 'part' in item else {})})
                if lecture==2 and number==20:
                    # Requested smooth objective entrance, with original copy and layout.
                    delays={2:0,7:.08,3:.18,8:.18,4:.34,9:.34,5:.50,10:.50,6:.66,11:.66}
                    entry['effects']=[{'shape':obj['id'],'type':2,'step':0,'direction':2,'duration':.55,'delay':delays[obj['id']],'exit':False}
                                      for obj in entry['objects']]
                result['slides'].append(entry)
                fields={'layout':'none','lecture':lecture,'title':f'Lecture {lecture} · original slide {number}',
                        'clicks':entry['clicks'],'sourceDeck':manifest['deck'],'sourceSlide':number}
                if not markdown:fields.update(routeAlias=f'lecture-{lecture}',section=True)
                markdown.append('---\n'+'\n'.join(f'{k}: {json.dumps(v,ensure_ascii=False)}' for k,v in fields.items())
                                +f'\n---\n\n<PowerPointSource :lecture="{lecture}" :slide="{number}" />\n')
        (ROOT/f'sources/lecture{lecture}-native.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        (ROOT/'lectures'/file).write_text('\n'.join(markdown),encoding='utf-8')
        print(f'Lecture {lecture}: {len(result["slides"])} source slides, {sum(len(s["objects"]) for s in result["slides"])} native objects.')

if __name__=='__main__':
    import sys
    build(prepare_math='--prepare-math' in sys.argv)
