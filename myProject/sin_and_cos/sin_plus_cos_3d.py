from manimlib.imports import *

class sin_cos_in_axis(SpecialThreeDScene):

    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi":66 * DEGREES,
        # "phi": 66 * DEGREES,
        "theta": 20 * DEGREES,
        # "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': BLACK},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }
        MYORIGIN=ORIGIN+2*RIGHT+UP
        axes_origin = ORIGIN
        axes_scale = 1.2
        # axes_scale = 1.2
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 1.5
        # cp_scale = 2
        #加了个复杂平面B
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        #添加坐标
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        l = axes_scale

        # r = cp.n2p(1)[0]/2
        r = cp.n2p(1)[0]/2
        print("r:",r,"n2p(1):",cp.n2p(-2))

        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-1.5, 0, 0)+3*RIGHT)
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=BLACK, stroke_width=6)
        line_r2 = Line(circle.get_center(), circle.get_center() + UP * r*0.7, color=ORANGE, stroke_width=6,plot_depth=1).add_tip()
        # line_tip=line_r2.get_tip().rotate(90*DEGREES)
        # line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6)
        dot = Dot3d(color=RED, size=0.18,plot_depth=1).add_updater(lambda d: d.move_to(line_r.get_end()))
        

        cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))

        w = TAU/2
        #这里的shift 是到开始的地方
        color_sin=YELLOW
        color_cos=GREEN
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=WHITE, stroke_width=4).shift(cp.n2p(-1.5)+5*LEFT)
        self.cos_t = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), 0]), t_min=0, t_max=8,
                                      color=color_cos, stroke_width=44).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+3.45))
        self.sin_t = ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=color_sin, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+5))
        dot2 = Dot3d(color=color_cos, size=0.18,plot_depth=1).add_updater(lambda d: d.move_to(self.cos_t.get_end()))
        dot3 = Dot3d(color=color_sin, size=0.18,plot_depth=1).add_updater(lambda d: d.move_to(self.sin_t.get_end()))
        self.add(dot2,dot3)
        
        cube_g = VGroup()
        A = axes.c2p(-2, -0.5, 0.5)
        B = axes.c2p(-2, 0.5, 0.5)
        C = axes.c2p(-2, 0.5, -0.5)
        D = axes.c2p(-2, -0.5, -0.5)
        E = axes.c2p(2, -0.5, 0.5)
        F = axes.c2p(2, 0.5, 0.5)
        G = axes.c2p(2, 0.5, -0.5)
        H = axes.c2p(2, -0.5, -0.5)
        line_color = LIGHT_GREY
        s_width = 2
        line_sc=4.5
        axes_color=LIGHT_GREY
        up_line=Line(ORIGIN,UP*line_sc,color=axes_color)
        down_line=Line(ORIGIN,DOWN*line_sc*0.25,color=axes_color).add_tip()
        down_tip=down_line.get_tip().rotate(0*DEGREES,axis=LEFT)
        in_line=Line(ORIGIN,IN*line_sc,color=axes_color)
        out_line=Line(ORIGIN,OUT*line_sc*1.25,color=axes_color).add_tip()
        tip=out_line.get_tip().rotate(90*DEGREES,axis=UP).shift(0.2*LEFT)
        right_line=Line(ORIGIN,RIGHT*line_sc*0.5,color=axes_color).add_tip()
        # right_tip=right_line.get_tip().rotate(-180*DEGREES)
        left_line=Line(ORIGIN,LEFT*line_sc*0.5,color=axes_color)
        left_line_dash=DashedLine(LEFT*line_sc*0.5,LEFT*line_sc*3,color=axes_color,positive_space_ratio=0.3,dash_length=0.2)


        my_axes=VGroup(up_line,down_line,in_line,out_line,right_line,left_line,left_line_dash)

        AB = Line(A, B, color=line_color, stroke_width=s_width)
        BC = DashedLine(C, B, color=line_color, stroke_width=s_width)
        CD = DashedLine(C, D, color=line_color, stroke_width=s_width)
        DA = Line(A, D, color=line_color, stroke_width=s_width)

        AE = Line(A, E, color=line_color, stroke_width=s_width)
        BF = Line(F, B, color=line_color, stroke_width=s_width)
        CG = DashedLine(C, G, color=line_color, stroke_width=s_width)
        DH = Line(H, D, color=line_color, stroke_width=s_width)

        EF = Line(E, F, color=line_color, stroke_width=s_width)
        FG = Line(F, G, color=line_color, stroke_width=s_width)
        GH = Line(G, H, color=line_color, stroke_width=s_width)
        HE = Line(H, E, color=line_color, stroke_width=s_width)

        cube_g.add(AB, BC, CD, DA, AE, BF, CG, DH, EF, FG, GH, HE)

        y_dash = VGroup(DashedLine((A+D)/2, (E+H)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            y_dash.add(DashedLine(A + i * (E-A)/16, D + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A+B)/2, (E+F)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            x_dash.add(DashedLine(A + i * (E-A)/16, B + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)

        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}

        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_sint = TexMobject('\\mathbf{\\sin{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_cost = TexMobject('\\mathbf{\\cos{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*0.4 + LEFT * 0.2)
        text_sint.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(DOWN*r*(1+2))
        text_cost.scale(1.2).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*r*(1+1.45)+LEFT*0.75*r+DOWN*0.4*r)

        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube/2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI/2, RIGHT).next_to(l_x, UP*1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI/2, RIGHT).next_to(l_y, OUT*0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI/2, RIGHT).next_to(l_t, RIGHT*0.5)
        # navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(cp.n2p(-0.6-3.2j))
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t).move_to(cp.n2p(-0.6-3.2j))

        ## rotate update ##
        # curve_3d.shift
        rotate_group = VGroup(curve_3d, line_r, dot,line_r2)
        self.varphi = 0
        def rotate_all(r, dt):
            r.rotate(2.5*DEGREES, RIGHT, about_point=ORIGIN)
            # r.rotate(2.5*DEGREES, RIGHT, about_point=r.get_center())
            self.varphi += 2.5*DEGREES
            # self.cos_t.become(ParametricFunction(lambda t: np.array([t * r, r * np.cos(w * t + self.varphi), 0]), t_min=0, t_max=8,
            #                            color=GREEN, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
            # self.sin_t.become(ParametricFunction(lambda t: np.array([t * r, 0, r * np.sin(w * t + self.varphi)]), t_min=0, t_max=8,
            #                            color=PINK, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))
        self.cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + self.varphi), 0]), t_min=-0.0001, t_max=8,
                                      color=color_cos, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((IN+1.6*LEFT+0.1*DOWN+0.18*UP)*r*(1+1.45))))
        self.sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + self.varphi)]), t_min=-0.0001, t_max=8,
                                      color=color_sin, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((0.95*DOWN+LEFT+0.6*OUT)*r*(1+2))))


        dot2.add_updater(lambda d: d.move_to(self.cos_t.get_end()))
        dot3.add_updater(lambda d: d.move_to(self.sin_t.get_end()))
        # cos_line=Line(self.cos_t.get_end(),dot.get_center(),color=ORANGE).add_updater(lambda c:c.become(Line(self.cos_t.get_end(),dot.get_center(),color=ORANGE)))
        cos_line=DashedLine(self.cos_t.get_end(),dot.get_center(),color=line_color, stroke_width=s_width).add_updater(lambda c:c.become(DashedLine(self.cos_t.get_end(),dot.get_center(),color=line_color, stroke_width=s_width)))
        # sin_line=Line(self.sin_t.get_end(),dot.get_center(),color=ORANGE).add_updater(lambda c:c.become(Line(self.cos_t.get_end(),dot.get_center(),color=ORANGE)))
        sin_line=DashedLine(self.sin_t.get_end(),dot.get_center(),color=line_color, stroke_width=s_width).add_updater(lambda c:c.become(DashedLine(self.sin_t.get_end(),dot.get_center(),color=line_color, stroke_width=s_width)))
        
        
        ## animation ##
        axes.shift(curve_3d.get_center()+IN+5*RIGHT)

        # self.add(cp, axes)
        # self.add(axes)
        # circle.shift(axes.c2p(4, 0, 0))
        #self.add(curve_3d, cube_g, circle, line_r, dot, navi_group, yt, xt, self.sin_t, self.cos_t, text_sint, text_cost, text_eiwt)
        self.add(self.sin_t, self.cos_t)
        # self.add(text_sint, text_cost, text_eiwt)
        # yt.shift(DOWN*r*2)

        # xt.shift(OUT*r*1.45)

        cos_sin_lines=VGroup(cos_line,sin_line)
        my_axes.shift(2*RIGHT+2*DOWN+2*IN)
        self.add(my_axes)
        self.play(
            ShowCreation(cos_sin_lines)
        )
        self.play(
            FocusOn(dot), 
            FadeIn(line_r2),
            FadeIn(dot)
            
        )
        self.wait()
        self.add(rotate_group)
        rotate_group.add_updater(rotate_all)
        # self.add(cos_line,sin_line)
        self.wait(15)

