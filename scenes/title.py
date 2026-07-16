from utils import load_font
import pygame as pg
from pygame import freetype as ft
from core.scene_manager import Scene

class TitleScene(Scene):
    def __init__(self):
        ft.init()

        self.font = load_font("Boxy-Bold")

    def render(self, screen: pg.Surface):
        screen.fill("black")

        title_pos = (screen.width // 2, screen.height * .25)
        self.font.render_to(screen, title_pos, "Fluttering Bird", "white", size=32)
