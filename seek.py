from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty



class GeneSeek(Widget):

    def do_action(self):
        print self.ids.textinput.text
        self.ids.ficha.text = 'Gene such and such, etc.'


class SeekApp(App):
    def build(self):
        return GeneSeek()


if __name__ == '__main__':
    SeekApp().run()
