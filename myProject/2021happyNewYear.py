

from manimlib.imports import *

class AnimatingMethods(Scene):
    def construct(self):
        #grid = Tex(r"福").get_
        # grid(10, 10, height=4
        # )
        # grid = Text("哈哈",font="zihun144hao-langyuanti")
        # grid = Text("牛",font="zihun43hao-guochaoshoushu")
        # grid = Text("牛",font="Kaiti SC")
        # self.add(grid)

        # # If you pass in a mobject method to the scene's "play" function,
        # # it will apply an animation interpolating between the mobject's
        # # initial state and whatever happens when you apply that method.
        # # For example, calling grid.shift(2 * LEFT) would shift it two units
        # # to the left, but the following line animates that motion.
        # self.play(grid.shift, 2 * LEFT)
        # # The same applies for any method, including those setting colors.
        # grid.set_color(['#edc686','#c66b4a','#efb110'])
        # self.play(grid.set_height, TAU - MED_SMALL_BUFF)
        # self.wait()

        # # The method Mobject.apply_complex_function lets you apply arbitrary
        # # complex functions, treating the points defining the mobject as
        # # complex numbers.
        # self.play(Rotate(        
        #     grid,
        #     radians=PI*4
        # ))
        # self.play(Rotate(        
        #     grid,
        #     radians=PI*4
        # )) 
        # self.play(grid.apply_complex_function, np.exp, run_time=5)
        
        # self.wait()
        # self.play(Rotate(        
        #     grid,
        #     radians=PI/4
        # ))
        # self.play(Rotate(        
        #     grid,
        #     radians=PI
        # ))  
        text2=TexMobject("f(z)=e^z")
        self.clear
        self.add(text2)
        self.wait(2)
        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        # self.play(
        #     grid.apply_function,
        #     lambda p: [
        #         p[0] + 0.5 * math.sin(p[1]),
        #         p[1] + 0.5 * math.sin(p[0]),
        #         p[2]
        #     ],
        #     run_time=5,
        # )
        self.wait()