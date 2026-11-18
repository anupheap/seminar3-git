"""New Manim scenes for the exact mathematics in the supplied source slides.

No LaTeX installation is needed. Numeric constants are shared with the code labs.
Render and publish: python animations/render_sources.py
"""
from pathlib import Path
import sys

from manim import *

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'python_examples'))
from source_math import (ROW_A, ROW_B, THREE_A, THREE_B, ELIM_A, ELIM_B,
                         PRODUCT_A, PRODUCT_B, INVERSE_A, PERM_A, PERM_P,
                         GRAM_R, CANVA_A)

BG = '#13222F'
INK = '#EAF0F3'
MUTED = '#A7BBC8'
BLUE = '#68B9EC'
ORANGE = '#FFA078'
GREEN = '#90D6B1'


def words(value, size=28, color=INK, width=12):
    item = Text(str(value), font='Segoe UI', font_size=size, color=color)
    if item.width > width:
        item.scale_to_fit_width(width)
    return item


def heading(scene, title, source):
    scene.camera.background_color = BG
    title = words(title, 34).to_edge(UP, buff=.35)
    note = words(source, 17, MUTED).to_edge(DOWN, buff=.22)
    scene.add(title, note)
    return title, note


def matrix(values, size=30, color=INK, augmented=False):
    values = np.asarray(values)
    if values.ndim == 1:
        values = values[:, None]
    rows, columns = values.shape
    cells = VGroup()
    for i, row in enumerate(values):
        for j, value in enumerate(row):
            text = f'{float(value):g}'
            cells.add(words(text, size, color).move_to([(j-(columns-1)/2)*.86, ((rows-1)/2-i)*.65, 0]))
    width, height = columns*.86 + .2, rows*.65 + .1
    left = VMobject(color=color).set_points_as_corners([
        [-width/2+.13, height/2, 0], [-width/2, height/2, 0],
        [-width/2, -height/2, 0], [-width/2+.13, -height/2, 0]])
    right = left.copy().rotate(PI, about_point=ORIGIN)
    group = VGroup(cells, left, right)
    if augmented:
        divider = Line([((columns-1)/2-.5)*.86, height/2, 0],
                       [((columns-1)/2-.5)*.86, -height/2, 0], color=ORANGE)
        group.add(divider)
    group.cells = cells
    return group


def grid2d(x_range, y_range):
    return NumberPlane(x_range=x_range, y_range=y_range, x_length=5.8, y_length=5,
        background_line_style={'stroke_color': '#3B5364', 'stroke_opacity': .5},
        axis_config={'stroke_color': MUTED, 'include_tip': True}).shift(LEFT*3 + DOWN*.2)


def vector(axes, start, end, color):
    return Arrow(axes.c2p(*start), axes.c2p(*end), buff=0, color=color, stroke_width=5)


class L1Rows(Scene):
    def construct(self):
        heading(self, 'Two rows, one intersection', 'Seminar.pptx · slides 5–6')
        axes = grid2d([-2, 4, 1], [-1, 5, 1])
        first = axes.plot(lambda x: 2*x, x_range=[-.4, 2.4], color=BLUE)
        second = axes.plot(lambda x: (3+x)/2, x_range=[-1.8, 3.8], color=ORANGE)
        equations = VGroup(words('2x − y = 0', 30, BLUE), words('−x + 2y = 3', 30, ORANGE)).arrange(DOWN, buff=.5).move_to(RIGHT*3+UP)
        self.play(Create(axes), FadeIn(equations), run_time=1)
        self.play(Create(first), Create(second), run_time=2)
        solution = np.linalg.solve(ROW_A, ROW_B)
        dot = Dot(axes.c2p(*solution), color=GREEN, radius=.09)
        result = words('(x, y) = (1, 2)', 32, GREEN).move_to(RIGHT*3+DOWN*.6)
        self.play(FadeIn(dot), FadeIn(result), run_time=.8)
        self.play(Indicate(dot, color=GREEN), run_time=1)
        check = VGroup(words('2(1) − 2 = 0', 25), words('−1 + 2(2) = 3', 25)).arrange(DOWN).move_to(RIGHT*3+DOWN*1.8)
        self.play(FadeIn(check))
        self.wait(2)


