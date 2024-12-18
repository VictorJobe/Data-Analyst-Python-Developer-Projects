from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line


class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 0)
            d = 70
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]




class MyPaintApp(MDApp):
    def build(self):
        return MyPaintWidget()



MyPaintApp().run()
