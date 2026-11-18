"""Regenerate the twelve illustrations used by the seminar.

    python python_examples/illustrate.py

No network, random data, or LaTeX installation is required.
"""
from pathlib import Path
import argparse
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

PAPER='#f7f5ee'
INK='#192b3a'
BLUE='#246a9c'
ORANGE='#c15b35'
GREEN='#32816b'
MUTED='#657681'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'text.color':INK,
    'axes.labelcolor':INK,'axes.edgecolor':'#b6c2c8','xtick.color':MUTED,
    'ytick.color':MUTED,'figure.facecolor':PAPER,'axes.facecolor':PAPER,
    'savefig.facecolor':PAPER,'svg.fonttype':'none'})


def figure():
    return plt.subplots(figsize=(5.2,4.3),layout='constrained')


def style(ax,xlabel='x',ylabel='y'):
    ax.spines[['top','right']].set_visible(False)
    ax.axhline(0,color='#b6c2c8',lw=.8,zorder=0)
    ax.axvline(0,color='#b6c2c8',lw=.8,zorder=0)
    ax.grid(alpha=.2)
    ax.set(xlabel=xlabel,ylabel=ylabel)


def vector(ax,start,delta,color,name=None):
    start=np.asarray(start)
    end=start+np.asarray(delta)
    ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'lw':2.5})
    if name: ax.annotate(name,end,xytext=(7,7),textcoords='offset points',color=color,fontsize=13)


def heatmap(ax,values,title=None):
    values=np.asarray(values)
    ax.imshow(np.abs(values),cmap='Blues',vmin=0,vmax=max(9,float(np.abs(values).max())),alpha=.45,aspect='equal')
    for (i,j),v in np.ndenumerate(values):
        ax.text(j,i,f'{v:g}',ha='center',va='center',color=INK,fontsize=17)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    if title: ax.set_title(title,fontsize=14,pad=12)


def save(fig,name,out):
    svg=out/f'{name}.svg'
    fig.savefig(svg,bbox_inches='tight')
    # Keep generated SVG path data friendly to Git's whitespace checks.
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    fig.savefig(out/f'{name}.png',dpi=160,bbox_inches='tight')
    plt.close(fig)


