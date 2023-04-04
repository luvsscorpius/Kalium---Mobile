from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.uix.button import MDFloatingActionButton

# import mysql.connector

Window.size = (360, 600)
class Kalium(MDApp):

    def build(self):
        self.theme_cls.theme_style='Light'
        return Builder.load_file('tela_seleciona_cliente.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Black"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)

    def on_start(self):
        data = {
            "standard": {"md_bg_color": "#fefbff", "text_color": "#6851a5"},
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon="note-search",
                    type=type_button,
                    theme_icon_color="Custom",
                    md_bg_color=data[type_button]["md_bg_color"],
                    icon_color=data[type_button]["text_color"],
                )
            )

Kalium().run()


