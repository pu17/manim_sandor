from manimlib.imports import *

class HalfCircle(VMobject):
    def __init__(self,left_down=ORIGIN,loc=ORIGIN,arcradius=3,**kwargs):
        self.top_arc = Arc(PI/2,PI,radius=arcradius,stroke_width=1).rotate(-90* DEGREES).move_arc_center_to(loc)
        # .move_arc_center_to(ORIGIN + RIGHT * arcradius)
        # self.top_arc = Arc(PI,PI/2*3).move_arc_center_to(ORIGIN + RIGHT * radius)
        self.line = Line(self.top_arc.get_start(),self.top_arc.get_end(),stroke_width=1)
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        self.append_points(self.top_arc.points)
        self.append_points(self.line.points)
    def get_line_black(self):
        self.line.set_color(BLACK)

class TrigRepresentationsScene(GraphScene):
    CONFIG = {
        'x_color': BLUE,
        'y_color': YELLOW,
        'angle_color': RED,
        "graph_origin": UP + 0.25 * LEFT,
        "graph_origin":ORIGIN,
        "x_axis_width": 4,
        "y_min": -1,
        "y_max": 1,
        "x_min": -1,
        "x_max": 1,
        "y_axis_height": 4,
        "label_stroke_color": GREY,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "x_labeled_nums": [],
        "y_labeled_nums": [],
        # "circle_color": "#f1a608",
        "circle_color": GREY,
        "theta": 0,
        "increment_value": TAU,
        "final_theta": 0 * DEGREES,
        "radius": 2,
        "arc_radius": 0.8,
        "radius_color": RED,
        "inner_sector_scale": 4.5,
        "sector_color": TEAL,
        "close_new_points": True,
        "anchors_span_full_range": False,
        # points
        'point_color': TEAL,
        'point_size': 0.2,

        'num_decimal_places': 2,
        'coordinates_scale': 1,
        'x_coordinates_color': LIGHT_GREY,
        'y_coordinates_color': LIGHT_GREY,

        # "theta_color": "#f1a608",
        "theta_color": TEAL,
        "theta_height": 0.3,

        "theta_value": 30*DEGREES,

        "x_line_colors":TEAL,
        # "x_line_colors":"#d56d60",
        # "y_line_colors":"#6e8cb6",
        "y_line_colors":TEAL,
        "axis_color": GREY,
        "axis_width":2

    }

    def setup(self):
        self.init_axes()
        self.init_halfcircle()
        self.init_theta_group()

    def init_axes(self):
        # self.setup_axes()
        # self.y_line = Line(self.y_axis.get_start(), self.y_axis.get_center(), color=self.axis_color).scale(1.3,about_point=self.y_axis.get_start())
        # self.x_line = Line(self.x_axis.get_start(), self.x_axis.get_end(), color=self.axis_color).scale(1.3)
        # self.y_axis_label_mob.shift(UP)
        # self.x_axis_label_mob.shift(RIGHT)
        # self.my_axes=VGroup(self.axes,self.y_line,self.x_line)
        # self.add(self.y_line, self.x_line)

        self.y_line = Line(RIGHT, LEFT, color=self.axis_color,stroke_width=self.axis_width).scale(2.3,about_point=ORIGIN)
        self.x_line = Line(ORIGIN, UP, color=self.axis_color,stroke_width=self.axis_width).scale(2.3,about_point=ORIGIN)
        self.my_axes=VGroup(self.y_line,self.x_line)
        self.add(self.y_line, self.x_line)
    


    def init_halfcircle(self):
        # self.circle = Circle(
        #     radius=self.radius,
        #     color=self.circle_color)
        self.halfcircle = HalfCircle(
            arcradius=self.radius, 
            color=self.circle_color,
            loc=self.graph_origin
            )
        # self.halfcircle.move_(self.graph_origin)
        self.add(self.halfcircle)
    def init_theta_group(self):
        self.theta_group = self.get_theta_group()
        self.add(self.theta_group)
    def add_trig_lines(self, *funcs, **kwargs):
        lines = VGroup(*[
            self.get_trig_line(func, **kwargs)
            for func in funcs
        ])
        self.add(*lines)
    def get_theta_group(self):
        # angle = Arc(
        #     radius=self.radius,
        #     start_angle=self.theta,
        #     angle=radius_line.get_angle(),
        #     color=self.radius_color,
        #     close_new_points=True,
        #     anchors_span_full_range=False,
        # ).move_arc_center_to(self.graph_origin)
        arc = Sector(
            outer_radius=self.radius / self.inner_sector_scale,
            start_angle=0*DEGREES,
            angle=self.theta_value,
            color=self.sector_color,
            close_new_points=True,
            anchors_span_full_range=False,
        ).move_arc_center_to(self.graph_origin).set_fill(self.sector_color, opacity=0.4)

        arc2 = Arc(
            start_angle=0*DEGREES,
            angle=self.theta_value,
            radius=self.arc_radius,
            color=self.radius_color,
        ).move_arc_center_to(self.graph_origin)
        
        arc3 = Arc(
            start_angle=0*DEGREES,
            angle=180 * DEGREES - self.theta_value,
            radius=self.arc_radius,
            color=self.radius_color,
        ).move_arc_center_to(self.graph_origin)

        theta_sc = 0.8
        theta = TexMobject("\\theta",background_stroke_width=0).scale(theta_sc)
        theta.set_background_stroke(color=self.theta_color)
        theta.shift(arc2.point_from_proportion(0.5))
        theta.set_color(self.theta_color)
        theta.set_stroke(width=0)
        theta.set_height(self.theta_height)
        self.theta2 = TexMobject("\\pi-\\theta",stroke_width=0,background_stroke_width=0).scale(theta_sc)
        # self.theta2.set_stroke(width=0)
        self.theta2.set_background_stroke(color=self.theta_color)
        self.theta2.shift(arc3.point_from_proportion(0.5))
        self.theta2.set_color(self.theta_color)
        self.theta2.set_height(self.theta_height)
        line = Line(self.graph_origin, self.get_circle_point(), color=self.point_color)
        dot = Dot(line.get_end(), radius = 0.1,color=self.point_color)
        return VGroup(line, arc, theta,dot)

    def get_circle_point(self):
        return rotate_vector(self.radius*RIGHT, self.theta_value)
        # return rotate_vector(self.radius*RIGHT, 0*DEGREES)

    def get_trig_line(self, func_name = "sin", color = None):
        assert(func_name in ["sin", "tan", "sec", "cos", "cot", "csc"])
        is_co = func_name in ["cos", "cot", "csc"]
        if color is None:
            if is_co:
                color = self.y_line_colors
            else:
                color = self.x_line_colors

        #Establish start point
        if func_name in ["sin", "cos", "tan", "cot"]:
            start_point = self.get_circle_point()
        else:
            start_point = self.graph_origin

        #Establish end point
        if func_name is "sin":
            end_point = start_point[0]*RIGHT
        elif func_name is "cos":
            end_point = start_point[1]*UP
        elif func_name in ["tan", "sec"]:
            end_point = (1./np.cos(self.theta_value))*self.radius*RIGHT
        elif func_name in ["cot", "csc"]:
            end_point = (1./np.sin(self.theta_value))*self.radius*UP
        return DashedLine(start_point, end_point, color = color)







