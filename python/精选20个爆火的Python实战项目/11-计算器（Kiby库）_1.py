from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class CalculatorGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                # 通过eval函数计算表达式结果
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return CalculatorGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()