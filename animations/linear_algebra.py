"""Original Manim visualizations for the selected MIT 18.06 seminar.

Render with Manim Community 0.22.1, without a LaTeX dependency:
    python -m manim -qm --fps 30 animations/linear_algebra.py \
        ColumnCombination EliminationGeometry DependenceAndBasis
"""

from manim import *

INK = "#EAF0F3"
MUTED = "#A7BBC8"
BLUE = "#68B9EC"
ORANGE = "#FFA078"
GREEN = "#90D6B1"
BG = "#13222F"


def label(text, size=27, color=INK):
    return Text(text, font="Segoe UI", font_size=size, color=color)


def heading(scene, text):
    scene.camera.background_color = BG
    title = label(text, 34).to_edge(UP, buff=.35).to_edge(LEFT, buff=.45)
    scene.add(title)


def plane_for_vectors():
    plane = NumberPlane(
        x_range=[-3, 4, 1], y_range=[-2, 5, 1],
        x_length=6.15, y_length=6.15,
        background_line_style={"stroke_color": "#3B5364", "stroke_opacity": .5, "stroke_width": 1},
        axis_config={"stroke_color": MUTED, "stroke_width": 1.6, "include_tip": False},
    ).shift(LEFT * 2.9 + DOWN * .25)
    return plane


def arrow_on(plane, start, end, color):
    return Arrow(plane.c2p(*start), plane.c2p(*end), buff=0, color=color,
                 stroke_width=6, max_tip_length_to_length_ratio=.12)