class ShowSinCos(TrigRepresentationsScene):
    CONFIG = {
        "alt_theta_val": 150*DEGREES,
        'camera_config': {'background_color': WHITE}
    }
    def setup(self):
        # PiCreatureScene.setup(self)
        TrigRepresentationsScene.setup(self)

    def construct(self):
        self.introduce_angle()
        self.show_sine_and_cosine()
        # self.show_tangent_and_cotangent()
        # self.show_secant_and_cosecant()
        # self.explain_cosecant()
        # self.summarize_full_group()

    def introduce_angle(self):
        self.remove(self.halfcircle)
        self.remove(self.theta_group)
        line, self.arc,self.theta, dot = self.theta_group
        # self.theta_group = line, Barc,self.theta,dot
        #
        # line.rotate(-self.theta_value)
        brace = Brace(line, UP+0.6*LEFT, buff = SMALL_BUFF)
        one = brace.get_text("1", buff = SMALL_BUFF)
        # VGroup(line, brace, one).rotate(self.theta_value)

        words = Text("对应点",font='方正经黑简体').scale(0.5)
        words.next_to(dot, UP+RIGHT, buff = 1.5*LARGE_BUFF)
        words.shift_onto_screen()
        arrow = Arrow(words.get_bottom(), dot, buff = SMALL_BUFF)
        # self.point1 = TexMobject("(","{\\cos\\theta}",",","{\\sin\\theta}",")").scale(0.75)
        # #
        self.play(
            ShowCreation(line),
            ShowCreation(self.arc),
        )

        self.play(Write(self.theta))
        # self.play(self.pi_creature.change_mode, "pondering")
        self.play(
            LaggedStart(
            ShowCreation(self.halfcircle),
            Rotating(line,radians=150* DEGREES, rate_func = smooth, in_place = False,about_point=self.graph_origin),
            lag_ratio=0.1,
            ),
            run_time = 2
        )
        self.play(
            Rotating(line,radians=-150* DEGREES, rate_func = smooth, in_place = False,about_point=self.graph_origin),
        )
        self.play(
            Write(words),
            ShowCreation(arrow),
            ShowCreation(dot)
        )
        self.wait()
        self.play(
            GrowFromCenter(brace),
            Write(one)
        )
        self.wait(2)
        self.play(*list(map(FadeOut, [
            words, arrow, brace, one
        ])))
        self.play(

        )
        self.radial_line_label = VGroup(brace, one)
        self.intro_line =line
        # sc=0.7
        # self.my_axes.scale_about_point(sc, ORIGIN)
        # self.theta_group.scale_about_point(sc,ORIGIN)
    def show_sine_and_cosine(self):
        # self.my_axes.scale_about_point(0.7,ORIGIN)
        sin_line, sin_brace, sin_text = sin_group = self.get_line_brace_text("sin")
        cos_line, cos_brace, cos_text = cos_group = self.get_line_brace_text("cos")

        sin_text.next_to(cos_line,LEFT+UP)
        cos_text.next_to(sin_line,DOWN)

        self.play(ShowCreation(sin_line))
        self.play(
            # GrowFromCenter(sin_brace),
            Write(cos_text),
        )
        # self.play(self.pi_creature.change_mode, "happy")
        self.play(ShowCreation(cos_line))
        self.play(
            # GrowFromCenter(cos_brace),
            Write(sin_text),
        )
        self.wait()
        # self.change_mode("well")
        # self.play(Write(self.point1))
        self.wait()

        mover = VGroup(
            sin_group[0],
            cos_group[0],
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        print(thetas)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            targets.append(VGroup(
                self.get_line_brace_text("sin")[0],
                self.get_line_brace_text("cos")[0],
                self.get_theta_group()
            ))
        thetas2 = np.linspace(self.alt_theta_val,np.pi / 5,  100)

        print(thetas2)
        targets2 = []
        for theta in thetas2:
            self.theta_value = theta
            targets2.append(VGroup(
                self.get_line_brace_text("sin")[0],
                self.get_line_brace_text("cos")[0],
                self.get_theta_group()
            ))
        fate_color=BLACK
        fate_ratio=0.1
        self.play(
            *list(map(FadeIn, [
                sin_line.copy().set_color(fate_color),
                cos_line.copy().set_color(fate_color),
                self.intro_line.copy().set_color(fate_color),
                self.arc.copy().set_color(fate_color),
                self.theta.copy().set_color(fate_color)
            ]))
        )
        sin_line_before =  sin_line.copy()
        cos_line_before =  cos_line.copy()

        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            # rate_func=there_and_back,
            run_time = 2,
            # rate_func = there_and_back
        ))

        # self.play(*list(map(FadeOut,[sin_brace, sin_text,cos_brace, cos_text])))
        self.play(
            Transform(self.theta, self.theta2)

        )
        dot = self.theta_group[-1]
        # self.point2 = TexMobject("(","{\\cos\\theta}",",","{\\sin\\theta}",")").scale(0.75)
        # self.point2.next_to(dot, UP + RIGHT, buff=0.2)
        # self.play(Transform(VGroup(sin_line_before,cos_line_before),VGroup(sin_line.copy(),cos_line.copy())))
        # self.play(
        #     Transform(sin_line_before,cos_line.copy()),
        #     Transform(cos_line_before,sin_line.copy()),
        # )
        # point2=self.point1.copy()
        # self.play(
        #     point2.move_to,self.point2.get_center()
        #           )
        self.play(
            # Swap(point2[1],point2[3]), 
            Transform(sin_line_before,cos_line.copy()),
            Transform(cos_line_before,sin_line.copy()),
        )

        # self.play(Succession(
        #     *[
        #         Transform(mover, target, rate_func=linear)
        #         for target in targets2
        #     ],
        #     # rate_func=there_and_back,
        #     run_time=2,
        #     # rate_func = there_and_back
        # ))
        sin_tex = "{\\sin\\theta}"
        cos_tex = "{\\cos\\theta}"
        sin_pi_tex ="{\\sin(\\dfrac{\\pi}{2}-\\theta})"
        tan_frac = TexMobject("= \\frac" + sin_tex + cos_tex)
        cot_frac = TexMobject("= \\frac" + cos_tex + sin_tex)
        tan_frac.to_corner(UP+LEFT)
        tan_frac.shift(RIGHT)
        cot_frac.next_to(tan_frac, DOWN)
        # sin_pi = TexMobject("2.1")
        # self.play(
        #     Write(sin_pi)
        # )

        self.theta_value = thetas2[-1]
        self.wait()
        self.sin_group, self.cos_group = sin_group, cos_group
        
        # self.theta_group.scale_about_point(0.7,ORIGIN)
        # self.circle.scale_about_point(0.7,ORIGIN)
        # self.my_axes.scale_about_point(0.7,ORIGIN)
        # sc =0.7
    def show_tangent_and_cotangent(self):
        tan_group = self.get_line_brace_text("tan")
        cot_group = self.get_line_brace_text("cot")
        tan_text = tan_group[-1]
        cot_text = cot_group[-1]
        line = Line(UP, DOWN).scale(FRAME_Y_RADIUS)
        line.rotate(self.theta_value)
        line.move_to(self.theta_group[-1])
        line.set_stroke(width = 2)

        sin_tex = "{\\sin\\theta}"
        cos_tex = "{\\cos\\theta}"
        tan_frac = TexMobject("= \\frac" + sin_tex + cos_tex)
        cot_frac = TexMobject("= \\frac" + cos_tex + sin_tex)
        tan_frac.to_corner(UP+LEFT)
        tan_frac.shift(RIGHT)
        cot_frac.next_to(tan_frac, DOWN)


        # self.change_mode("pondering")
        for frac, text in (tan_frac, tan_text), (cot_frac, cot_text):
            # VGroup(frac[5], frac[-2]).set_color(YELLOW)
            frac.scale_in_place(0.7)
            text.save_state()
            text.next_to(frac, LEFT)
            self.play(Write(VGroup(text, frac)))
            self.wait()
        # self.change_mode("confused")
        self.wait()
        self.play(*list(map(FadeOut, [
            tan_frac, cot_frac, self.sin_group, self.cos_group
        ])))
        self.wait()

        self.play(
            # self.theta_group[-1].set_color, YELLOW,
            ShowCreation(line),
            # self.pi_creature.change_mode, 'pondering'
        )
        small_lines = VGroup()
        for group in tan_group, cot_group:
            small_line, brace, text = group
            self.play(
                ShowCreation(small_line),
                GrowFromCenter(brace),
                text.restore,
            )
            self.wait()
            small_lines.add(small_line)
        self.play(FadeOut(line), Animation(small_lines))

        mover = VGroup(
            tan_group,
            cot_group,
            self.theta_group,
        )
        thetas = np.linspace(self.theta_value, self.alt_theta_val, 100)
        targets = []
        for theta in thetas:
            self.theta_value = theta
            targets.append(VGroup(
                self.get_line_brace_text("tan"),
                self.get_line_brace_text("cot"),
                self.get_theta_group()
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets
            ],
            run_time = 2,
            rate_func = there_and_back
        ))
        thetas2 = np.linspace(self.alt_theta_val,np.pi / 5, 100)
        targets2 = []
        for theta in thetas2:
            self.theta_value = theta
            targets2.append(VGroup(
                self.get_line_brace_text("tan"),
                self.get_line_brace_text("cot"),
                self.get_theta_group()
            ))
        self.play(Succession(
            *[
                Transform(mover, target, rate_func=linear)
                for target in targets2
            ],
            run_time=2,
            rate_func=there_and_back
        ))

        self.theta_value = thetas[0]

        # self.change_mode("happy")
        self.wait(2)

        # self.tangent_line = self.get_tangent_line()
        # self.add(self.tangent_line)
        # self.play(*it.chain(*[
        #     list(map(FadeOut, [tan_group, cot_group])),
        #     [Animation(self.theta_group[-1])]
        # ]))
    def get_line_brace_text(self, func_name="sin"):
        line = self.get_trig_line(func_name)
        angle = line.get_angle()
        vect = rotate_vector(UP, angle)
        vect = np.round(vect, 1)
        if (vect[1] < 0) ^ (func_name is "sec"):
            vect = -vect
            angle += np.pi
        brace = Brace(
            Line(
                line.get_length() * LEFT / 2,
                line.get_length() * RIGHT / 2,
            ),
            UP
        )
        if func_name =="sin":
            brace.move_to(line.get_center() + 0.25*RIGHT)
        elif func_name =="cos":
            brace.move_to(line.get_center() + 0.25 * UP)
        else:
            brace.move_to(line.get_center() + 0.15 * RIGHT+0.15 * UP)

        brace.rotate(angle)

        brace.set_color(line.get_color())
        text = TexMobject("\\%s\\theta" % func_name,)
        text.scale(0.75)
        # text[-2].set_color(self.theta_color)
        # text.add_background_rectangle()
        text.next_to(brace.get_center_of_mass(), vect, buff=1.2 * MED_SMALL_BUFF)
        return VGroup(line, brace, text)

    def get_tangent_line(self):
        return Line(
            self.radius * (1. / np.sin(self.theta_value)) * UP,
            self.radius * (1. / np.cos(self.theta_value)) * RIGHT,
            color=GREY
        )



