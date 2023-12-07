import random
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.uix.widget import MDWidget
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
class EntryPoint(MDRelativeLayout):
    def __init__(self, **kw):
        super(EntryPoint,self).__init__(**kw)
        self.custom_rects=[]
        self.mouse_pos_x=0
        self.mouse_pos_y=0
        self.mouse_in_window=False
        for _ in range(50):
            rect_dict={}
            color=self.randColor()
            size=self.randSize()
            pos=self.randomPosition(0,Window.width-size[0],Window.height-size[-1])
            custom_rect=CustomRect(pos,size,color)
            rect_dict["custom_rect"]=custom_rect
            rect_dict["velocity"] = [self.randVelocity(), self.randVelocity()]
            rect_dict["cords"]=pos
            rect_dict["size"]=size
            self.add_widget(custom_rect)
            self.custom_rects.append(rect_dict)
        Clock.schedule_interval(self.moveRects,1/60)
        Window.bind(on_motion=self.get_mouse_position)
    def moveRects(self,*args,**kwargs):
        for each in self.custom_rects:
            cords=each["cords"]
            rect=each["custom_rect"]
            vel=each["velocity"]
            size=each["size"]
            color=rect.md_bg_color
            if rect.pos[0]+rect.size[0]>=Window.width or rect.pos[0]<=0:
                vel[0]*=-1
            if rect.pos[-1]+rect.size[-1]>=Window.height or rect.pos[-1]<=0:
                vel[-1]*=-1

            if self.mouse_in_window:
                if (self.mouse_pos_x>=rect.pos[0] and self.mouse_pos_x<=rect.size[0]+rect.pos[0]) and (self.mouse_pos_y>=rect.pos[-1] and self.mouse_pos_y<=rect.pos[-1]+rect.size[-1]):
                    rect.size[0]+=.7
                    rect.size[-1]+=.7
    
                else:
                    rect.size=size
                
            cords[0]+=vel[0]
            cords[1]+=vel[1]
            rect.pos=cords
            rect.md_bg_color=color

    def get_mouse_position(self,etype,me,*args):
        if me=="update":
            self.mouse_pos_x=etype.mouse_pos[0]
            self.mouse_pos_y=etype.mouse_pos[-1]
            self.mouse_in_window=True
        elif me=="end":
            self.mouse_in_window=False

    @staticmethod
    def randomPosition(start,end_x,end_y):
        pos_x=random.randrange(start,end_x)
        pos_y=random.randrange(start,end_y)
        return [pos_x,pos_y]
    @staticmethod
    def randSize():
        h,w = random.randrange(10, 50), random.randrange(10, 50)
        return h,w
    @staticmethod
    def randColor():
        r, g, b = random.randrange(
            0, 255)/255, random.randrange(0, 255)/255, random.randrange(0, 255)/255
        return r,g,b
    @staticmethod
    def randVelocity():
        return random.randint(1,2)
    
class CustomRect(MDWidget):
    def __init__(self, pos:tuple, size:tuple, color:tuple, **kwargs):
        super(CustomRect,self).__init__(**kwargs)
        self.size_hint=None,None
        self.size=size
        self.md_bg_color=color
        self.pos=pos
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            pass
        return super().on_touch_down(touch)
class CustomLabel(MDLabel):
    def __init__(self, pos:tuple,color:tuple,**kwargs):
        super(CustomLabel,self).__init__(**kwargs)
        self.theme_text_color="Custom"
        self.text_color = self.invertColor(color)
        self.adaptive_size=True
        self.pos=pos
    
    @staticmethod
    def invertColor(color:tuple):
        color_lst=[]
        for i in color:
            color_lst.append((255-i)%255)
        color_lst.append(1)
        return tuple(color_lst)