"""Build click-synchronized SVG scenes from the actual Python code states.

Run: python python_examples/visual_states.py
The browser interpolates these numerical snapshots. It needs no Python runtime.
"""
from pathlib import Path
import contextlib
import io
import json
import numpy as np

BLUE='#246a9c'
ORANGE='#c15b35'
GREEN='#32816b'
INK='#192b3a'
MUTED='#657681'
RULE='#d8ddd9'
RED='#b34538'


class Scene:
    def __init__(self,title,caption,status=''):
        self.nodes=[]
        self.caption=caption
        self.status=status
        self.text('title',210,22,title,16,INK,'middle',600)

    def add(self,id,kind,points,**kwargs):
        self.nodes.append(dict(id=id,kind=kind,points=[float(p) for p in points],opacity=1,**kwargs))

    def text(self,id,x,y,text,size=15,color=INK,anchor='start',weight=400):
        self.add(id,'text',[x,y],text=str(text),size=size,fill=color,anchor=anchor,weight=weight)

    def line(self,id,a,b,color=RULE,width=1,dashed=False,arrow=False,opacity=1):
        self.add(id,'line',list(a)+list(b),stroke=color,width=width,dashed=dashed,arrow=arrow)
        self.nodes[-1]['opacity']=opacity

    def poly(self,id,points,color=BLUE,fill='none',opacity=1,width=2,closed=False):
        self.add(id,'polygon' if closed else 'polyline',np.asarray(points).flatten(),stroke=color,fill=fill,width=width)
        self.nodes[-1]['opacity']=opacity

    def dot(self,id,p,color=GREEN,r=4):
        self.add(id,'circle',list(p)+[r],fill=color,stroke='#f7f5ee',width=1.5)

    def rect(self,id,x,y,w,h,fill,opacity=1,stroke='none',width=1):
        self.add(id,'rect',[x,y,w,h,2],fill=fill,stroke=stroke,width=width)
        self.nodes[-1]['opacity']=opacity

    def matrix(self,id,values,x=210,y=120,cell=42,title=None,pivots=(),active_rows=(),colors=None,value_ids=False):
        values=np.asarray(values)
        rows,cols=values.shape
        left=x-cols*cell/2
        top=y-rows*cell/2
        if title:self.text(id+'-name',x,top-13,title,15,INK,'middle',600)
        for (i,j),v in np.ndenumerate(values):
            key=f'{id}-v{v:g}' if value_ids else f'{id}-{i}-{j}'
            cx=left+(j+.5)*cell
            cy=top+(i+.5)*cell
            c=colors[i] if colors else INK
            fill='#e7eef3' if abs(v)>0 else '#f0f1ed'
            if i in active_rows: fill='#f3e7dd'
            self.rect(key+'-bg',cx-cell*.46,cy-cell*.43,cell*.92,cell*.86,fill)
            self.text(key,cx,cy+6,f'{v:g}',22 if cell>=35 else 16,c,'middle',500)
            if (i,j) in pivots:
                self.rect(key+'-pivot',cx-cell*.45,cy-cell*.42,cell*.9,cell*.84,'none',stroke=GREEN,width=2.2)
        for side,sx in [('l',left-5),('r',left+cols*cell+5)]:
            d=5 if side=='l' else -5
            self.poly(id+'-'+side,[[sx+d,top],[sx,top],[sx,top+rows*cell],[sx+d,top+rows*cell]],MUTED,width=1.5)
        return left,top,cols*cell,rows*cell

    def finish(self,**values):
        return dict(nodes=self.nodes,caption=self.caption,status=self.status,values=values)