class L1Columns(Scene):
    def construct(self):
        heading(self, 'One column plus twice the other', 'Seminar.pptx · slides 8–11')
        axes = grid2d([-3, 3, 1], [-2, 5, 1])
        a1, a2 = np.array(ROW_A).T
        blue = vector(axes, [0, 0], a1, BLUE)
        orange = vector(axes, [0, 0], a2, ORANGE)
        labels = VGroup(words('a₁ = (2, −1)', 29, BLUE), words('a₂ = (−1, 2)', 29, ORANGE)).arrange(DOWN, buff=.5).move_to(RIGHT*3+UP*1.4)
        self.play(Create(axes), FadeIn(labels), GrowArrow(blue), GrowArrow(orange), run_time=1.4)
        self.wait(.6)
        self.play(Transform(orange, vector(axes, [0, 0], 2*a2, ORANGE)), run_time=1.5)
        self.play(Transform(orange, vector(axes, a1, a1+2*a2, ORANGE)), run_time=1.5)
        target = vector(axes, [0, 0], ROW_B, GREEN)
        result = VGroup(words('a₁ + 2a₂ = (0, 3)', 29, GREEN), words('The weights are x = 1, y = 2', 23, MUTED)).arrange(DOWN, buff=.5).move_to(RIGHT*3+DOWN)
        self.play(GrowArrow(target), FadeIn(result), run_time=1.5)
        self.wait(2)


class L1ThreePlanes(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG
        title = words('Three source planes meet at (0, 0, 1)', 32).to_edge(UP, buff=.3)
        equations = words('2x − y = 0     −x + 2y − z = −1     −3y + 4z = 4', 22).to_edge(DOWN, buff=.5)
        self.add_fixed_in_frame_mobjects(title, equations)
        axes = ThreeDAxes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-1, 3, 1], x_length=5, y_length=5, z_length=5)
        self.set_camera_orientation(phi=68*DEGREES, theta=-50*DEGREES, zoom=.8)
        self.add(axes)
        surfaces = [
            Surface(lambda u,v: axes.c2p(u, 2*u, v), u_range=[-.9,.9], v_range=[-.3,2.3], resolution=(8,8), fill_color=BLUE, fill_opacity=.38, checkerboard_colors=False),
            Surface(lambda u,v: axes.c2p(u, (u+v-1)/2, v), u_range=[-1.7,1.7], v_range=[-.3,2.3], resolution=(8,8), fill_color=ORANGE, fill_opacity=.38, checkerboard_colors=False),
            Surface(lambda u,v: axes.c2p(u, v, (4+3*v)/4), u_range=[-1.7,1.7], v_range=[-1.7,1.7], resolution=(8,8), fill_color=GREEN, fill_opacity=.38, checkerboard_colors=False),
        ]
        for surface in surfaces:
            self.play(FadeIn(surface), run_time=.8)
        solution = np.linalg.solve(THREE_A, THREE_B)
        self.play(FadeIn(Dot3D(axes.c2p(*solution), color=WHITE, radius=.1)))
        self.begin_ambient_camera_rotation(rate=.15)
        self.wait(4)
        self.stop_ambient_camera_rotation()


class L2Elimination(Scene):
    def construct(self):
        heading(self, 'Elimination with the original matrix', 'Seminar.pptx · slides 21–24')
        aug = np.column_stack((ELIM_A, ELIM_B)).astype(float)
        display = matrix(aug, augmented=True).scale(1.3).move_to(UP*.5)
        self.play(FadeIn(display))
        operation = words('Start with [A | b]', 26, MUTED).move_to(DOWN*1.6)
        self.play(FadeIn(operation))
        for row, multiplier, pivot, text in [(1,3,0,'R₂ ← R₂ − 3R₁'), (2,2,1,'R₃ ← R₃ − 2R₂')]:
            aug[row] -= multiplier*aug[pivot]
            self.play(Transform(operation, words(text, 28, ORANGE).move_to(operation)), run_time=.5)
            self.play(Transform(display, matrix(aug, augmented=True).scale(1.3).move_to(display)), run_time=1.4)
            self.wait(.7)
        self.play(FadeIn(words('Pivots: 1, 2, 5       (x, y, z) = (2, 1, −2)', 28, GREEN).move_to(DOWN*2.5)))
        self.wait(2)


