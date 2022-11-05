
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout



class CalculatorApp(App):
    def add_number(self, instance):
        if (self.formula == "0"):
            self.formula = ""
        self.formula += str(instance.text)
        print(self.formula)

    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation ='vertical')
        gl = GridLayout(cols = 4 )
        bl.add_widget(Label(text="0"))

        gl.add_widget(Button(text="7", on_press = self.add_number))
        gl.add_widget(Button(text="8"))
        gl.add_widget(Button(text="9"))
        gl.add_widget(Button(text="+"))

        gl.add_widget(Button(text="4"))
        gl.add_widget(Button(text="5"))
        gl.add_widget(Button(text="6"))
        gl.add_widget(Button(text="-"))

        gl.add_widget(Button(text="1"))
        gl.add_widget(Button(text="2"))
        gl.add_widget(Button(text="3"))
        gl.add_widget(Button(text="*"))

        gl.add_widget(Button(text="c"))
        gl.add_widget(Button(text="0"))
        gl.add_widget(Button(text="/"))
        gl.add_widget(Button(text="."))

        gl.add_widget(Button())
        gl.add_widget(Button(text="="))
        gl.add_widget(Button(text="del"))
        gl.add_widget(Button())


        bl.add_widget(gl)
        return bl

if __name__ == "__main__":
    CalculatorApp().run()

