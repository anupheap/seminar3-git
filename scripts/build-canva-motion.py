"""Restore saved Canva effects and add the requested float entrance to graphics."""
from pathlib import Path
import json
from lxml import etree as ET

ROOT=Path(__file__).resolve().parents[1]
settings=json.loads((ROOT/'sources/canva-animation-settings.json').read_text(encoding='utf-8'))
pages=[]
for page in settings['pages']:
    number=page['number'];prefix=f'canva-{number}-'
    html=ET.HTML((ROOT/f'sources/canva-native/{number:02}.html').read_text(encoding='utf-8'))
    models={e['id']:e for e in page['elements']}
    saved={e['id']:e['animation'] for e in page['elements'] if e.get('animation',{} ) and e['animation'].get('A?')=='B'}
    for ident,animation in saved.items():
        assert animation['A'] in [8,30,31],f'Unreviewed Canva preset: {number}/{ident}/{animation}'
    targets=set(saved)
    for image in html.xpath('//img|//*[local-name()="image"]|//*[@role="img"]'):
        for ancestor in [image,*image.iterancestors()]:
            ident=ancestor.get('id','')
            if ident.startswith(prefix+'LB'):
                targets.add(ident[len(prefix):]);break
    # A card/group already carries its children's graphic entrance.
    def covered(ident):
        parent=models.get(ident,{}).get('parent')
        while parent:
            if parent in targets:return True
            parent=models.get(parent,{}).get('parent')
        return False
    targets=[e for e in page['elements'] if e['id'] in targets and not covered(e['id'])]
    effects=[]
    for i,model in enumerate(targets):
        ident=model['id'];animation=saved.get(ident)
        assert html.xpath('//*[@id=$id]',id=prefix+ident),f'Missing native target {number}/{ident}'
        effect={'id':ident,'duration':1000 if animation and animation['A']==31 else 900,
                'delay':min(360,i*110),'distance':64,'sourceSettings':animation,
                'floatOrigin':'source-preset' if animation and animation['A']==31 else 'requested-for-all-graphics'}
        if animation and animation['A']==8:effect['wipe']={'duration':1000,'direction':'left-to-right'}
        if animation and animation['A']==30:effect['paint']={'duration':settings['maskAsset']['duration'],'file':settings['maskAsset']['file']}
        if number==25:
            effect['replacement']='code' if model['bounds'][0]+model['bounds'][2]/2<960 else 'output'
            effect['delay']=0
        effects.append(effect)
    pages.append({'number':number,'pageId':page['id'],'effects':effects,'savedEffects':len(saved)})
manifest={'source':settings['source'],'pages':pages,'loops':'sources/canva-liquid.json',
          'notes':'Saved presets 8/30/31 are recreated with directional clipping, the original paint mask, and float entrances. Remaining picture graphics also float in as requested. Native elements stay mounted; no slide-image overlays or final-image swaps.'}
(ROOT/'sources/canva-motion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Reviewed {len(pages)} Canva pages: {sum(p["savedEffects"] for p in pages)} saved effects; {sum(len(p["effects"]) for p in pages)} graphic/group entrances; 3 original liquid loops retained.')