class L3Products(Scene):
    def construct(self):
        heading(self, 'The four views agree on AB', 'Presentation2.pptx · slides 3–6 and 10')
        A, B = np.array(PRODUCT_A), np.array(PRODUCT_B)
        left, middle, right = [matrix(data).move_to([x,1,0]) for data,x in [(A,-4.4),(B,-.2),(A@B,4.2)]]
        self.play(FadeIn(left), FadeIn(middle), FadeIn(words('×', 38).move_to([-2.3,1,0])), FadeIn(words('=', 38).move_to([2,1,0])))
        dot = words('c₁₁ = 1·5 + 2·7 = 19', 30, BLUE).move_to(DOWN*.6)
        self.play(FadeIn(dot), run_time=.6)
        self.play(FadeIn(right), run_time=1)
        self.wait(.5)
        outer1 = matrix(np.outer(A[:,0], B[0,:]), size=25).move_to([-2.5,-2,0])
        outer2 = matrix(np.outer(A[:,1], B[1,:]), size=25).move_to([1,-2,0])
        self.play(FadeIn(outer1), FadeIn(words('+', 32).move_to([- .75,-2,0])), FadeIn(outer2))
        self.play(Transform(dot, words('Columns × rows: add the two outer products', 26, GREEN).move_to(dot)))
        self.wait(2.5)


class L3Inverse(Scene):
    def construct(self):
        heading(self, 'Gauss–Jordan on the source matrix', 'Presentation2.pptx · slides 8–11')
        aug = np.column_stack((INVERSE_A, np.eye(2))).astype(float)
        display = matrix(aug).scale(1.3).move_to(UP*.5)
        operation = words('[A | I]', 30, MUTED).move_to(DOWN*1.1)
        self.play(FadeIn(display), FadeIn(operation))
        states = []
        aug[1] -= 2*aug[0]; states.append((aug.copy(), 'R₂ ← R₂ − 2R₁'))
        aug[1] *= -1; states.append((aug.copy(), 'R₂ ← −R₂'))
        aug[0] -= 3*aug[1]; states.append((aug.copy(), 'R₁ ← R₁ − 3R₂'))
        for values, text in states:
            self.play(Transform(operation, words(text, 28, ORANGE).move_to(operation)), run_time=.4)
            self.play(Transform(display, matrix(values).scale(1.3).move_to(display)), run_time=1.1)
            self.wait(.4)
        result = words('A⁻¹ = [−5, 3; 2, −1]       A A⁻¹ = I', 28, GREEN).move_to(DOWN*2.2)
        self.play(FadeIn(result))
        self.wait(2)


class L5Permutation(Scene):
    def construct(self):
        heading(self, 'Swap rows before elimination', 'Lecture5.pptx · slides 3–4')
        A, P = np.array(PERM_A), np.array(PERM_P)
        display = matrix(A).scale(1.2).move_to(UP*.4)
        self.play(FadeIn(display))
        label = words('The first pivot is zero', 28, ORANGE).move_to(DOWN*1.5)
        self.play(FadeIn(label))
        self.wait(.8)
        self.play(Transform(display, matrix(P@A).scale(1.2).move_to(display)), Transform(label, words('P swaps R₁ and R₂', 28, BLUE).move_to(label)), run_time=1.5)
        U = (P@A).copy(); U[2] -= 2*U[0]; U[2] -= 2*U[1]
        self.wait(.8)
        self.play(Transform(display, matrix(U).scale(1.2).move_to(display)), Transform(label, words('R₃ − 2R₁, then R₃ − 2R₂', 27, ORANGE).move_to(label)), run_time=1.5)
        self.play(FadeIn(words('PA = LU     L = [1,0,0; 0,1,0; 2,2,1]', 26, GREEN).move_to(DOWN*2.5)))
        self.wait(2)