def chart(scene,prefix='axes',bounds=(-1,4,-1,5),box=(42,44,335,204),labels=('x','y')):
    xmin,xmax,ymin,ymax=bounds
    x,y,w,h=box
    def p(a,b):return np.array([x+(a-xmin)/(xmax-xmin)*w,y+h-(b-ymin)/(ymax-ymin)*h])
    for i,t in enumerate(np.linspace(xmin,xmax,6)):
        scene.line(f'{prefix}-gx{i}',p(t,ymin),p(t,ymax),RULE,.8)
    for i,t in enumerate(np.linspace(ymin,ymax,6)):
        scene.line(f'{prefix}-gy{i}',p(xmin,t),p(xmax,t),RULE,.8)
    scene.line(prefix+'-x',p(xmin,0),p(xmax,0),MUTED,1.2)
    scene.line(prefix+'-y',p(0,ymin),p(0,ymax),MUTED,1.2)
    scene.text(prefix+'-xl',x+w+7,p(0,0)[1]+4,labels[0],13,MUTED)
    scene.text(prefix+'-yl',p(0,0)[0]-8,y-6,labels[1],13,MUTED,'end')
    scene.text(prefix+'-zero',p(0,0)[0]-9,p(0,0)[1]+15,'0',11,MUTED)
    return p


def arrow(scene,id,p,start,end,color,name=None,offset=(7,-7),opacity=1):
    scene.line(id,p(*start),p(*end),color,3,arrow=True,opacity=opacity)
    if name:
        at=p(*end)+np.asarray(offset)
        scene.text(id+'-label',*at,name,14,color)


def solve(k,env):
    s=Scene(['Two equations define the system','The solution reaches the intersection','The residual checks the solution'][k],
            ['A and b define the two row equations. No solution has been computed yet.',
             'solve(A, b) gives x = (1, 2), the point shared by both lines.',
             'The residual Ax − b is zero in both equations.'][k])
    p=chart(s,bounds=(-.5,3,-.5,5))
    s.line('row1',p(-.25,-.5),p(2.5,5),BLUE,2.5)
    s.line('row2',p(-.5,1.25),p(3,3),ORANGE,2.5)
    s.text('eq1',50,60,'2x − y = 0',14,BLUE)
    s.text('eq2',245,80,'−x + 2y = 3',14,ORANGE)
    if 'x' in env:
        v=env['x'];q=p(*v)
        s.dot('solution',q)
        s.line('guide-x',p(v[0],0),q,MUTED,1,True)
        s.line('guide-y',p(0,v[1]),q,MUTED,1,True)
        s.text('solution-label',*(q+[10,20]),'(1, 2)',16,GREEN)
    if k==2:s.text('check',210,278,'Ax − b = (0, 0)   ✓',17,GREEN,'middle',600)
    return s.finish(**{key:env[key].tolist() for key in ['A','b','x'] if key in env})


def columns(k,env):
    s=Scene(['The two columns of A','The weighted sum produces b','Column addition equals A @ x'][k],
            ['a₁ and a₂ are drawn separately from the origin.',
             'The second column doubles and moves to the tip of a₁. Their sum is b.',
             'x = (1, 2) supplies the same weights to matrix multiplication.'][k])
    p=chart(s,bounds=(-2.7,3,-2,5))
    a1,a2=env['a1'],env['a2']
    arrow(s,'a1',p,[0,0],a1,BLUE,'a₁')
    start=np.zeros(2) if k==0 else a1
    end=a2 if k==0 else a1+2*a2
    arrow(s,'a2',p,start,end,ORANGE)
    s.text('a2-label',135 if k==0 else 225,105 if k==0 else 160,'a₂' if k==0 else '2a₂',15,ORANGE)
    if k>=1:
        arrow(s,'sum',p,[0,0],env['b'],GREEN,'b = (0, 3)',(-100,-10))
    if k==2:s.text('result',210,278,'a₁ + 2a₂ = A @ (1, 2) = (0, 3)',16,GREEN,'middle',600)
    return s.finish(**{key:env[key].tolist() for key in ['A','a1','a2','b','x'] if key in env})


def elimination(k,env):
    s=Scene(['The original augmented matrix','Eliminate the first column','The triangular system is ready'][k],
            ['The last column is b. Every row operation must update it too.',
             'R₂ − 2R₁ and R₃ − R₁ create the first two zeros.',
             'R₃ + 2R₂ creates the last zero. The pivots are 1, 1, and 9.'][k])
    box=s.matrix('aug',env['Ab'],210,128,48,pivots=[(0,0),(1,1),(2,2)] if k==2 else [(0,0)],active_rows=[1,2] if k==1 else [])
    left,top,w,h=box
    s.line('divider',[left+3*48,top-3],[left+3*48,top+h+3],ORANGE,1.8)
    s.text('a-title',left+72,top-16,'A',15,BLUE,'middle')
    s.text('b-title',left+168,top-16,'b',15,ORANGE,'middle')
    s.text('operation',210,246,['[A | b]','R₂ ← R₂ − 2R₁     R₃ ← R₃ − R₁','R₃ ← R₃ + 2R₂'][k],16,INK,'middle')
    if k==2:s.text('result',210,277,'Pivots: 1, 1, 9',17,GREEN,'middle',600)
    return s.finish(Ab=env['Ab'].tolist())