def make_all(out):
    out.mkdir(parents=True,exist_ok=True)
    x=np.linspace(-1,4,400)
    fig,ax=figure()
    ax.plot(x,2*x,color=BLUE,lw=2.5,label='2x − y = 0')
    ax.plot(x,(x+3)/2,color=ORANGE,lw=2.5,label='−x + 2y = 3')
    ax.scatter([1],[2],color=GREEN,s=65,zorder=5)
    ax.annotate('(1, 2)',(1,2),xytext=(15,-22),textcoords='offset points',color=GREEN)
    ax.set(xlim=(-.5,3),ylim=(-.5,5))
    style(ax)
    ax.legend(frameon=False,loc='upper left',fontsize=12)
    save(fig,'01-solve',out)

    fig,ax=figure()
    vector(ax,[0,0],[2,-1],BLUE,'a₁')
    vector(ax,[2,-1],[-2,4],ORANGE)
    ax.text(1.35,1.25,'2a₂',color=ORANGE)
    vector(ax,[0,0],[0,3],GREEN,'b = (0, 3)')
    ax.set(xlim=(-1.5,3),ylim=(-2,4.5),aspect='equal')
    style(ax)
    save(fig,'02-columns',out)

    fig,ax=figure()
    U=np.array([[1,2,1,4],[0,1,1,2],[0,0,9,9]])
    heatmap(ax,U,'The augmented matrix after elimination')
    ax.axvline(2.5,color=ORANGE,lw=2)
    for i in range(3): ax.add_patch(Rectangle((i-.46,i-.46),.92,.92,fill=False,ec=GREEN,lw=2.5))
    ax.set_xlabel('Three pivots, one unique solution',labelpad=15)
    save(fig,'03-elimination',out)

    fig,axs=plt.subplots(3,1,figsize=(5.2,4.3),layout='constrained')
    terms=[[0,0,9],[0,1,1],[1,2,1]]
    for ax,row,title in zip(axs,terms,['9z = 9','y + z = 2','x + 2y + z = 4']):
        ax.barh(['x','y','z'],row,color=[BLUE,ORANGE,GREEN])
        ax.set_xlim(0,10)
        ax.set_title(title,loc='left',fontsize=12,pad=2)
        ax.spines[['top','right','left']].set_visible(False)
        ax.tick_params(labelsize=10)
    save(fig,'04-back-substitution',out)

    A=np.array([[2,-1],[-1,2]])
    B=np.array([[1,2],[0,1]])
    fig,axs=plt.subplots(1,2,figsize=(5.2,4.3),layout='constrained')
    for ax,T,title in zip(axs,[A@B,B@A],['AB','BA']):
        for t in [-1,0,1]:
            p=T@np.array([[-1,1],[t,t]])
            q=T@np.array([[t,t],[-1,1]])
            ax.plot(*p,color=BLUE,alpha=.35,lw=1)
            ax.plot(*q,color=ORANGE,alpha=.35,lw=1)
        square=T@np.array([[0,1,1,0,0],[0,0,1,1,0]])
        ax.fill(*square,color=BLUE,alpha=.15)
        vector(ax,[0,0],T[:,0],BLUE)
        vector(ax,[0,0],T[:,1],ORANGE)
        ax.set(xlim=(-5.5,5.5),ylim=(-4,4),aspect='equal',title=title)
        style(ax,'','')
        ax.tick_params(labelsize=9)
    save(fig,'05-products',out)

    C=np.array([[1,3],[2,7]])
    fig,axs=plt.subplots(1,2,figsize=(5.2,4.3),layout='constrained')
    heatmap(axs[0],np.round(np.linalg.inv(C),10),'A⁻¹')
    heatmap(axs[1],np.round(C@np.linalg.inv(C),10),'AA⁻¹ = I')
    save(fig,'06-inverse',out)

    fig,axs=plt.subplots(1,2,figsize=(5.2,4.3),layout='constrained')
    rectangular=np.arange(1,7).reshape(2,3)
    heatmap(axs[0],rectangular,'A: 2 × 3')
    heatmap(axs[1],rectangular.T,'Aᵀ: 3 × 2')
    save(fig,'07-transpose',out)

    fig,ax=figure()
    xx=np.linspace(-1.4,1.4,200)
    ax.plot(xx,2*xx,color=BLUE,lw=2.5,label='y = 2x')
    ax.plot(xx,2*xx+1,color=ORANGE,lw=2,ls='--',label='y = 2x + 1')
    ax.scatter([0],[0],color=GREEN,zorder=5,s=55)
    ax.scatter([0],[1],color=ORANGE,zorder=5,s=45)
    ax.set(xlim=(-1.4,1.4),ylim=(-2.3,3.2))
    style(ax)
    ax.legend(frameon=False,loc='upper left',fontsize=12)
    save(fig,'08-subspace',out)

    fig,ax=figure()
    xx=np.linspace(-1,5,100)
    ax.plot(xx,2*xx,color=BLUE,lw=2.5,label='C(B): b₂ = 2b₁')
    ax.scatter([4],[8],s=70,color=GREEN,zorder=5)
    ax.scatter([4],[7],s=70,color=ORANGE,zorder=5)
    ax.annotate('(4, 8)',(4,8),xytext=(-55,12),textcoords='offset points',color=GREEN)
    ax.annotate('(4, 7)',(4,7),xytext=(-55,-20),textcoords='offset points',color=ORANGE)
    ax.set(xlim=(-.5,5),ylim=(-1,10))
    style(ax,'b₁','b₂')
    ax.legend(frameon=False,loc='upper left',fontsize=12)
    save(fig,'09-column-space',out)

    fig=plt.figure(figsize=(5.2,4.3),layout='constrained')
    ax=fig.add_subplot(projection='3d')
    s,t=np.meshgrid(np.linspace(-1,1,15),np.linspace(-1,1,15))
    ax.plot_surface(-2*s-3*t,s,t,color=BLUE,alpha=.3,edgecolor='#8ca9bb',lw=.3)
    for v,color in [(np.array([-2,1,0]),BLUE),(np.array([-3,0,1]),ORANGE)]:
        ax.quiver(0,0,0,*v,color=color,linewidth=2.5,arrow_length_ratio=.15)
    ax.set(xlabel='x₁',ylabel='x₂',zlabel='x₃',title='N(B): x₁ + 2x₂ + 3x₃ = 0')
    ax.view_init(elev=23,azim=-55)
    ax.set_xticks([-4,0,4])
    ax.set_yticks([-1,0,1])
    ax.set_zticks([-1,0,1])
    ax.tick_params(labelsize=9)
    save(fig,'10-nullspace',out)

    fig,ax=figure()
    for a in [-1,0,1,2,3]: ax.plot([a-1,a+2],[-1,2],color=ORANGE,alpha=.22,lw=1)
    vector(ax,[0,0],[1,0],BLUE,'b₁')
    vector(ax,[1,0],[2,2],ORANGE)
    ax.text(2.15,.8,'2b₂',color=ORANGE)
    vector(ax,[0,0],[3,2],GREEN,'v = (3, 2)')
    ax.set(xlim=(-1,4.7),ylim=(-1,3),aspect='equal')
    style(ax)
    ax.set_title('Basis coordinates: (1, 2)',fontsize=15)
    save(fig,'11-coordinates',out)

    fig=plt.figure(figsize=(5.2,4.3),layout='constrained')
    ax=fig.add_subplot(projection='3d')
    s,t=np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10))
    ax.plot_surface(s,2*s+t,t,color=BLUE,alpha=.3,edgecolor='#8ca9bb',lw=.3)
    ax.set(xlabel='b₁',ylabel='b₂',zlabel='b₃',title='C(M): a plane in output space')
    ax.view_init(elev=24,azim=-55)
    ax.set_xticks([-1,0,1])
    ax.set_yticks([-3,0,3])
    ax.set_zticks([-1,0,1])
    ax.tick_params(labelsize=9)
    save(fig,'12-rank',out)
    print(f'Generated 12 SVG figures and 12 PNG previews in {out}')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'public/python')
    make_all(parser.parse_args().output)
