from utils import load_font
import pygame as pg
from pygame import freetype as ft
from core.scene_manager import Scene
import pygame_gui as pgui

class TitleScene(Scene):
    def __init__(self):
        ft.init()

        self.font = load_font("Boxy-Bold")

        play_button_rect = pg.Rect(self.manager.screen.width // 2, self.manager.screen.height *.25, 200, 100)
        self.play_button = pgui.elements.UIButton(play_button_rect, "Play", self.manager.ui_manager)

    def render(self):
        self.manager.screen.fill("black")

        text, rect = self.font.render("Fluttering Bird", "white", size=32)
        rect.center = (self.manager.screen.width // 2, self.manager.screen.height * .25)
        self.manager.screen.blit(text, rect)