def back_substitution(k,env):
    s=Scene(['Initialize the solution vector','Solve z, then y','Solve x and check U @ x'][k],
            ['U and c form the triangular system. x starts as a vector of zeros.',
             'The bottom two equations give z = 1 and y = 1. x₁ is still uncomputed.',
             'The top equation gives x₁ = 1. U @ x equals c.'][k])
    augmented=np.column_stack((env['U'],env['c']))
    box=s.matrix('upper',augmented,210,113,42,active_rows=[] if k==0 else [1,2] if k==1 else [0])
    s.line('divider',[box[0]+126,box[1]],[box[0]+126,box[1]+126],ORANGE,1.5)
    s.text('solution-title',74,231,'x =',18,INK,'end')
    x=env['x']
    for i,v in enumerate(x):
        color=GREEN if k==2 or k==1 and i>0 else MUTED
        s.text(f'x-{i}',115+i*85,231,f'{v:g}',24,color,'middle',600)
        s.text(f'x-name-{i}',115+i*85,253,['x₁','x₂','x₃'][i],13,MUTED,'middle')
    if k==2:s.text('check',210,280,'U @ x = (4, 2, 9) = c   ✓',16,GREEN,'middle',600)
    return s.finish(U=env['U'].tolist(),c=env['c'].tolist(),x=x.tolist())


def product_plot(s,prefix,T,box,columns=False):
    p=chart(s,prefix,(-6,6,-4,4),box,('',''))
    square=T@np.array([[0,1,1,0],[0,0,1,1]])
    s.poly(prefix+'-square',[p(*q) for q in square.T],BLUE,'#d8e5ee',.7,1.8,True)
    if columns:
        arrow(s,prefix+'-c1',p,[0,0],T[:,0],BLUE)
        arrow(s,prefix+'-c2',p,[0,0],T[:,1],ORANGE)


def products(k,env):
    s=Scene(['The product C = A @ B','Build C one column at a time','Outer products add to the same C'][k],
            ['C maps the unit square to the displayed parallelogram.',
             'The blue and orange arrows are A times the two columns of B.',
             'The two rank-one terms sum to C. The reversed product BA differs.'][k])
    C=env['C']
    if k<2:
        s.matrix('C',C,95,135,40,title='C = AB',colors=None)
        product_plot(s,'ab',C,(210,65,180,160),columns=k==1)
        if k==1:
            s.text('col1',94,225,'C[:, 0] = (2, −1)',14,BLUE,'middle')
            s.text('col2',94,248,'C[:, 1] = (3, 0)',14,ORANGE,'middle')
    else:
        terms=env['terms']
        s.matrix('term0',terms[0],65,90,32,title='column 1 × row 1')
        s.matrix('term1',terms[1],205,90,32,title='column 2 × row 2')
        s.matrix('C',C,350,90,32,title='C = AB')
        s.text('plus',135,98,'+',21,INK,'middle')
        s.text('equals',277,98,'=',21,INK,'middle')
        product_plot(s,'ab',C,(35,168,155,80))
        product_plot(s,'ba',env['B']@env['A'],(240,168,155,80))
        s.text('ab-label',112,272,'AB',16,BLUE,'middle',600)
        s.text('ba-label',317,272,'BA ≠ AB',16,ORANGE,'middle',600)
    values={key:env[key].tolist() for key in ['A','B','C','by_columns','by_outer'] if key in env}
    return s.finish(**values)


