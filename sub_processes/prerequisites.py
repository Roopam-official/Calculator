from kivy.core.text import LabelBase
from kivy.core.window import Window


def initialize():
    # Prerequisites
    Window.clearcolor = (1, 1, 1, 1)  # sets background color to white
    # registering new custom fontstyle
    LabelBase.register(
        name='FreeSerif',
        fn_regular='resources/fonts/FreeSerifItalic.ttf')
    LabelBase.register(
        name='MaterialDesign',
        fn_regular='resources/fonts/materialdesignicons-webfont.ttf')