class ColumnCombination(Scene):
    def construct(self):
        heading(self, "A linear combination of columns")
        plane = plane_for_vectors()
        self.add(plane)
        a1 = arrow_on(plane, (0, 0), (2, -1), BLUE)
        a2 = arrow_on(plane, (0, 0), (-1, 2), ORANGE)
        labels = VGroup(
            label("a₁ = (2, −1)", 29, BLUE),
            label("a₂ = (−1, 2)", 29, ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=.42).move_to([3.25, 1.65, 0])
        self.play(GrowArrow(a1), GrowArrow(a2), FadeIn(labels), run_time=1.8)
        self.wait(1.2)
        step = label("Scale the second column", 25).move_to([3.2, .1, 0])
        doubled = arrow_on(plane, (0, 0), (-2, 4), ORANGE)
        self.play(Transform(a2, doubled), FadeIn(step), run_time=2)
        scaled_text = label("2a₂ = (−2, 4)", 29, ORANGE).move_to([3.15, -.65, 0])
        self.play(FadeIn(scaled_text), run_time=.7)
        self.wait(1)
        ghost = a2.copy().set_opacity(.22)
        self.add(ghost)
        translated = arrow_on(plane, (2, -1), (0, 3), ORANGE)
        next_step = label("Add tip to tail", 25).move_to(step)
        self.play(Transform(a2, translated), Transform(step, next_step), run_time=2.2)
        resultant = arrow_on(plane, (0, 0), (0, 3), GREEN)
        result = label("a₁ + 2a₂ = (0, 3)", 28, GREEN).move_to([3.15, -1.65, 0])
        self.play(GrowArrow(resultant), FadeIn(result), run_time=1.5)
        target = label("b", 26, GREEN).next_to(plane.c2p(0, 3), LEFT, buff=.18)
        self.play(FadeIn(target), run_time=.5)
        self.wait(3)


class EliminationGeometry(Scene):
    def construct(self):
        heading(self, "Elimination keeps the solution fixed")
        axes = NumberPlane(
            x_range=[-1, 4, 1], y_range=[-1, 5, 1],
            x_length=5.4, y_length=5.9,
            background_line_style={"stroke_color": "#3B5364", "stroke_opacity": .5, "stroke_width": 1},
            axis_config={"stroke_color": MUTED, "stroke_width": 1.6, "include_tip": False},
        ).shift(LEFT * 3 + DOWN * .35)
        first = axes.plot(lambda x: 2*x, x_range=[-.4, 2.4], color=BLUE, stroke_width=5)
        t = ValueTracker(0)
        second = always_redraw(lambda: axes.plot(
            lambda x: (3 + (1-2*t.get_value())*x)/(2-t.get_value()),
            x_range=[-.8, 3.8], color=ORANGE, stroke_width=5,
        ))
        point = Dot(axes.c2p(1, 2), radius=.085, color=GREEN)
        point_label = label("(1, 2)", 24, GREEN).next_to(point, DOWN+RIGHT, buff=.12)
        before = VGroup(
            label("2x − y = 0", 30, BLUE),
            label("−x + 2y = 3", 30, ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=.45).move_to([3, 1.7, 0])
        self.play(Create(axes), Create(first), Create(second), FadeIn(before), run_time=2)
        self.play(FadeIn(point), FadeIn(point_label), run_time=.7)
        self.wait(1)
        operation = label("Row 2 + ½ Row 1", 28).move_to([3, .1, 0])
        self.play(FadeIn(operation), run_time=.7)
        self.play(t.animate.set_value(.5), run_time=4, rate_func=smooth)
        after = label("3y/2 = 3", 30, ORANGE).move_to(before[1]).align_to(before[1], LEFT)
        self.play(Transform(before[1], after), run_time=1)
        solution = VGroup(
            label("y = 2", 29, GREEN),
            label("x = 1", 29, GREEN),
            label("The intersection stays put", 22, MUTED),
        ).arrange(DOWN, buff=.4).move_to([3, -1.65, 0])
        self.play(FadeIn(solution), run_time=1)
        self.wait(3)


class DependenceAndBasis(Scene):
    def construct(self):
        heading(self, "Dependence and a basis of the plane")
        axes = NumberPlane(
            x_range=[-1, 4, 1], y_range=[-1, 3, 1],
            x_length=6, y_length=4.8,
            background_line_style={"stroke_color": "#3B5364", "stroke_opacity": .5, "stroke_width": 1},
            axis_config={"stroke_color": MUTED, "stroke_width": 1.6, "include_tip": False},
        ).shift(LEFT * 2.9 + DOWN * .3)
        self.add(axes)
        v1 = arrow_on(axes, (0, 0), (1, 0), BLUE)
        v2 = arrow_on(axes, (0, 0), (1, 1), ORANGE)
        vectors = VGroup(
            label("v₁ = (1, 0)", 28, BLUE),
            label("v₂ = (1, 1)", 28, ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=.4).move_to([3.1, 1.8, 0])
        self.play(GrowArrow(v1), GrowArrow(v2), FadeIn(vectors), run_time=1.8)
        self.wait(.8)
        shifted = arrow_on(axes, (1, 0), (2, 1), ORANGE).set_opacity(.7)
        self.play(TransformFromCopy(v2, shifted), run_time=1.5)
        v3 = arrow_on(axes, (0, 0), (2, 1), GREEN)
        relation = label("v₃ = v₁ + v₂", 29, GREEN).move_to([3.1, .35, 0])
        self.play(GrowArrow(v3), FadeIn(relation), run_time=1.5)
        zero = label("v₁ + v₂ − v₃ = 0", 28, GREEN).move_to([3.1, -.5, 0])
        self.play(FadeIn(zero), run_time=.7)
        self.wait(1.5)
        self.play(FadeOut(v3), FadeOut(shifted), run_time=1)
        dots = VGroup(*[
            Dot(axes.c2p(a+b, b), radius=.035, color=BLUE).set_opacity(.65)
            for a in [-1, 0, 1, 2] for b in [-.75, 0, .75, 1.5]
            if -1 <= a+b <= 3.5
        ])
        basis = VGroup(
            label("{v₁, v₂} is a basis of R²", 25),
            label("Two independent directions", 22, MUTED),
        ).arrange(DOWN, buff=.3).move_to([3.1, -1.8, 0])
        self.play(LaggedStart(*[FadeIn(dot) for dot in dots], lag_ratio=.05), FadeIn(basis), run_time=2)
        self.wait(3)
