"""Nine additional scenes. Run with Manim Community 0.22.1, Cairo renderer."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from manim import *
from linear_algebra import label, heading, arrow_on, INK, MUTED, BLUE, ORANGE, GREEN, BG


def coordinate_plane(x_range, y_range, center, width=5.8, height=5.2):
    return NumberPlane(
        x_range=x_range, y_range=y_range, x_length=width, y_length=height,
        background_line_style={"stroke_color": "#3B5364", "stroke_opacity": .5, "stroke_width": 1},
        axis_config={"stroke_color": MUTED, "stroke_width": 1.5, "include_tip": False},
    ).move_to(center)


def cells(values, width=.86, height=.7, colors=None):
    group=VGroup()
    rows=len(values)
    cols=len(values[0])
    for i,row in enumerate(values):
        for j,value in enumerate(row):
            color=colors[i] if colors else INK
            group.add(label(str(value),32,color).move_to([(j-(cols-1)/2)*width,((rows-1)/2-i)*height,0]))
    return group


def brackets(group):
    left,right=group.get_left()[0]-.25,group.get_right()[0]+.25
    bottom,top=group.get_bottom()[1]-.2,group.get_top()[1]+.2
    return VGroup(
        VMobject(color=MUTED).set_points_as_corners([[left+.12,top,0],[left,top,0],[left,bottom,0],[left+.12,bottom,0]]),
        VMobject(color=MUTED).set_points_as_corners([[right-.12,top,0],[right,top,0],[right,bottom,0],[right-.12,bottom,0]]),
    )


class RowIntersection(Scene):
    def construct(self):
        heading(self,"Two equations, one intersection")
        plane=coordinate_plane([-1,4,1],[-1,5,1],[-2.7,-.3,0],5.2,5.8)
        first=plane.plot(lambda x:2*x,x_range=[-.4,2.4],color=BLUE,stroke_width=5)
        second=plane.plot(lambda x:(x+3)/2,x_range=[-.8,3.8],color=ORANGE,stroke_width=5)
        equations=VGroup(label("2x − y = 0",30,BLUE),label("−x + 2y = 3",30,ORANGE)).arrange(DOWN,buff=.5).move_to([3.15,1.6,0])
        self.add(plane)
        self.play(Create(first),FadeIn(equations[0]),run_time=1.4)
        self.play(Create(second),FadeIn(equations[1]),run_time=1.4)
        point=Dot(plane.c2p(1,2),radius=.09,color=GREEN)
        guides=VGroup(DashedLine(plane.c2p(1,0),point.get_center(),color=MUTED),DashedLine(plane.c2p(0,2),point.get_center(),color=MUTED))
        self.play(Create(guides),FadeIn(point),run_time=1)
        answer=VGroup(label("x = 1,  y = 2",31,GREEN),label("Both equations hold here",23,MUTED)).arrange(DOWN,buff=.35).move_to([3.1,-.4,0])
        self.play(FadeIn(answer),run_time=.8)
        dotlabel=label("(1, 2)",24,GREEN).next_to(point,DOWN+RIGHT,buff=.12)
        self.play(FadeIn(dotlabel),run_time=.4)
        self.wait(2)


class EliminationPivots(Scene):
    def construct(self):
        heading(self,"Elimination uncovers three pivots")
        stages=[[[1,2,1,4],[2,5,3,10],[1,0,8,9]],[[1,2,1,4],[0,1,1,2],[0,-2,7,5]],[[1,2,1,4],[0,1,1,2],[0,0,9,9]]]
        matrix=cells(stages[0],width=1.1,height=.9).move_to([-2.5,-.1,0])
        border=brackets(matrix)
        divider=Line(matrix[2].get_center()+RIGHT*.55+UP*.75,matrix[10].get_center()+RIGHT*.55+DOWN*.75,color=MUTED)
        self.add(matrix,border,divider)
        text=label("[ A  |  b ]",30).move_to([3.1,1.7,0])
        self.add(text)
        for values,operation in zip(stages[1:],["R₂ − 2R₁,  R₃ − R₁","R₃ + 2R₂"]):
            new=cells(values,width=1.1,height=.9).move_to(matrix)
            op=label(operation,28,ORANGE).move_to([3.1,.45,0])
            self.play(FadeIn(op),run_time=.6)
            self.play(Transform(matrix,new),run_time=1.6)
            self.wait(.7)
            self.play(FadeOut(op),run_time=.3)
        boxes=VGroup(*[SurroundingRectangle(matrix[k],color=GREEN,buff=.15) for k in [0,5,10]])
        result=VGroup(label("Pivots: 1, 1, 9",29,GREEN),label("9z = 9,  y + z = 2",24),label("x + 2y + z = 4",24),label("x = y = z = 1",29,GREEN)).arrange(DOWN,buff=.35).move_to([3.1,-.55,0])
        self.play(Create(boxes),FadeIn(result),run_time=1.2)
        self.wait(2.2)


class MatrixComposition(Scene):
    def construct(self):
        heading(self,"The order of two matrices changes the answer")
        planes=[coordinate_plane([-1,7,1],[-2,5,1],[x,-.3,0],5.4,4.72) for x in [-3.5,3.5]]
        self.add(*planes)
        labels=VGroup(label("ABv: B acts first",25,BLUE).move_to([-3.5,2.65,0]),label("BAv: A acts first",25,ORANGE).move_to([3.5,2.65,0]))
        self.add(labels)
        v=(1,1.5)
        arrows=[arrow_on(p,(0,0),v,GREEN) for p in planes]
        self.play(*[GrowArrow(a) for a in arrows],run_time=1)
        start=label("v = (1, 1.5)",23,MUTED).to_edge(DOWN,buff=.25)
        self.add(start)
        self.wait(.8)
        self.play(Transform(arrows[0],arrow_on(planes[0],(0,0),(4,1.5),BLUE)),Transform(arrows[1],arrow_on(planes[1],(0,0),(.5,2),ORANGE)),run_time=1.8)
        self.wait(.8)
        self.play(Transform(arrows[0],arrow_on(planes[0],(0,0),(6.5,-1),BLUE)),Transform(arrows[1],arrow_on(planes[1],(0,0),(4.5,2),ORANGE)),run_time=1.8)
        final=VGroup(label("ABv = (6.5, −1)",25,BLUE).move_to([-3.5,-3.05,0]),label("BAv = (4.5, 2)",25,ORANGE).move_to([3.5,-3.05,0]))
        self.play(FadeIn(final),run_time=.7)
        self.wait(2.4)


class GaussJordanInverse(Scene):
    def construct(self):
        heading(self,"Gauss–Jordan transforms [A | I] into [I | A⁻¹]")
        stages=[[[1,3,1,0],[2,7,0,1]],[[1,3,1,0],[0,1,-2,1]],[[1,0,7,-3],[0,1,-2,1]]]
        matrix=cells(stages[0],1.3,1).move_to([0,.3,0])
        border=brackets(matrix)
        divider=Line([0,1.3,0],[0,-.7,0],color=MUTED)
        self.add(matrix,border,divider)
        heads=VGroup(label("A",29,BLUE).move_to([-1.3,2,0]),label("I",29,ORANGE).move_to([1.3,2,0]))
        self.add(heads)
        for values,operation in zip(stages[1:],["R₂ ← R₂ − 2R₁","R₁ ← R₁ − 3R₂"]):
            op=label(operation,30,GREEN).move_to([0,-1.65,0])
            self.play(FadeIn(op),run_time=.6)
            self.play(Transform(matrix,cells(values,1.3,1).move_to(matrix)),run_time=1.5)
            self.wait(.7)
            self.play(FadeOut(op),run_time=.3)
        self.play(Transform(heads[0],label("I",29,BLUE).move_to(heads[0])),Transform(heads[1],label("A⁻¹",29,ORANGE).move_to(heads[1])),run_time=.8)
        end=label("A⁻¹ = [[7, −3], [−2, 1]]",29,GREEN).move_to([0,-2,0])
        self.play(FadeIn(end),run_time=.7)
        self.wait(2)


class MatrixTranspose(Scene):
    def construct(self):
        heading(self,"A transpose turns each row into a column")
        a=cells([[1,2,3],[4,5,6]],1,.9,[BLUE,ORANGE]).move_to([-3.4,0,0])
        self.add(a,brackets(a))
        right=cells([[1,4],[2,5],[3,6]],1,.9).move_to([3.1,0,0])
        for i,color in enumerate([BLUE,ORANGE]):
            for j in range(3): right[2*j+i].set_color(color)
        self.add(label("A: 2 × 3",29).move_to([-3.4,2.1,0]),label("Aᵀ: 3 × 2",29).move_to([3.1,2.1,0]))
        self.wait(.8)
        moved=[]
        for i in range(2):
            targets=VGroup(*[right[2*j+i] for j in range(3)])
            sources=VGroup(*[a[3*i+j].copy() for j in range(3)])
            self.add(sources)
            self.play(*[Transform(sources[j],targets[j],path_arc=PI/6) for j in range(3)],run_time=1.7)
            moved.extend(sources)
            self.wait(.5)
        self.play(Create(brackets(right)),run_time=.6)
        rule=label("Entry (i, j) moves to (j, i)",29,GREEN).move_to([0,-2.4,0])
        self.play(FadeIn(rule),run_time=.7)
        self.wait(2)


class PermutationRows(Scene):
    def construct(self):
        heading(self,"Left multiplication by P reorders rows")
        colors=[BLUE,ORANGE,GREEN]
        values=[[1,2,3],[4,5,6],[7,8,9]]
        original=cells(values,1,.85,colors).move_to([-3.4,-.2,0])
        target=cells([values[1],values[2],values[0]],1,.85,[ORANGE,GREEN,BLUE]).move_to([3.1,-.2,0])
        self.add(original,brackets(original))
        self.add(label("A",30).move_to([-3.4,2,0]),label("PA",30).move_to([3.1,2,0]))
        self.wait(.7)
        for source_row,target_row in [(1,0),(2,1),(0,2)]:
            group=VGroup(*[original[source_row*3+j].copy() for j in range(3)])
            self.add(group)
            self.play(*[Transform(group[j],target[target_row*3+j],path_arc=-PI/8) for j in range(3)],run_time=1.25)
        self.play(Create(brackets(target)),run_time=.5)
        desc=VGroup(label("New row order: 2, 3, 1",28),label("P⁻¹ = Pᵀ undoes the permutation",26,GREEN)).arrange(DOWN,buff=.35).move_to([0,-2.6,0])
        self.play(FadeIn(desc),run_time=.8)
        self.wait(2)


class ColumnSpaceSweep(Scene):
    def construct(self):
        heading(self,"All outputs stay on the column-space line")
        plane=coordinate_plane([-1,5,1],[-2,10,2],[-2.7,-.3,0],5.5,5.5)
        line=plane.plot(lambda x:2*x,x_range=[-.8,4.8],color=BLUE,stroke_width=4)
        self.add(plane)
        self.play(Create(line),run_time=1)
        coefficient=ValueTracker(0)
        dot=always_redraw(lambda:Dot(plane.c2p(coefficient.get_value(),2*coefficient.get_value()),radius=.085,color=GREEN))
        self.add(dot)
        equations=VGroup(label("B = [[1, 2, 3],",28),label("       [2, 4, 6]]",28),label("Bx = (t, 2t)",30,BLUE),label("t = x₁ + 2x₂ + 3x₃",25)).arrange(DOWN,aligned_edge=LEFT,buff=.35).move_to([3.1,1.1,0])
        self.play(FadeIn(equations),run_time=.7)
        self.play(coefficient.animate.set_value(4),run_time=1.8)
        self.play(coefficient.animate.set_value(-.7),run_time=1.8)
        self.play(coefficient.animate.set_value(4),run_time=1.8)
        possible=label("(4, 8): achievable",26,GREEN).move_to([3.1,-1.25,0])
        off=Dot(plane.c2p(4,7),radius=.085,color=ORANGE)
        impossible=label("(4, 7): outside C(B)",26,ORANGE).move_to([3.1,-2,0])
        self.play(FadeIn(possible),FadeIn(off),FadeIn(impossible),run_time=.9)
        self.wait(2)


class NullspacePlane(ThreeDScene):
    def construct(self):
        self.camera.background_color=BG
        self.set_camera_orientation(phi=65*DEGREES,theta=-45*DEGREES)
        axes=ThreeDAxes(x_range=[-4,4,2],y_range=[-2,2,1],z_range=[-2,2,1],x_length=5.8,y_length=3.8,z_length=3.8,axis_config={"include_tip":False,"stroke_color":MUTED,"stroke_width":1.5}).shift(LEFT*2)
        plane=Surface(lambda s,t:axes.c2p(-2*s-3*t,s,t),u_range=[-.7,.7],v_range=[-.7,.7],resolution=(10,10),fill_opacity=.36,checkerboard_colors=[BLUE,BLUE],stroke_color=BLUE,stroke_width=.45)
        title=label("The nullspace is a plane of inputs",34).to_edge(UP,buff=.35).to_edge(LEFT,buff=.45)
        formula=VGroup(label("x₁ + 2x₂ + 3x₃ = 0",27),label("x = s(−2, 1, 0)",25,BLUE),label("    + t(−3, 0, 1)",25,ORANGE),label("Every point gives Bx = (0, 0)",25,GREEN)).arrange(DOWN,aligned_edge=LEFT,buff=.45).move_to([3.1,0,0])
        self.add_fixed_in_frame_mobjects(title,formula)
        self.add(axes)
        self.play(Create(plane),run_time=1.6)
        dots=VGroup(*[Dot3D(axes.c2p(-2*s-3*t,s,t),radius=.065,color=GREEN) for s,t in [(.5,0),(0,.5),(-.5,0),(0,-.5),(.4,-.4)]])
        self.play(LaggedStart(*[FadeIn(d) for d in dots],lag_ratio=.2),run_time=1.6)
        self.begin_ambient_camera_rotation(rate=.06)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(1)


class BasisCoordinates(Scene):
    def construct(self):
        heading(self,"The vector stays fixed while its coordinates change")
        plane=coordinate_plane([-1,5,1],[-1,4,1],[-2.8,-.4,0],6,5)
        origin=plane.c2p(0,0)
        self.add(plane)
        target=arrow_on(plane,(0,0),(3,2),GREEN)
        target_label=label("v = (3, 2)",27,GREEN).move_to([3.3,1.8,0])
        self.play(GrowArrow(target),FadeIn(target_label),run_time=1.2)
        basis1=arrow_on(plane,(0,0),(1,0),BLUE)
        basis2=arrow_on(plane,(0,0),(1,1),ORANGE)
        self.play(GrowArrow(basis1),GrowArrow(basis2),run_time=1.2)
        coefficients=VGroup(label("b₁ = (1, 0)",27,BLUE),label("b₂ = (1, 1)",27,ORANGE)).arrange(DOWN,buff=.35).move_to([3.2,.65,0])
        self.play(FadeIn(coefficients),run_time=.6)
        skew=VGroup(*[Line(plane.c2p(a-1,-1),plane.c2p(a+2,2),color=ORANGE,stroke_opacity=.25,stroke_width=1.5) for a in [-1,0,1,2,3]])
        self.play(Create(skew),run_time=1)
        twice=arrow_on(plane,(1,0),(3,2),ORANGE)
        self.play(GrowArrow(twice),run_time=1.5)
        result=VGroup(label("v = 1b₁ + 2b₂",29,GREEN),label("Basis coordinates: (1, 2)",25)).arrange(DOWN,buff=.4).move_to([3.2,-1.3,0])
        self.play(FadeIn(result),run_time=.8)
        self.wait(2.5)
