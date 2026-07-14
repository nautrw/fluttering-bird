import pygame as pg
from pygame.locals import *
from scripts.utils import load_sprite

class Floor(pg.sprite.Sprite):
    rect: pg.Rect | pg.FRect
    image: pg.Surface

    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.image = load_sprite('floor')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, screen_width: int | float):
        self.rect.x -= 2

        if self.rect.right <= 0:
            # The floors are actually 2 floor sprites that keep wrapping behind
            # each other, so as to create the effect that its infinite
            # this is the part that makes it wrap
            self.rect.x = screen_width

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
