from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

# import mysql.connector

Window.size = (360, 600)
class Kalium(MDApp):

    def build(self):
        self.theme_cls.theme_style='Light'
        return Builder.load_file('tela_login.kv')

Kalium().run()


