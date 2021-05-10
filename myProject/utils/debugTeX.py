# from @鹤翔万里

from manimlib.imports import *
import itertools

def debugTeX(self, texm):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(0.3).set_color(PURPLE)
        tex_id.move_to(j)
        self.add(tex_id)

class Axes3d(VGroup):
    CONFIG = {
        "size": 0.25,
        "tex_scale": 0.7,

    }
    def __init__(self,**kwargs):
        VGroup.__init__(self, **kwargs)
        line_color = LIGHT_GREY
        s_width = 2
        line_sc=1.5
        axes_color=LIGHT_GREY

        up_line=Line(ORIGIN,UP*line_sc,color=axes_color)
        down_line=Line(ORIGIN,DOWN*line_sc*1,color=axes_color).add_tip()
        in_line=Line(ORIGIN,IN*line_sc,color=axes_color)
        out_line=Line(ORIGIN,OUT*line_sc*1,color=axes_color).add_tip()
        right_line=Line(ORIGIN,RIGHT*line_sc*1,color=axes_color).add_tip()
        left_line=Line(ORIGIN,LEFT*line_sc*1,color=axes_color)
        up_text= TextMobject("up").move_to(up_line.get_end()).scale(self.tex_scale)
        right_text= TextMobject("right").move_to(right_line.get_end()).scale(self.tex_scale)
        left_text= TextMobject("left").move_to(left_line.get_end()).scale(self.tex_scale)
        out_text= TextMobject("out").move_to(out_line.get_end()).scale(self.tex_scale)
        in_text= TextMobject("in").move_to(in_line.get_end()).scale(self.tex_scale)
        down_text= TextMobject("down").move_to(down_line.get_end()).scale(self.tex_scale)
        


        self.add(up_line,down_line,in_line,out_line,right_line,left_line,up_text,down_text,out_text,in_text,right_text,left_text,up_text)
        # self.add(my_axes)
