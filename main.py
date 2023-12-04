from kivy.factory import Factory
from kaki.app import App
from kivymd.app import MDApp
class HotReload(App,MDApp):
    CLASSES={'EntryPoint':'app.main_ui'}
    KV_FILES=['app/kivy_lang.kv']
    AUTORELOADER_PATHS=[('.',{'recursive':True})]
    def build_app(self):
        self.title="Snake Game"
        return Factory.EntryPoint()

if __name__=='__main__':
    HotReload().run()
