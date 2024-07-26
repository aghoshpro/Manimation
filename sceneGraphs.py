from manim import *

class NumberLine(Scene):
    def construct(self):
        axes = Axes(x_range=[-2, 10, 1],
                    y_range =[-2, 8, 1],
                    tips=False,
            axis_config={"include_numbers": True})
        
        # a dot with respect to the axes
        dot_axes = Dot(axes.coords_to_point(2, 2), color=GREEN)
        lines = axes.get_lines_to_point(axes.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2,2,0), color=RED)

        self.play(Write(axes, lag_ratio=0.01, run_time=2))
        