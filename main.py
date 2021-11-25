# Configuring Kivy (sets unmutable Window size and removing maximize/minimize button)
from kivy.config import Config
Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '500')
Config.set('graphics', 'resizable', 0)

# Main Imports
from kivy.factory import Factory
from kivy.lang.builder import Builder
from kivy.app import App
from json import load
# Custom module imports
from sub_processes.engine import calculate
from sub_processes import prerequisites



# Prerequisites
# sets background color to white and registering new custom fontstyles
prerequisites.initialize()


# App class
class CalculatorApp(App):
    def build(self):
        return Builder.load_file('graphics/main.kv')


# Main Processes(excluding Graphical part) Logic (*soon we will make it functional)

    def process_handler(self):
        pass


# Converter Button Logic (*under development)

    def app_mode(self):
        pass


# History Button Logic

    def hist_cntrlr(self):
        # Using conditions to switch between slides
        if self.root.ids.top_app_bar.ids.hist_cntrlr.text == u"\U000F02DA":  # history
            self.history()
        elif self.root.ids.top_app_bar.ids.hist_cntrlr.text == u"\U000F15A6":  # calculator-variant-outline
            self.normal_calculator_1()
        # Changing the 'advance calculator' button's text(Bug fix)
        self.root.ids.top_app_bar.ids.calc_modes_btn.font_name = "FreeSerif"
        self.root.ids.top_app_bar.ids.calc_modes_btn.text = "f(x)"
        # Loading history
        records = load(open('resources/data/history.json'))
        for input, output in records.items():
            replaced_text = f"[size=15][color=#424242]{input}[/color][/size]\n[size=20][color=#000000][b]{output}[/b][/color][/size]"
            btn = Factory.History_entry_custom_button(text=replaced_text)
            self.root.ids.slide_history.ids.history_entry_layout.add_widget(btn)
            btn.bind(on_press=lambda _, output=output: setattr(
                self.root.ids.calc_display, 'text', output))

    def history(self):
        slide3 = self.root.ids.modes_and_history_carousel.slides[2]
        self.root.ids.modes_and_history_carousel.load_slide(slide3)
        self.root.ids.top_app_bar.ids.hist_cntrlr.text = u"\U000F15A6"  # calculator-variant-outline

    def normal_calculator_1(self):
        slide1 = self.root.ids.modes_and_history_carousel.slides[0]
        self.root.ids.modes_and_history_carousel.load_slide(slide1)
        self.root.ids.top_app_bar.ids.hist_cntrlr.text = u"\U000F02DA"  # history


# Calculator modes changing Logic

    def calculator_modes(self):
        # Using conditions to switch between slides
        if self.root.ids.top_app_bar.ids.calc_modes_btn.text == "f(x)":
            self.advance_calculator()
        elif self.root.ids.top_app_bar.ids.calc_modes_btn.text == u"\U000F15A6":  # calculator-variant-outline
            self.normal_calculator_3()
        # Changing the 'history' button's text(Bug fix)
        self.root.ids.top_app_bar.ids.hist_cntrlr.text = u"\U000F02DA"  # history

    def advance_calculator(self):
        slide2 = self.root.ids.modes_and_history_carousel.slides[1]
        self.root.ids.modes_and_history_carousel.load_slide(slide2)
        self.root.ids.top_app_bar.ids.calc_modes_btn.font_name = "MaterialDesign"
        self.root.ids.top_app_bar.ids.calc_modes_btn.text = u"\U000F15A6"  # calculator-variant-outline

    def normal_calculator_3(self):
        slide1 = self.root.ids.modes_and_history_carousel.slides[0]
        self.root.ids.modes_and_history_carousel.load_slide(slide1)
        self.root.ids.top_app_bar.ids.calc_modes_btn.font_name = "FreeSerif"
        self.root.ids.top_app_bar.ids.calc_modes_btn.text = "f(x)"


CalculatorApp().run()
