'''
Author: puhongli
Date: 2021-05-12 11:36:27
LastEditTime: 2021-05-12 14:39:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /manim_sandor/myProject/for_17hertz/background.py
'''
from manimlib.imports import *
from myProject.utils.debugTeX import *
from myProject.utils.youtubedalao import *


class hertzbackground(Scene):
    CONFIG={
    'camera_config': {'background_color': BLACK},
    "side_length":1,
    "square_size":3,
    "square_color":"#d6d7ff",
    "square_opacity":0.5,
    }
    def construct(self):
        self.init_background()
    def init_background(self):
        
        
        x_max = int(FRAME_X_RADIUS+self.side_length)*self.square_size
        y_max = int(FRAME_Y_RADIUS+self.side_length)*4*self.square_size
        squares = VGroup(*[
            Square(side_length=1/self.square_size,stroke_width=0.5, fill_color=self.square_color,fill_opacity=self.square_opacity).move_to(1/self.square_size*(x * RIGHT + y * UP))
            for x in range(-x_max, x_max)
            for y in range(-y_max, y_max)
        ])
        squares.shift(RIGHT*0.5*1/self.square_size)
        self.play(
            FadeInRandom(squares)
        )
        
        self.wait(2)
