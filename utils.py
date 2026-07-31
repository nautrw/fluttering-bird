import sys, os
import pygame as pg
import pygame.freetype as ft

# needed for pyinstaller to work
def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def load_sprite(name: str) -> pg.Surface:
    file = resource(f"assets/sprites/{name}.png")
    return pg.image.load(file).convert_alpha()