def inverse(k,env):
    s=Scene(['Start with [A | I]','Apply both row operations','Extract the inverse and verify'][k],
            ['The right half starts as the identity matrix.',
             'The left half is now I. The right half contains the inverse entries.',
             'The extracted right half multiplies with A to give I.'][k])
    box=s.matrix('aug',env['aug'],210,115,43)
    s.line('divider',[210,box[1]-4],[210,box[1]+box[3]+4],ORANGE,1.6)
    s.text('left-title',167,box[1]-14,'A' if k==0 else 'I',15,BLUE,'middle')
    s.text('right-title',253,box[1]-14,'I' if k==0 else 'A⁻¹',15,ORANGE,'middle')
    if k==1:s.text('ops',210,224,'R₂ − 2R₁, then R₁ − 3R₂',16,INK,'middle')
    if k==2:
        s.matrix('identity',np.round(env['A']@env['inverse'],10),310,230,26,title='A @ inverse')
        s.text('check',130,237,'A @ A⁻¹ = I   ✓',18,GREEN,'middle',600)
    return s.finish(aug=env['aug'].tolist(),**({'inverse':env['inverse'].tolist()} if 'inverse' in env else {}))


def transpose(k,env):
    A=env['A']
    values=A if k==0 else env['R'] if k==1 else env['P']@env['R']
    s=Scene(['A is a 2 × 3 array','R = A.T is a 3 × 2 array','P @ R cycles the rows'][k],
            ['Each colored row contains three entries.',
             'The entries move from rows into columns without changing value.',
             'The new row order is 2, 3, 1. Pᵀ reverses this permutation.'][k])
    # IDs follow the entries, so transposition and row permutation move cells.
    s.matrix('entry',values,210,134,48,value_ids=True)
    for node in s.nodes:
        if node['kind']=='text' and node['id'].startswith('entry-v'):
            node['fill']=BLUE if float(node['text'])<=3 else ORANGE
    s.text('shape',210,253,f'shape = {values.shape}',17,INK,'middle',600)
    if k==2:s.text('check',210,279,'Pᵀ @ P = I   ✓',16,GREEN,'middle')
    return s.finish(A=A.tolist(),display=values.tolist(),**({'R':env['R'].tolist()} if 'R' in env else {}))


def subspace(k,env):
    s=Scene(['Two vectors on the subspace line','A linear combination stays on the line','Negative scaling leaves the quadrant'][k],
            ['u = (1, 2) and v = (−2, −4) both satisfy y = 2x.',
             'The computed vector w = 3u − 2v = (7, 14) still satisfies y = 2x.',
             'q is inside the first quadrant. −q is outside, so closure fails.'][k])
    if k<2:
        p=chart(s,bounds=(-3,8,-6,16))
        s.line('subspace-line',p(-3,-6),p(8,16),BLUE,2)
        arrow(s,'u',p,[0,0],env['u'],BLUE,'u')
        arrow(s,'v',p,[0,0],env['v'],ORANGE,'v',(-20,-8))
        if k==1:arrow(s,'w',p,[0,0],env['w'],GREEN,'w = (7, 14)',(-95,17))
    else:
        p=chart(s,bounds=(-2,2,-2,2))
        a=p(0,2);b=p(2,0)
        s.rect('quadrant',a[0],a[1],b[0]-a[0],b[1]-a[1],'#e1eae1',.5)
        arrow(s,'q',p,[0,0],env['q'],GREEN,'q')
        arrow(s,'minus-q',p,[0,0],-env['q'],RED,'−q',(-28,18))
        s.text('check',210,279,'np.all(−q ≥ 0) = False',17,RED,'middle',600)
    return s.finish(**{key:env[key].tolist() for key in ['u','v','w','q'] if key in env})


