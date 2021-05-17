from manimlib.imports import *
import itertools
from myProject.utils.debugTeX import *
from myProject.utils.youtubedalao import *


class CountCube(SpecialThreeDScene):
    CONFIG={
        "default_angled_camera_position": {
        "phi":66 * DEGREES,
        # "phi": 66 * DEGREES,
        "theta": 20 * DEGREES,
        "theta": -60 * DEGREES,
        'gamma': 60 * DEGREES,
        "distance": 50,
        },
    'camera_config': {'background_color': BLACK},
        'cube_style': {
            'color': WHITE,
            'stroke_width': 0.8,
            'fill_opacity': 0.5,
        },
        'cube_scale': 0.65,
        'camera_init': {
            'phi': 60 * DEGREES,
            'gamma': 0,
            'theta': 35 * DEGREES,
        },
    "text_scale":0.65

    }
    def construct(self):
        self.set_camera_orientation(**self.camera_init)
        self.init_cubes()
    def init_cubes(self):
        self.group_02=VGroup()
        color_list = [[GREEN_E, MAROON, GREEN_A, TEAL_D],
                      [MAROON, BLUE_D, GOLD_D, PURPLE_A],
                      [GREEN_A, GOLD_D, RED, YELLOW_D],
                      [TEAL_D, PURPLE_A, YELLOW_D, PINK]]
        
        self.color_list = color_list[1]
        def create_cube(cube_color = WHITE):
            color = cube_color
            cube = Cube(
                side_length=self.cube_scale,
                fill_color=color,
                stroke_color=self.cube_style['color'],
                stroke_width=self.cube_style['stroke_width'],
            )
            # cube.rotate(45 * DEGREES) beatiful!
            return cube
        def create_group(group_dim=2, cube_color = self.color_list[3],group_name = self.group_02,loc = ORIGIN):
            cube_number = group_dim**3
            for i in range(cube_number):
                cube = create_cube(cube_color)
                group_name.add(cube)
            for z in range(group_dim):
                for y in range(group_dim):
                    for x in range(group_dim):
                        if x==0 and y==0 and z !=0:
                            # print("1  z=%d,y=%d,x=%d" % (z, y, x))
                            # print("1  now=%d,loc=%d" % ((z+1)**2,(z+1)**2 -group_dim**2))
                            group_name[x+group_dim*y+(group_dim**2)*z].next_to(group_name[x+group_dim*y+(group_dim**2)*(z-1)], IN, buff=0)
                        elif y!=0 and x==0:
                            # print("2  z=%d,y=%d,x=%d" % (z, y, x))
                            # print("2  now=%d,loc=%d" % (z**2+y+1,z**2+ y+1-group_dim))
                            group_name[x+group_dim*y+(group_dim**2)*z].next_to(group_name[x+group_dim*(y-1)+(group_dim**2)*z], RIGHT, buff=0)
                        else:
                            # print("3  z=%d,y=%d,x=%d" % (z, y, x))
                            # print("3  now=%d,loc=%d" % (z**2+y+x+1, z**2+y+x+1))
                            group_name[x+group_dim*y+(group_dim**2)*z].next_to(group_name[x+group_dim*y+(group_dim**2)*z-1], UP, buff=0)
            return group_name
        def getdebugTeX(texm):
            tex_ids=VGroup()
            for i, j in enumerate(texm):
                tex_id = Text(str(i), font="Consolas").scale(self.text_scale).set_color(YELLOW)
                tex_id.next_to(j,OUT,buff=0)
                tex_ids.add(tex_id)
            return tex_ids

        self.group_02 = create_group(group_dim=3,cube_color = self.color_list[1],group_name = self.group_02)
        self.add(Axes3d())
        # self.group_02.remove(self.group_02[63])
        # self.group_02.remove(self.group_02[2])
        my_cube=VGroup(self.group_02[18:26],self.group_02[9:11],self.group_02[12],self.group_02[15],self.group_02[0])
        layer1=self.group_02[0]
        layer2=VGroup(self.group_02[9:11],self.group_02[12],self.group_02[15])
        layer3=self.group_02[18:26]
        layer_count1=self.group_02[0]
        layer_count2=VGroup(self.group_02[10],self.group_02[12],self.group_02[15])
        layer_count3=VGroup(self.group_02[20],self.group_02[22:24],self.group_02[25])
        layer_texts=VGroup(*[
            getdebugTeX(mob)
            for mob in [layer_count1,layer_count2,layer_count3]
        ])
        layer1_text,layer2_text,layer3_text=layer_texts.split()
        # layer1_text=getdebugTeX(layer_count1)
        # layer2_text=getdebugTeX(layer_count2)
        # layer3_text=getdebugTeX(layer_count3)
        
        # self.add(my_cube)
        #lag_ratio then large then slow
        self.play(
                FadeInRandom(my_cube,lag_ratio=0.9)
            )
        anim_list=[layer1,layer2,layer3]
        
        print("anim_list2",anim_list)
        def play_animation(animlist=anim_list,anim=layer1):
            anim_list2=anim_list.copy()
            anim_list2.remove(anim)
        
            self.play(
                anim_list2[0].set_fill,GREY,
                anim_list2[1].set_fill,GREY,
                rate_func=there_and_back, 
                run_time=3
            )
            self.play(
                
                WiggleOutThenIn(anim),
            )
            #TODO: GET NAMES
            names=globals()
            # self.play(
            #     Write(names.get("%s_text"%anim))
            # )
            self.wait(2)
        
        play_animation()
        self.play(
                Write(layer1_text)
            )
        play_animation(anim=layer2)
        self.play(
                Write(layer2_text)
            )
        play_animation(anim=layer3)
        self.play(
                Write(layer3_text)
            )
        quations_before=TexMobject("1*3","+","3*2","+","4*1","=","13").scale(self.text_scale)
        
        play_animation()
        # self.play(

        # )
        # self.group_02.remove(self.group_02[15])
        # debugTeX(self,self.group_02[18:27])
        # self.begin_ambient_camera_rotation(rate=0.12)

