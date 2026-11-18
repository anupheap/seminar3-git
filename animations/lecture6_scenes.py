"""New Lecture 6 geometry. Click cues: 0, 2.2, 4.4, 7 seconds."""
from manim import *
import numpy as np

config.background_color = '#050607'
BLUE6 = '#58C4DD'
GREEN6 = '#83C167'
GOLD6 = '#F0AC5F'

class SubspaceClosure(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=58*DEGREES, theta=-65*DEGREES, zoom=.9)
        axes=ThreeDAxes(x_range=[-3,3,1],y_range=[-3,3,1],z_range=[-1,2,1],x_length=7,y_length=7,z_length=3,
                       axis_config={'color':'#727C87','stroke_width':1.5,'include_ticks':False})
        grid=VGroup()
        for k in range(-3,4):
            grid.add(Line(axes.c2p(k,-3,0),axes.c2p(k,3,0),color=BLUE6,stroke_width=1,stroke_opacity=.25))
            grid.add(Line(axes.c2p(-3,k,0),axes.c2p(3,k,0),color=BLUE6,stroke_width=1,stroke_opacity=.25))
        origin=axes.c2p(0,0,0)
        u=np.array([1.,1.,0.]);v=np.array([1.,-.5,0.])
        arrow=lambda point,color:Arrow3D(origin,axes.c2p(*point),color=color,thickness=.018,height=.20,base_radius=.07)
        au=arrow(u,BLUE6);av=arrow(v,GREEN6)
        self.add(axes,grid,Dot3D(origin,radius=.045,color=WHITE),au,av)
        self.wait(2.2)
        guide=DashedLine(axes.c2p(*u),axes.c2p(*(u+v)),color=GREEN6,stroke_width=2)
        total=arrow(u+v,GOLD6)
        self.play(Create(guide),FadeIn(total),run_time=1.2)
        self.wait(1.)
        scaled=arrow(-2*u,'#FC6255')
        self.play(FadeIn(scaled),run_time=1.2)
        self.wait(1.4)
