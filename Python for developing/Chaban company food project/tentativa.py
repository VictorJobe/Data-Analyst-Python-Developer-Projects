from kivy.lang import Builder
from kivymd.uix.toolbar import MDToolbar
from kivymd.app import MDApp


KV = '''
BoxLayout:
    orientation: "vertical"
    MDToolbar:
        id: toolbar
        title: "Chaban Group םולש"
        label_title_font_name: 'Arial'
        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
    Widget:    

'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.root.ids.toolbar.ids.label_title.font_name = "Arial"


Test().run()