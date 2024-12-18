from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog



usernameID_helper = '''


MDRectangleFlatButton:
    text: 'שלח'
    font_name:'DejaVuSans.ttf'
    pos_hint: {'center_x':0.5,'center_y':0.3}
    on_press: root.manager.current = 'profile'
'''

class FoodApp(MDApp):
    def build(self):
        screen = Screen()
        #self.usernameID = MDTextField(text="Enter your ID", pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                         size_hint_x=None, width=300)





        submit_button = MDRectangleFlatButton(text="Submit", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                              on_release=self.show)

        self.usernameID = Builder.load_string(usernameID_helper)
        screen.add_widget(submit_button)
        screen.add_widget(self.usernameID)

        return screen

    def show(self, obj):
        if self.usernameID.text == '':
            check = 'Please enter your ID'
        else:
            check = self.usernameID.text
        close_button = MDRectangleFlatButton(text="Close", on_release=self.close_dialog_box)
        self.dialog_box = MDDialog(title="It works!!!", text=self.usernameID.text, size_hint=(0.7, 1),
                                   buttons=[close_button])
        self.dialog_box.open()

    def close_dialog_box(self, obj):
        self.dialog_box.dismiss()



FoodApp().run()

