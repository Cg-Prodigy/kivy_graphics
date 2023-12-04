from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.graphics import Rectangle,Color
from kivy.utils import get_color_from_hex
from kivy.core.window import Window,Clock
import random
class EntryPoint(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super(EntryPoint,self).__init__(*args, **kwargs)
        self.md_bg_color = get_color_from_hex("#5a5a5a")
        self.width,self.height=(50,50)
        self._keyboard=Window.request_keyboard(None,self)
        self._keyboard.bind(on_key_down=self._on_keyboard_press)
        self.cords=self.generateCords()
        self.dx=1
        self.dy=1
        self.rects=[]
        self.screen_x=Window.width
        self.screen_y=Window.height
        with self.canvas:
            for _ in range(50):
                color=self.generateColor()
                cords=self.generateCords()
                size=self.generateSize()
                Color(rgb=color)
                rect=Rectangle(pos=cords,size=(size,size))
                rect_dict={}
                rect_dict["rect"]=rect
                rect_dict["cords"]=cords
                rect_dict["vel"]=[random.randrange(1,3),random.randrange(1,3)]
                self.rects.append(rect_dict)

        Clock.schedule_interval(self.moveSnake,1/60)


    def generateCords(self):
        rand_X=random.randrange(0,self.screen_x-self.width)
        rand_Y=random.randrange(0,self.screen_y-self.height)
        return [rand_X,rand_Y]
    def generateSize(self):
        size_u=random.randrange(20,50)
        return size_u
    def generateColor(self):
        R,G,B=random.randrange(0,255)/255,random.randrange(0,255)/255,random.randrange(0,255)/255
        return round(R,2),round(G,2),round(B,2)
    def _on_keyboard_press(self,keyboard,keycode,text,modifiers):
        if keycode[-1]=="up":
            self.cords[-1]+=self.dx
        elif keycode[-1]=="down":
            self.y+=1
        elif keycode[-1]=="left":
            self.x-=1
        elif keycode[-1]=="right":
            self.x+=1
        self.rect.pos=self.cords

    def moveSnake(self,*args,**kwargs):
        for each in self.rects:
            cords=each["cords"]
            rect=each["rect"]
            vel=each["vel"]
            if rect.pos[0]+rect.size[0]>=self.screen_x or rect.pos[0]<=0:
                vel[0]*=-1
            if rect.pos[1]+rect.size[1]>=self.screen_y or rect.pos[1]<=0:
                vel[1]*=-1
            cords[0]+=vel[0]
            cords[1]+=vel[1]
            rect.pos=cords
    
    def on_size(self,*args):
        self.screen_x=Window.width
        self.screen_y=Window.height