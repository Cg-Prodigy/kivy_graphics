import random
from kivy.core.window import Window
from kivymd.uix.widget import MDWidget
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from kivy.uix.effectwidget import InvertEffect
class EntryPoint(MDRelativeLayout):
    def __init__(self, **kw):
        super(EntryPoint,self).__init__(**kw)
        for i in range(20):
            color=self.randColor()
            size=self.randSize()
            pos=self.randomPosition(0,Window.width-size[0],Window.height-size[-1])
            text=f"Rect {i}"
            custom_rect=CustomRect(pos,size,color,text)
            self.add_widget(custom_rect)
    @staticmethod
    def randomPosition(start,end_x,end_y):
        pos_x=random.randrange(start,end_x)
        pos_y=random.randrange(start,end_y)
        return pos_x,pos_y
    @staticmethod
    def randSize():
        h,w = random.randrange(10, 50), random.randrange(10, 50)
        return h,w
    @staticmethod
    def randColor():
        r, g, b = random.randrange(
            0, 255)/255, random.randrange(0, 255)/255, random.randrange(0, 255)/255
        return r,g,b
    
class CustomRect(MDWidget):
    def __init__(self, pos:tuple, size:tuple, color:tuple,text:str, **kwargs):
        super(CustomRect,self).__init__(**kwargs)
        self.size_hint=None,None
        self.size=size
        self.md_bg_color=color
        self.pos=pos
        self.text=text
        self.add_widget(CustomLabel(text=text,pos=pos,color=color))
        Window.bind(on_motion=self.update_position)
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            print(f"Touched {self.text}")
        return super().on_touch_down(touch)
    def update_position(self,etype,me,*args):
        if me=="update":
            print(etype.mouse_pos)
        return
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