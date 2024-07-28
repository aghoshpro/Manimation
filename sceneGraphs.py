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
        
class AreaUnderCurve(Scene):
      def construct(self):
        ax = Axes(x_range=(-5, 5), y_range=(-5, 5), axis_config={"include_numbers": True})
        curve = ax.plot(lambda x: (x+5/2)*x*(x-5/2)/2, color = RED)
        area = ax.get_area(curve, x_range=(-2.5, 2.5))
        plane = NumberPlane()
        
        self.play(Create(ax, run_time = 2), Create(curve, run_time = 3))
        self.play(FadeIn(area))
        self.wait(2)
