from manim import *

class DisplayText(Scene):
    def construct(self):
        self.play(Write(Text("Hello World!!! It's Arka", font_size=80)))

# ########## Code WRITING ###################################################################################################################

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(Write(rendered_code, lag_ratio=0.01, run_time = 3))

# ########## Equation WRITING ###################################################################################################################


class Equation(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        # self.add(t) # Just static scene as png
        self.play(Write(t))