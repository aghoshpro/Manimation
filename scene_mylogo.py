from manim import *

class MyName(Scene):
        def construct(self):
            # Objects with properties
            nameTXT = Write(Text("Arka", font_size=80));

            # latex = Write(MathTex(r"\mathbb{ARKA}", color=WHITE).scale(3).shift(2.25 * LEFT + 1.5 * UP))
            firstNameTEX = MathTex(r"\mathbb{ARKA}", color=WHITE)
            lastNameTEX = MathTex(r"\mathbb{GHOSH}", color=WHITE)

            circle = Circle(radius=2, color=GREEN_A, fill_opacity=0.5)  # create a circle
            square = Square(side_length=4, color=BLUE)  # create a square

            # Actions of Objects
            square.rotate(PI / 4)  # rotate a certain amount
            firstNameTEX.scale(3).shift(2.25 * LEFT + 1.5 * UP)
            lastNameTEX.scale(3).shift(2.25 * RIGHT + 1.5 * DOWN)
            
            # Animation starts here in order 
            self.play(Write(firstNameTEX))
            self.play(Create(square))  # animate the creation of the square
            self.play(Transform(square, circle))  # interpolate the square into the circle
            self.play(Write(lastNameTEX))
            self.play(FadeOut(square))  # fade out animation


class MyLogo(Scene):
    def construct(self):
        # Objects with properties
        text = Write(Text("Arka", font_size=80));

        # latex = Write(MathTex(r"\mathbb{ARKA}", color=WHITE).scale(3).shift(2.25 * LEFT + 1.5 * UP))
        latex = MathTex(r"\mathbb{ARKA}", color=WHITE)

        circle = Circle(radius=2, color=GREEN_A, fill_opacity=0.5)  # create a circle
        square = Square(side_length=4, color=BLUE)  # create a square

        # Actions of Objects
        square.rotate(PI / 4)  # rotate a certain amount
        latex.scale(3)
        
        # Animation starts here in order)
        # self.play(Write(latex))
        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SolarSystem(Scene):
    def construct(self):
        text = Write(Text("A", font_size=90, color=GOLD_A));
        text1 = Write(Text("R", font_size=90, color=GOLD_B).shift(RIGHT * 1));
        text2 = Write(Text("K", font_size=90, color=GOLD_C).shift(RIGHT * 2));
        text3 = Write(Text("A", font_size=90, color=GOLD_D).shift(RIGHT * 3));
        
        circle1= Circle(radius=1, color=BLUE)
        circle2= Circle(radius=2, color=BLUE_B)
        circle3= Circle(radius=3, color=BLUE_D)

        dot = Dot()
        dot1 = Dot()
        dot2 = Dot()
        dot3 = Dot()
        self.add(dot)
        self.play(FadeOut(dot)) 
        self.play(text)

        self.play(GrowFromCenter(circle1))
        self.play(MoveAlongPath(dot1, circle1), run_time=1, rate_func=linear)
        self.play(FadeOut(dot1)) 
        self.play(text1)

        self.play(GrowFromCenter(circle2))
        self.play(MoveAlongPath(dot2, circle2), run_time=2, rate_func=linear)
        self.play(FadeOut(dot2)) 
        self.play(text2)

        self.play(GrowFromCenter(circle3))
        self.play(MoveAlongPath(dot3, circle3), run_time=3, rate_func=linear)
        self.play(FadeOut(dot3)) 
        self.play(text3)
        self.play(Write(Text("A", font_size=90, color=RED)))
