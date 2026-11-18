"""Rebuild the approved source-faithful lecture sequence. No authored rewrite."""
from pathlib import Path
import json,runpy
ROOT=Path(__file__).resolve().parents[1]
FILES={1:'01-geometry.md',2:'02-elimination.md',3:'03-products-inverses.md',5:'05-permutations-spaces.md',9:'09-independence-basis.md'}
TITLES={1:'Geometry of linear equations',2:'Elimination with matrices',3:'Matrix multiplication and inverses',5:'Permutations, transposes, and vector spaces',9:'Independence, basis, and dimension'}
def build():
    runpy.run_path(str(ROOT/'scripts/build-lecture1-native.py'))['build']()
    runpy.run_path(str(ROOT/'scripts/build-remaining-native.py'))['build']()
    canva=json.loads((ROOT/'sources/canva-native.json').read_text(encoding='utf-8'))
    parts=[]
    for page in canva['pages']:
        n=page['number'];fields={'layout':'none','lecture':9,'title':f'Lecture 9 · original page {n}','sourceDeck':'CanvaLecture9','sourceSlide':n,'clicks':0}
        if not parts:fields.update(routeAlias='lecture-9',section=True)
        parts.append('---\n'+'\n'.join(f'{k}: {json.dumps(v)}' for k,v in fields.items())+f'\n---\n\n<CanvaSource :slide="{n}" />\n')
    (ROOT/'lectures'/FILES[9]).write_text('\n'.join(parts),encoding='utf-8')
    index=[];start=1
    for lecture in FILES:
        count=len(canva['pages']) if lecture==9 else len(json.loads((ROOT/f'sources/lecture{lecture}-native.json').read_text(encoding='utf-8'))['slides'])
        index.append({'lecture':lecture,'title':TITLES[lecture],'start':start,'file':'lectures/'+FILES[lecture],'originals':count,'new_labs':0,'total':count,'rendering':'source-native-html' if lecture==9 else 'source-native-svg'})
        start+=count
    (ROOT/'sources/lecture-index.json').write_text(json.dumps(index,indent=2)+'\n',encoding='utf-8')
    print(f'Built {start-1} original source slides in lecture order 1, 2, 3, 5, 9.')
if __name__=='__main__':build()
