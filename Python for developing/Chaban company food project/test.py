from kivy.lang import Builder
from datetime import*

from kivymd.app import MDApp

"""a = datetime.weekday(datetime.today())
print(a)"""
a=5
b=2
if a == 5 and b ==2:
    print('oi')

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        id: toolbar
        title: "MDToolbar םולש"
        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
    Widget:    
    
    MDLabel:
        text: 'שלום'
        font_name: 'Arial'  
      
'''




class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


    def on_start(self):
        self.root.ids.toolbar.ids.label_title.font_name = "Arial"




Test().run()