class L5Symmetry(Scene):
    def construct(self):
        heading(self, 'RᵀR is symmetric', 'Lecture5.pptx · slides 6–7')
        R = np.array(GRAM_R)
        left = matrix(R).move_to([-4.3,.8,0])
        transposed = matrix(R.T).move_to([-.7,.8,0])
        product = matrix(R.T@R, color=GREEN).move_to([3.8,.8,0])
        self.play(FadeIn(left), FadeIn(words('R',28).move_to([-4.3,2.3,0])))
        self.play(TransformFromCopy(left, transposed), FadeIn(words('Rᵀ',28).move_to([-.7,2.3,0])), run_time=1.5)
        self.wait(.5)
        self.play(FadeIn(product), FadeIn(words('RᵀR',28,GREEN).move_to([3.8,2.3,0])), run_time=1)
        self.play(Indicate(product.cells[1], color=ORANGE), Indicate(product.cells[2], color=ORANGE))
        self.play(FadeIn(words('Both off-diagonal entries are 2', 28, GREEN).move_to(DOWN*1.5)))
        self.play(FadeIn(words('(RᵀR)ᵀ = RᵀR', 28).move_to(DOWN*2.3)))
        self.wait(2)


class L5ColumnSpace(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG
        title = words('Column space of the source R',32).to_edge(UP,buff=.3)
        bottom = words('a₁ = (1, 3, 0)     a₂ = (2, 0, 4)     a₁ + 2a₂ = (5, 3, 8)',22).to_edge(DOWN,buff=.4)
        self.add_fixed_in_frame_mobjects(title,bottom)
        axes = ThreeDAxes(x_range=[-2,6,2],y_range=[-2,6,2],z_range=[-2,10,2],x_length=5,y_length=5,z_length=5)
        self.set_camera_orientation(phi=65*DEGREES,theta=-50*DEGREES,zoom=.8)
        self.add(axes)
        a,b = np.array(GRAM_R).T
        surface = Surface(lambda u,v: axes.c2p(*(u*a+v*b)),u_range=[-.5,1.3],v_range=[-.5,2.3],resolution=(6,6),fill_color=BLUE,fill_opacity=.25,checkerboard_colors=False)
        self.play(FadeIn(surface))
        for end,color in [(a,BLUE),(b,ORANGE),(a+2*b,GREEN)]:
            self.play(Create(Line3D(axes.c2p(0,0,0),axes.c2p(*end),color=color,thickness=.025)),run_time=1)
        self.begin_ambient_camera_rotation(rate=.12)
        self.wait(3)
        self.stop_ambient_camera_rotation()


class L9Dependence(ThreeDScene):
    def construct(self):
        self.camera.background_color = BG
        title = words('The Canva vectors are dependent',32).to_edge(UP,buff=.3)
        bottom = words('(3, 2, 5) + (4, 7, 2) = (7, 9, 7)',28,GREEN).to_edge(DOWN,buff=.4)
        self.add_fixed_in_frame_mobjects(title,bottom)
        axes = ThreeDAxes(x_range=[0,10,2],y_range=[0,10,2],z_range=[0,10,2],x_length=4,y_length=4,z_length=4)
        self.set_camera_orientation(phi=65*DEGREES,theta=-55*DEGREES,zoom=.85)
        self.add(axes)
        a,b,c = np.array(CANVA_A).T
        origin = axes.c2p(0,0,0)
        first = Line3D(origin,axes.c2p(*a),color=BLUE,thickness=.03)
        second = Line3D(origin,axes.c2p(*b),color=ORANGE,thickness=.03)
        self.play(Create(first),Create(second),run_time=1.5)
        self.play(Transform(second,Line3D(axes.c2p(*a),axes.c2p(*c),color=ORANGE,thickness=.03)),run_time=1.6)
        self.play(Create(Line3D(origin,axes.c2p(*c),color=GREEN,thickness=.03)),run_time=1.2)
        self.begin_ambient_camera_rotation(rate=.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()


class L9Basis(Scene):
    def construct(self):
        heading(self, 'Two pivots, one free column', 'Canva Lecture 9 · pages 14–24')
        source = matrix(CANVA_A).scale(1.2).move_to(UP*.5)
        self.play(FadeIn(source))
        self.wait(.8)
        reduced = matrix([[1,0,1],[0,1,1],[0,0,0]]).scale(1.2).move_to(source)
        self.play(Transform(source,reduced),run_time=2)
        result = VGroup(words('Pivot columns: 1 and 2',28,BLUE),
                        words('Take those columns from the original A',23,MUTED),
                        words('dim C(A) = 2     dim N(A) = 1',29,GREEN)).arrange(DOWN,buff=.3).move_to(DOWN*2)
        self.play(FadeIn(result),run_time=1)
        self.wait(3)
