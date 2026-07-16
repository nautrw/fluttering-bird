import os
import pygame as pg
import pygame.freetype as ft

def load_sprite(name: str) -> pg.Surface:
    path = os.path.join("assets", "sprites", f"{name}.png")
    return pg.image.load(path).convert_alpha()

def load_font(name: str) -> ft.Font:
    path = os.path.join("assets", "fonts", f"{name}.ttf")
    return ft.Font(path)