def column_space(k,env):
    s=Scene(['C(B) has one direction','The good target stays on the line','The bad target adds a new direction'][k],
            ['B has numerical rank 1. Every output lies on b₂ = 2b₁.',
             'Appending (4, 8) leaves the rank at 1, so this target is reachable.',
             'Appending (4, 7) raises the rank to 2. This target lies outside C(B).'][k])
    p=chart(s,bounds=(-.5,5,-1,10),labels=('b₁','b₂'))
    s.line('space',p(-.5,-1),p(5,10),BLUE,2.6)
    s.text('rank',60,62,f'rank(B) = {env["r"]}',15,BLUE)
    if k>=1:
        q=p(*env['good'][:,-1]);s.dot('good',q,GREEN)
        s.text('good-label',*(q+[-75,-9]),'(4, 8) ✓',15,GREEN)
    if k==2:
        q=p(*env['bad'][:,-1]);s.dot('bad',q,ORANGE)
        arrow(s,'new-direction',p,[0,0],env['bad'][:,-1],ORANGE)
        s.text('bad-label',*(q+[-84,21]),'(4, 7) ✕',15,ORANGE)
    rank_value=env['r'] if k==0 else np.linalg.matrix_rank(env['good' if k==1 else 'bad'])
    rank_label=['rank(B)','rank([B | good])','rank([B | bad])'][k]
    s.text('check',210,278,f'{rank_label} = {rank_value}',17,GREEN if k<2 else ORANGE,'middle',600)
    return s.finish(rank=int(env['r']),B=env['B'].tolist(),**{key:env[key].tolist() for key in ['good','bad'] if key in env})


PROJ=np.array([[.78,-.55,0],[-.28,-.25,.84]])
def project(v,center,scale):
    out=PROJ@np.asarray(v)
    return np.asarray(center)+scale*np.array([out[0],-out[1]])


def plane3d(s,prefix,basis,center=(210,150),scale=45,color=BLUE,offset=None,opacity=.35):
    basis=np.asarray(basis)
    offset=np.zeros(3) if offset is None else np.asarray(offset)
    def p(v):return project(v,center,scale)
    corner=[basis@np.array([a,b])+offset for a,b in [(-1,-1),(1,-1),(1,1),(-1,1)]]
    s.poly(prefix+'-surface',[p(v) for v in corner],color,color,opacity,1.2,True)
    for i,t in enumerate(np.linspace(-1,1,5)):
        s.line(prefix+f'-u{i}',p(basis@[-1,t]+offset),p(basis@[1,t]+offset),color,.8,opacity=.3)
        s.line(prefix+f'-v{i}',p(basis@[t,-1]+offset),p(basis@[t,1]+offset),color,.8,opacity=.3)
    return p


def axes3d(s,prefix,center=(210,150),scale=45,labels=('x₁','x₂','x₃')):
    for i,label in enumerate(labels):
        vec=np.eye(3)[i]*1.8
        a=project(-vec,center,scale);b=project(vec,center,scale)
        s.line(prefix+f'-axis{i}',a,b,MUTED,.9)
        s.text(prefix+f'-axis-label{i}',*(b+[4,-4]),label,12,MUTED)


def nullspace(k,env):
    s=Scene(['N spans the homogeneous nullspace','Add xₚ to reach the shifted solution plane','The shifted point still maps to b'][k],
            ['Both columns of N are sent to zero. They span the blue plane N(B).',
             'Adding xₚ shifts the blue plane. The computed x lies on the orange plane.',
             'B @ N = 0 and B @ x = (4, 8). The free parameters preserve the output.'][k])
    center=(165,154);scale=24
    axes3d(s,'input',center,scale)
    p=plane3d(s,'null',env['N'],center,scale,opacity=.35 if k==0 else .16)
    for i in range(2):
        s.line(f'n-vector{i}',p([0,0,0]),p(env['N'][:,i]),[BLUE,ORANGE][i],2.3,arrow=True)
    s.text('null-label',45,63,'N(B)',16,BLUE)
    if k>=1:
        plane3d(s,'shift',env['N'],center,scale,ORANGE,env['xp'],.22)
        s.dot('xp',p(env['xp']),ORANGE)
        s.text('xp-label',*(p(env['xp'])+[6,14]),'xₚ',14,ORANGE)
        s.dot('x',p(env['x']),GREEN,5)
        s.text('x-label',*(p(env['x'])+[8,-9]),'x',16,GREEN)
        s.text('affine-label',255,60,'xₚ + N(B)',16,ORANGE)
    if k==2:
        result=env['B']@env['x']
        s.text('check',210,280,f'B @ x = ({result[0]:g}, {result[1]:g})   ✓',17,GREEN,'middle',600)
    return s.finish(**{key:env[key].tolist() for key in ['B','N','xp','x'] if key in env})