class show_cubes(SpecialThreeDScene):
    CONFIG = {
    # "background_image": 'my_projects\\resource\\png_files\\screen_test.png',
    "default_angled_camera_position": {
        "phi": 66 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 0.0 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': BLACK},
    "three_d_axes_config": {
        "num_axis_pieces": 1,
        "number_line_config": {
            'color': BLACK,
            "unit_size": 2,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [0, 1, 2],
            "stroke_width": 2,
            }
        },
    }

    def construct(self):

        axis_config={
            "stroke_color": BLACK,
            "stroke_width": 2,
            "include_ticks": False,
            "include_tip": False,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
            'decimal_number_config': {'color': BLACK},
        }

        axes_origin = ORIGIN
        axes_scale = 1.2
        axes = self.get_axes().scale(axes_scale, about_point=ORIGIN).shift(axes_origin)

        self.set_camera_to_default_position()

        cp_scale = 2
        cp = ComplexPlane(axis_config=axis_config).scale(cp_scale*axes_scale, about_point=ORIGIN).shift(axes_origin)
        cp.add_coordinates(0, 1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6)
        cp.add_coordinates(1j, 2j, 3j, 4j, -1j, -2j, -3j, -4j)

        ##
        l = axes_scale

        r = cp.n2p(1)[0]/2

        circle = Circle(radius=r).rotate(PI/2, UP).shift(axes.c2p(-2, 0, 0))
        line_r = Line(circle.get_center(), circle.get_center() + UP * r, color=ORANGE, stroke_width=6).shift(r*8*RIGHT)
        dot = Dot3d(color=RED, size=0.18).add_updater(lambda d: d.move_to(line_r.get_end()))

        cube = Cube(color=BLUE, fill_opacity=0.0, stroke_width=4, stroke_color=BLUE_D).scale(np.array([l * 4, l, l]))

        w = TAU/2
        curve_3d = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=ORANGE, stroke_width=4).shift(cp.n2p(-2))
        self.cos_t = ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t), 0]), t_min=0, t_max=8,
                                      color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
        self.sin_t = ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t)]), t_min=0, t_max=8,
                                      color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))

        cube_g = VGroup()
        A = axes.c2p(-2, -0.5, 0.5)
        B = axes.c2p(-2, 0.5, 0.5)
        C = axes.c2p(-2, 0.5, -0.5)
        D = axes.c2p(-2, -0.5, -0.5)
        E = axes.c2p(2, -0.5, 0.5)
        F = axes.c2p(2, 0.5, 0.5)
        G = axes.c2p(2, 0.5, -0.5)
        H = axes.c2p(2, -0.5, -0.5)
        line_color = BLUE
        s_width = 2

        AB = Line(A, B, color=line_color, stroke_width=s_width)
        BC = DashedLine(C, B, color=line_color, stroke_width=s_width)
        CD = DashedLine(C, D, color=line_color, stroke_width=s_width)
        DA = Line(A, D, color=line_color, stroke_width=s_width)

        AE = Line(A, E, color=line_color, stroke_width=s_width)
        BF = Line(F, B, color=line_color, stroke_width=s_width)
        CG = DashedLine(C, G, color=line_color, stroke_width=s_width)
        DH = Line(H, D, color=line_color, stroke_width=s_width)

        EF = Line(E, F, color=line_color, stroke_width=s_width)
        FG = Line(F, G, color=line_color, stroke_width=s_width)
        GH = Line(G, H, color=line_color, stroke_width=s_width)
        HE = Line(H, E, color=line_color, stroke_width=s_width)

        cube_g.add(AB, BC, CD, DA, AE, BF, CG, DH, EF, FG, GH, HE)

        y_dash = VGroup(DashedLine((A+D)/2, (E+H)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            y_dash.add(DashedLine(A + i * (E-A)/16, D + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        yt = VGroup(DA.copy(), AE.copy(), HE.copy(), DH.copy(), y_dash)

        x_dash = VGroup(DashedLine((A+B)/2, (E+F)/2, color=line_color, stroke_width=s_width*0.75))
        for i in range(1, 16):
            x_dash.add(DashedLine(A + i * (E-A)/16, B + i * (E-A)/16, color=line_color, stroke_width=s_width*0.75))
        xt = VGroup(AB.copy(), BF.copy(), EF.copy(), AE.copy(), x_dash)

        color_dict = {'e': GREEN, 'i': YELLOW_D, 't': BLUE, '\\omega': RED, '\\varphi': ORANGE, '\\sin': PINK, '\\cos': GREEN}

        text_eiwt = TexMobject('\\mathbf{e^{', 'i', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_sint = TexMobject('\\mathbf{\\sin{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_cost = TexMobject('\\mathbf{\\cos{', '(', '\\omega', 't', '+', '\\varphi', ')}}', background_stroke_color=WHITE, color=BLACK).set_color_by_tex_to_color_map(color_dict)
        text_eiwt.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*0.4 + LEFT * 0.2)
        text_sint.scale(1.25).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(DOWN*r*(1+2))
        text_cost.scale(1.2).rotate(PI/2, RIGHT).shift(axes.c2p(2.75, 0, 0)).shift(OUT*r*(1+1.45)+LEFT*0.75*r+DOWN*0.4*r)

        navi_cube = Cube(stroke_color=ORANGE, stroke_width=0.6, fill_color=ORANGE, fill_opacity=0.2).scale(0.1)
        l_cube = navi_cube.get_height()
        navi_cube.shift(l_cube/2)
        l_x = Line(ORIGIN, l_cube * UP * 4, color=GREEN)
        l_y = Line(ORIGIN, l_cube * OUT * 4, color=PINK)
        l_t = Line(ORIGIN, l_cube * RIGHT * 4, color=ORANGE)
        tex_x = TexMobject('x', background_stroke_color=WHITE, color=GREEN).rotate(PI/2, RIGHT).next_to(l_x, UP*1.25)
        tex_y = TexMobject('y', background_stroke_color=WHITE, color=PINK).rotate(PI/2, RIGHT).next_to(l_y, OUT*0.5)
        tex_t = TexMobject('t', background_stroke_color=WHITE, color=ORANGE).rotate(PI/2, RIGHT).next_to(l_t, RIGHT*0.5)
        # navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t, navi_cube).move_to(cp.n2p(-0.6-3.2j))
        navi_group = VGroup(l_x, l_y, l_t, tex_x, tex_y, tex_t).move_to(cp.n2p(-0.6-3.2j))


        e_sc=0.7
        everything=VGroup(curve_3d, cube_g, circle, line_r, dot, navi_group, yt, xt, self.sin_t, self.cos_t, text_sint, text_cost, text_eiwt,curve_3d, line_r, dot,self.cos_t,self.sin_t,circle)
        everything.scale(e_sc, about_point=ORIGIN)

        ## rotate update ##
        rotate_group = VGroup(curve_3d, line_r, dot)
        self.varphi = 0
        def rotate_all(r, dt):
            r.rotate(2.5*DEGREES, RIGHT, about_point=ORIGIN)
            self.varphi += 2.5*DEGREES
            # self.cos_t.become(ParametricFunction(lambda t: np.array([t * r, r * np.cos(w * t + self.varphi), 0]), t_min=0, t_max=8,
            #                            color=GREEN, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(OUT*r*(1+1.45))
            # self.sin_t.become(ParametricFunction(lambda t: np.array([t * r, 0, r * np.sin(w * t + self.varphi)]), t_min=0, t_max=8,
            #                            color=PINK, stroke_width=4)).shift(axes.c2p(-2, 0, 0)).shift(DOWN*r*(1+2))
        # self.cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + self.varphi), 0]), t_min=-0.0001, t_max=8,
        #                               color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((0.58*UP+OUT+LEFT*0.3)*r*(1+1.45)).scale(e_sc,about_point=ORIGIN)))
        # self.sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + self.varphi)]), t_min=-0.0001, t_max=8,
        #                               color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((0.5*DOWN+0.44*IN+LEFT*0.44)*r*(1+2)).scale(e_sc,about_point=ORIGIN)))
        self.cos_t.add_updater(lambda c: c.become(ParametricFunction(lambda t: np.array([t*r, r * np.cos(w * t + self.varphi), 0]), t_min=-0.0001, t_max=8,color=GREEN, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((0*UP+OUT+LEFT*0)*r*(1+1.45)).scale(e_sc,about_point=ORIGIN)))
        self.sin_t.add_updater(lambda s: s.become(ParametricFunction(lambda t: np.array([t*r, 0, r * np.sin(w * t + self.varphi)]), t_min=-0.0001, t_max=8, color=PINK, stroke_width=4).shift(axes.c2p(-2, 0, 0)).shift((DOWN)*r*(1+2)).scale(e_sc)))

        ## animation ##
        line_color = LIGHT_GREY
        s_width = 2
        line_sc=4.5
        axes_color=LIGHT_GREY

        up_line=Line(ORIGIN,UP*line_sc,color=axes_color)
        down_line=Line(ORIGIN,DOWN*line_sc*0.25,color=axes_color).add_tip()
        in_line=Line(ORIGIN,IN*line_sc,color=axes_color)
        out_line=Line(ORIGIN,OUT*line_sc*1.25,color=axes_color).add_tip()
        right_line=Line(ORIGIN,RIGHT*line_sc*0.5,color=axes_color).add_tip()
        left_line=Line(ORIGIN,LEFT*line_sc*0.5,color=axes_color)
        up_text= TextMobject("up").move_to(up_line.get_end())
        right_text= TextMobject("right").move_to(right_line.get_end())
        left_text= TextMobject("left").move_to(left_line.get_end())
        out_text= TextMobject("out").move_to(out_line.get_end())
        in_text= TextMobject("in").move_to(in_line.get_end())
        down_text= TextMobject("down").move_to(down_line.get_end())
        


        my_axes=VGroup(up_line,down_line,in_line,out_line,right_line,left_line,up_text,down_text,out_text,in_text,right_text,left_text,up_text)
        self.add(my_axes)
        # self.add(cp, axes)
        circle.shift(axes.c2p(4, 0, 0))
        # self.add(curve_3d, cube_g, circle, line_r, dot, navi_group, yt, xt, self.sin_t, self.cos_t, text_sint, text_cost, text_eiwt)
        self.add(curve_3d, cube_g, line_r, dot, self.sin_t, self.cos_t)
        yt.shift(DOWN*r*2)
        xt.shift(OUT*r*1.45)
        self.wait()
        self.add(rotate_group)
        rotate_group.add_updater(rotate_all)
        
        #sin
        self.move_camera(
            phi=90 * DEGREES,
            theta=-90 * DEGREES,
            # added_anims=[
            #     self.camera.frame_center.move_to, ORIGIN,
            # ]
            run_time = 10
            )
        #circle
        self.move_camera(
            phi=90 * DEGREES,
            theta=0 * DEGREES,
            # added_anims=[
            #     self.camera.frame_center.move_to, ORIGIN,
            # ]
            run_time = 10
            )
        self.move_camera(
            phi=0 * DEGREES,
            theta=90 * DEGREES,
            # added_anims=[
            #     self.camera.frame_center.move_to, ORIGIN,
            # ]
            run_time = 10
            )

        self.wait(35)
class Dot3d(VGroup):

    def __init__(self, loc=ORIGIN, size=0.2, color=WHITE, **kwargs):
        VGroup.__init__(self, **kwargs)
        dot_01 = Dot(loc, color=color).set_height(size)
        self.add(dot_01)
        num=8
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=UP)
            self.add(dot_i)
        for i in range(1, num):
            dot_i = dot_01.copy().rotate(PI * i/num, axis=RIGHT)
            self.add(dot_i)
# class test2(Scene):
#     def construct(self):
#         dot1=Dot(color=YELLOW_D).move_to(LEFT)
#         dot2=Dot3d(color=PINK).move_to(RIGHT).set_sub([YELLOW,BLUE,RED,GREEN])

#         self.play(
#             FadeIn(dot1),

#         )
#         self.play(  
#             FadeIn(dot2))
#         self.play(
#             Rotating(
#                 dot2,
#                 radians=PI,
#                 run_time=2,
#                 axis=RIGHT
#             )
        # )
class HalfCircle(VMobject):
    def __init__(self,left_down=ORIGIN,radius=3,**kwargs):
        self.top_arc = Arc(PI/2,PI).move_arc_center_to(ORIGIN + RIGHT * radius)
        # self.top_arc = Arc(PI,PI/2*3).move_arc_center_to(ORIGIN + RIGHT * radius)
        self.line = Line(self.top_arc.get_start(),self.top_arc.get_end())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.append_points(self.top_arc.points)
        self.append_points(self.line.points)
    def get_line_black(self):
        self.line.set_color(BLACK)
class SinCosHalfCircle(Scene):
    CONFIG = {
        'camera_config': {'background_color': WHITE},
        }
    def construct(self):
        half_circle= HalfCircle(color=BLACK).rotate(-90* DEGREES)
        
        sin_line, sin_brace, sin_text = sin_group = self.get_line_brace_text("sin")
        cos_line, cos_brace, cos_text = cos_group = self.get_line_brace_text("cos")

        self.play(ShowCreation(sin_line))
        self.play(
            GrowFromCenter(sin_brace),
            Write(sin_text),
        )
        # self.play(self.pi_creature.change_mode, "happy")
        self.play(ShowCreation(cos_line))
        self.play(
            GrowFromCenter(cos_brace),
            Write(cos_text),
        )
        self.wait()
        # self.change_mode("well")
        self.play(Write(self.point1))
        self.wait()

        mover = VGroup(
            sin_group,
            cos_group,
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)

        self.add(half_circle)

