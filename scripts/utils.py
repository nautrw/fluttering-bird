import os
import pygame as pg

def load_sprite(name: str) -> pg.Surface:
    path = os.path.join("assets", "sprites", f"{name}.png")
    return pg.image.load(path).convert_alpha()
