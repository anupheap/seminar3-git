"""Audit code order, available variables, matrix entries, and plotted results.

Run after regenerating visual_states.json:
    python python_examples/audit.py
"""
from pathlib import Path
import ast
import contextlib
import io
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
PROJECTION=np.array([[.78,-.55,0],[-.28,-.25,.84]])


def audit():
    lessons=json.loads((ROOT/'walkthroughs.json').read_text(encoding='utf-8'))
    scenes=json.loads((ROOT/'visual_states.json').read_text(encoding='utf-8'))
    report=[]
    for lesson in lessons:
        previous='';stages=[]
        for k,source in enumerate(lesson['steps']):
            assert not previous or source.startswith(previous+'\n'),f'Prior code disappeared: {lesson["title"]}'
            previous=source
            env={};stdout=io.StringIO()
            with contextlib.redirect_stdout(stdout):exec(compile(source,lesson['title'],'exec'),env)
            scene=scenes[lesson['figure']]['states'][k]
            nodes={n['id']:n for n in scene['nodes']}
            checks=[]
            def same(label,actual,expected):
                assert np.allclose(actual,expected),f'{lesson["figure"]}, step {k+1}: {label}'
                checks.append(label)
            def has_node(id,present):
                assert (id in nodes)==present,f'{lesson["figure"]}: premature or missing {id}'
                checks.append(f'{id}: present' if present else f'{id}: withheld')
            def matrix(id,expected):
                for (i,j),value in np.ndenumerate(expected):same(f'{id}[{i},{j}]',float(nodes[f'{id}-{i}-{j}']['text']),value)
            def point(bounds,xy,box=(42,44,335,204)):
                xmin,xmax,ymin,ymax=bounds;x,y,w,h=box
                return np.array([x+(xy[0]-xmin)/(xmax-xmin)*w,y+h-(xy[1]-ymin)/(ymax-ymin)*h])
            def projection(v,center,scale):
                p=PROJECTION@v
                return np.array(center)+scale*np.array([p[0],-p[1]])

            # Every exported numerical variable must be available in this code state.
            for name,value in scene['values'].items():
                if name=='rank':expected=env['r']
                elif name=='nullity':expected=env['N'].shape[1]
                elif name=='display':expected=env['P']@env['R'] if 'P' in env else env.get('R',env['A'])
                else:
                    assert name in env,f'Visualization used future variable {name}'
                    expected=env[name]
                same(f'exported {name}',value,expected)

            f=lesson['figure']
            if f=='01-solve':
                for i,id in enumerate(['row1','row2']):
                    endpoints=np.array(nodes[id]['points']).reshape(-1,2)
                    for px,py in endpoints:
                        xy=np.array([-.5+(px-42)/335*3.5,5-(py-44)/204*5.5])
                        same(f'equation {i+1} line endpoint',env['A'][i]@xy,env['b'][i])
                has_node('solution','x' in env);has_node('check',k==2)
                if 'x' in env:same('solution point',nodes['solution']['points'][:2],point((-.5,3,-.5,5),env['x']))
            elif f=='02-columns':
                end=env['a2'] if k==0 else env['b']
                same('second column endpoint',nodes['a2']['points'][2:],point((-2.7,3,-2,5),end))
                has_node('sum','b' in env);has_node('result','x' in env)
            elif f=='03-elimination':matrix('aug',env['Ab'])
            elif f=='04-back-substitution':
                matrix('upper',np.column_stack((env['U'],env['c'])))
                for i,v in enumerate(env['x']):same(f'solution entry {i}',float(nodes[f'x-{i}']['text']),v)
                has_node('check',k==2)
            elif f=='05-products':
                matrix('C',env['C'])
                has_node('term0-0-0','terms' in env)
                has_node('ba-square',k==2)
                if 'terms' in env:
                    for i,term in enumerate(env['terms']):matrix(f'term{i}',term)
                    same('outer product sum',sum(env['terms']),env['C'])
            elif f=='06-inverse':
                matrix('aug',env['aug'])
                has_node('identity-0-0','inverse' in env)
                if 'inverse' in env:matrix('identity',np.round(env['A']@env['inverse'],10))
            elif f=='07-transpose':
                expected=env['P']@env['R'] if 'P' in env else env.get('R',env['A'])
                rows,cols=expected.shape
                for (i,j),value in np.ndenumerate(expected):
                    key=f'entry-v{value:g}'
                    same(f'transposed entry {value}',nodes[key]['points'],[210-cols*24+(j+.5)*48,134-rows*24+(i+.5)*48+6])
            elif f=='08-subspace':
                has_node('w','w' in env and k==1);has_node('minus-q','q' in env)
                if k==1:same('w endpoint',nodes['w']['points'][2:],point((-3,8,-6,16),env['w']))
                if k==2:same('negative q endpoint',nodes['minus-q']['points'][2:],point((-2,2,-2,2),-env['q']))
            elif f=='09-column-space':
                for name in ['good','bad']:
                    has_node(name,name in env)
                    if name in env:same(f'{name} target',nodes[name]['points'][:2],point((-.5,5,-1,10),env[name][:,-1]))
            elif f=='10-nullspace':
                has_node('shift-surface','xp' in env);has_node('x','x' in env);has_node('check',k==2)
                if 'x' in env:same('affine solution point',nodes['x']['points'][:2],projection(env['x'],[165,154],24))
            elif f=='11-coordinates':
                has_node('coords','c' in env)
                same('target endpoint',nodes['target']['points'][2:],point((-1,4.5,-1,3),env['v']))
                if 'c' in env:same('weighted basis reconstructs target',env['V']@env['c'],env['v'])
            elif f=='12-rank':
                has_node('null-line','N' in env);has_node('check',k==2)
                if 'N' in env:
                    same('nullspace goes to zero',env['M']@env['N'],0)
                    same('nullspace line endpoint',nodes['null-line']['points'][2:],projection(2.4*env['N'][:,0],[320,151],40))
            stages.append(dict(step=k+1,variables=sorted(n for n in env if not n.startswith('__') and n not in ['np','null_space']),
                introducedLines=lesson['introducedLines'][k],stdout=stdout.getvalue(),checks=len(checks),passed=True))
        report.append(dict(slide=lesson['slide'],title=lesson['title'],states=stages,passed=True))
    result=dict(walkthroughs=len(report),states=sum(len(r['states']) for r in report),
                checks=sum(s['checks'] for r in report for s in r['states']),passed=True,results=report)
    (ROOT/'audit.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'Audit passed: {result["states"]} states, {result["checks"]} code/visual checks, cumulative order in all 12 walkthroughs.')
    return result


if __name__=='__main__':audit()
