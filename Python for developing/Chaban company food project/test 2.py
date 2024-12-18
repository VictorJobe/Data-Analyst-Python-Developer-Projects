from kivy.lang import Builder

from kivymd.app import MDApp

Nav_drawer = '''MDNavigationDrawer:
            id: nav_drawer
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"
            Image:
                id: avatar
                size_hint: (1,1)
                source: "image.png"
            MDLabel:
                text: "          םויה לש טריפתה תא רוחבל אנ"
    
                font_name:'Arial'
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "[font=Arial.ttf]                                 ןושאר םוי[/font]"
                        font_name:'Arial'
                        on_press: root.current = 'sunday'
                        IconLeftWidget:
                            icon: "calendar"
    
    
                    OneLineIconListItem:
                        text: "[font=Arial.ttf]                                    ינש םוי[/font]"
                        on_press: root.current = 'monday'
                        IconLeftWidget:
                            icon: "calendar"
    
                    OneLineIconListItem:
                        text: "[font=Arial.ttf]                                ישילש םוי[/font]"
                        on_press: root.current = 'tuesday'
                        IconLeftWidget:
                            icon: "calendar"
    
                    OneLineIconListItem:
                        text: "[font=Arial.ttf]                                 יעיבר םוי[/font]"
                        on_press: root.current = 'wednesday'
                        IconLeftWidget:
                            icon: "calendar"
    
                    OneLineIconListItem:
                        text: "[font=Arial.ttf]                               ישימח םוי[/font]"
                        on_press: root.current = 'thursday'
                        IconLeftWidget:
                            icon: "calendar"
    '''

KV = """
Screen:


    MDLabel:
        id: direct
        text: 'Paste File Path: '
        color: [0.6,0.5,0.3,1,1]

        pos_hint: {"center_x": .55, "center_y": .7}

    MDTextField:
        id: getpath
        text: 'רקי להנ'
        hint_text:'ככככ'
        font_name: 'Arial'
        pos_hint: {"center_x": .5, "center_y": 0.7}
        size_hint_x: None
        width: "300dp"

    MDRaisedButton:
        text: "Check Text"
        font_name:'Arial'
        color: "green"
        pos_hint: {"center_x": .5, "center_y": .45}
        on_release: app.checkprint()

"""

class OneApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.screen = Builder.load_string(KV)

        return self.screen

    def checkprint(self):
        value = self.screen.ids.getpath.text
        print("What you typed is: ", value)
        print(self.root.ids)


OneApp().run()