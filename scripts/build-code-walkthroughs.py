"""Read-only Magic Move code: preserve original examples and reveal cumulative steps."""
from pathlib import Path
import contextlib,io,json,re
import numpy as np
from sympy import Matrix
ROOT=Path(__file__).resolve().parents[1]

def python_outputs(stages):
    result=[]
    for code in stages:
        stream=io.StringIO()
        with contextlib.redirect_stdout(stream):exec(compile(code,'<slide-code>','exec'),{})
        result.append(stream.getvalue().rstrip())
    return result

def magic(language,stages,highlights=None,lines=False):
    blocks=[]
    for i,code in enumerate(stages):
        hl=highlights[i] if highlights else '*'
        blocks.append(f'```{language} {{{hl}}}\n{code}\n```')
    return '````md magic-move {at:1, duration:500, lines:'+str(lines).lower()+'}\n'+'\n'.join(blocks)+'\n````'

def read_shape(lecture,slide,ident):
    native=json.loads((ROOT/f'sources/lecture{lecture}-native.json').read_text(encoding='utf-8'))
    page=next(p for p in native['slides'] if p['number']==slide)
    return next(o for o in page['objects'] if o['id']==ident)

def examples():
    p='\n'.join(read_shape(3,10,15)['paragraphs'])
    inv='\n'.join(read_shape(3,11,3)['paragraphs'])
    symmetric='''import numpy as np
R = np.array([[1, 2], [3, 0], [0, 4]], dtype=float)

RT_R = R.T @ R

is_symmetric = np.allclose(RT_R, RT_R.T)

print("R^T * R:\\n", RT_R)
print("Is symmetric?:", is_symmetric)'''
    rank='''from sympy import Matrix

A = Matrix([[3, 4, 7],
            [2, 7, 9],
            [5, 2, 7]])

n_vectors = A.shape[1]
rank = A.rank()

print("Number of vectors:", n_vectors)
print("Rank:", rank)
print("Linearly independent?", rank == n_vectors)'''
    setup='''from sympy import Matrix
A = Matrix([[1, 1, 2],
            [2, 1, 3],
            [3, 1, 4],
            [4, 1, 5]])'''
    column=setup+'''

columns = A.columnspace()
print([list(v) for v in columns])

x = Matrix([2, -1, 0])
print("A*x =", list(A*x))'''
    null=setup+'''

n = -A.nullspace()[0]
print("n =", list(n))
print("A*n =", list(A*n))

x0 = Matrix([1, 0, 0])
print("A*x0 =", list(A*x0))
print("A*(x0+2*n) =", list(A*(x0+2*n)))'''
    cumulative=lambda code,ends:['\n'.join(code.splitlines()[:end]) for end in ends]
    inverse_base='\n'.join(read_shape(3,11,5)['paragraphs']).rstrip()
    inverse_identity=inverse_base+'\n\nans =\n     1     0\n     0     1'
    inverse_checked=inverse_identity+'\n\nans =\n    -5     3\n     2    -1'
    data={
      'l3-product':{'language':'matlab','stages':cumulative(p,[1,2,3]),'outputs':['','','\n'.join(read_shape(3,10,16)['paragraphs'])],'highlights':['1','2','3']},
      'l3-inverse':{'language':'matlab','stages':cumulative(inv,[1,2,3,4,5]),'outputs':['','M =\n     1     0    -5     3\n     0     1     2    -1',inverse_base,inverse_identity,inverse_checked],'highlights':['1','2','3','4','5']},
      'l5-symmetric':{'language':'python','stages':cumulative(symmetric,[2,4,6,8,9]),'highlights':['1-2','4','6','8','9']},
      'l9-rank':{'language':'python','stages':cumulative(rank,[5,8,10,11,12]),'highlights':['1-5','7-8','10','11','12']},
      'l6-column':{'language':'python','stages':cumulative(column,[5,8,11]),'highlights':['1-5','7-8','10-11']},
      'l6-null':{'language':'python','stages':cumulative(null,[5,8,9,12,13]),'highlights':['1-5','7-8','9','11-12','13']},
    }
    for key,item in data.items():
        if item['language']=='python':item['outputs']=python_outputs(item['stages'])
        item['outputLines']=[len(stage.splitlines()) if output!=(item['outputs'][i-1] if i else '') else None for i,(stage,output) in enumerate(zip(item['stages'],item['outputs']))]
    # Validate the MATLAB examples without modifying their original code.
    assert Matrix([[1,2],[3,4]])*Matrix([[5,6],[7,8]])==Matrix([[19,22],[43,50]])
    assert Matrix([[1,3],[2,5]]).inv()==Matrix([[-5,3],[2,-1]])
    A=Matrix([[1,1,2],[2,1,3],[3,1,4],[4,1,5]])
    assert A[:,2]==A[:,0]+A[:,1] and A.rank()==2
    assert A*Matrix([1,1,-1])==Matrix.zeros(4,1)
    assert -A.nullspace()[0]==Matrix([1,1,-1])
    assert A*Matrix([2,-1,0])==Matrix([1,3,5,7])
    assert A*Matrix([1,0,0])==A*(Matrix([1,0,0])+2*A.nullspace()[0])
    (ROOT/'sources/code-walkthroughs.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return data

def code_body(key,background,code_bounds,output_bounds,style):
    data=examples()[key]
    pos=lambda b:';'.join(f'{k}:{v}%' for k,v in zip(['left','top','width','height'],b))
    return background+f'\n\n<div class="stepped-source-code {style}" style="{pos(code_bounds)}">\n\n'+magic(data['language'],data['stages'],data['highlights'])+f'\n\n</div>\n\n<div class="stepped-source-result {style}" style="{pos(output_bounds)}"><CodeWalkOutput lesson="{key}" /></div>\n'

def apply():
    data=examples()
    replacements={
      (3,10):('l3-product',code_body('l3-product','<PowerPointSource :lecture="3" :slide="10" :hide-shapes="[15,16]" />',[4.375,27.7778,35.9375,55.5556],[59.6875,27.7778,35.9375,55.5556],'walk-matlab')),
      (3,11):('l3-inverse',code_body('l3-inverse','<PowerPointSource :lecture="3" :slide="11" :hide-shapes="[3,5]" />',[4.375,22.7778,62.5,70],[69.375,22.7778,26.25,70],'walk-inverse')),
      (5,7):('l5-symmetric',code_body('l5-symmetric','<PowerPointSource :lecture="5" :slide="7" :hide-shapes="[6,11]" />',[3.6394,31.6641,49,43],[59.2628,32.6893,33.9631,27.8],'walk-numpy')),
      (9,25):('l9-rank',code_body('l9-rank','<CanvaSource :slide="25" :hide-images="true" />',[7.88,42,42,45],[53.7,48,37.65,31],'walk-sympy')),
    }
    files={3:'03-products-inverses.md',5:'05-permutations-spaces.md',9:'09-independence-basis.md'}
    for lecture,filename in files.items():
        path=ROOT/'lectures'/filename;parts=re.split(r'(?m)^---\s*$\n?',path.read_text(encoding='utf-8'));output=[]
        for i in range(1,len(parts),2):
            meta=parts[i].strip();body=parts[i+1].strip();source=re.search(r'^sourceSlide:\s*(\d+)',meta,re.M)
            entry=replacements.get((lecture,int(source[1]))) if source else None
            if entry:
                key,body=entry;meta=re.sub(r'^clicks:\s*\d+',f'clicks: {len(data[key]["stages"])-1}',meta,flags=re.M)
                meta=re.sub(r'(?m)^(?:codeCopy|magicMoveCopy):.*\n?','',meta).strip()+'\ncodeCopy: false\nmagicMoveCopy: false'
            output.append('---\n'+meta+'\n---\n\n'+body+'\n')
        path.write_text('\n'.join(output),encoding='utf-8')
    path=ROOT/'lectures/06-column-nullspace.md'
    parts=re.split(r'(?m)^---\s*$\n?',path.read_text(encoding='utf-8'));output=[]
    for i in range(1,len(parts),2):
        meta=parts[i].strip();body=parts[i+1].strip()
        lesson=re.search(r'<CodeWalkOutput lesson="(l6-[^"]+)"',body)
        if lesson:
            item=data[lesson[1]]
            meta=re.sub(r'^clicks:\s*\d+',f'clicks: {len(item["stages"])-1}',meta,flags=re.M)
            body=re.sub(r'(?ms)^````md magic-move\b.*?^````[ \t]*$',lambda _:magic(item['language'],item['stages'],item['highlights']),body)
        output.append('---\n'+meta+'\n---\n\n'+body+'\n')
    path.write_text('\n'.join(output),encoding='utf-8')
    print('Restored read-only Magic Move in all four original code sections; verified every Python stage.')
    return data

if __name__=='__main__':apply()