def coordinates(k,env):
    s=Scene(['The basis and the target vector','Solve for basis coordinates','Reconstruct the same vector'][k],
            ['The columns of V form the skew basis. v is the fixed target (3, 2).',
             'solve(V, v) finds c = (1, 2). The weighted basis arrows reach v.',
             'V @ c reconstructs v, and rank(V) = 2 confirms two independent directions.'][k])
    p=chart(s,bounds=(-1,4.5,-1,3))
    arrow(s,'target',p,[0,0],env['v'],GREEN,'v = (3, 2)',(-88,-10))
    first=env['V'][:,0] if k==0 else env['V'][:,0]*env['c'][0]
    arrow(s,'b1',p,[0,0],first,BLUE,'b₁')
    start=[0,0] if k==0 else env['V'][:,0]*env['c'][0]
    end=env['V'][:,1] if k==0 else env['v']
    arrow(s,'b2',p,start,end,ORANGE)
    s.text('b2-label',180 if k==0 else 250,140,'b₂' if k==0 else '2b₂',15,ORANGE)
    if k>=1:
        s.text('coords',210,276,f'Basis coordinates c = ({env["c"][0]:g}, {env["c"][1]:g})',17,GREEN,'middle',600)
    if k==2:
        for i,a in enumerate([-1,0,1,2]):s.line(f'skew{i}',p(a-1,-1),p(a+2,2),ORANGE,.8,opacity=.25)
    return s.finish(**{key:env[key].tolist() for key in ['V','v','c'] if key in env})


def rank(k,env):
    captions=['M has rank 2. Its columns span a plane in output space.',
              'null_space(M) finds one basis vector: N(M) is a line in input space.',
              'M @ N is zero, and rank + nullity = 2 + 1 = 3 input coordinates.']
    s=Scene(['Column space: rank 2','Different input and output spaces','The rank–nullity check succeeds'][k],captions[k])
    ccenter=(210,150) if k==0 else (105,151)
    cscale=60 if k==0 else 35
    axes3d(s,'output',ccenter,cscale,('b₁','b₂','b₃'))
    plane3d(s,'column',env['M'][:,:2],ccenter,cscale)
    s.text('column-label',ccenter[0],49,'C(M): output plane',15,BLUE,'middle',600)
    s.text('rank-value',ccenter[0],255,f'rank = {env["r"]}',16,BLUE,'middle')
    if k>=1:
        axes3d(s,'null-input',(320,151),40)
        n=env['N'][:,0]
        p=lambda v:project(v,(320,151),40)
        s.line('null-line',p(-2.4*n),p(2.4*n),ORANGE,3.4)
        s.dot('origin',p([0,0,0]),ORANGE,3.5)
        s.text('null-label',320,49,'N(M): input line',15,ORANGE,'middle',600)
        s.text('nullity-value',320,255,f'nullity = {env["N"].shape[1]}',16,ORANGE,'middle')
    if k==2:s.text('check',210,284,f'{env["r"]} + {env["N"].shape[1]} = {env["M"].shape[1]}   ✓',20,GREEN,'middle',600)
    return s.finish(rank=int(env['r']),M=env['M'].tolist(),**({'N':env['N'].tolist(),'nullity':env['N'].shape[1]} if 'N' in env else {}))


BUILDERS=[solve,columns,elimination,back_substitution,products,inverse,transpose,subspace,column_space,nullspace,coordinates,rank]


def main():
    folder=Path(__file__).resolve().parent
    lessons=json.loads((folder/'walkthroughs.json').read_text(encoding='utf-8'))
    output={}
    for lesson,builder in zip(lessons,BUILDERS):
        states=[]
        for k,source in enumerate(lesson['steps']):
            env={}
            with contextlib.redirect_stdout(io.StringIO()):exec(compile(source,f'{lesson["figure"]} step {k}','exec'),env)
            state=builder(k,env)
            ids=[n['id'] for n in state['nodes']]
            assert len(ids)==len(set(ids)),f'Duplicate SVG IDs in {lesson["figure"]}'
            for node in state['nodes']:
                assert np.isfinite(node['points']).all()
            states.append(state)
        output[lesson['figure']]=dict(title=lesson['title'],slide=lesson['slide'],states=states)
    (folder/'visual_states.json').write_text(json.dumps(output,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print('Generated 36 synchronized scenes from 36 executed Python code states.')


if __name__=='__main__':main()
