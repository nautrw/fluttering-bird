import pygame as pg
from pygame.locals import *
from utils import load_sprite

class Floor(pg.sprite.Sprite):
    rect: pg.Rect | pg.FRect
    image: pg.Surface

    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.image = load_sprite('floor')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.scroll_speed = 200

        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt: int | float):
        self.rect.x -= round(self.scroll_speed * dt)

        if self.rect.right <= 0:
            # The floors are actually 2 floor sprites that keep wrapping behind
            # each other, so as to create the effect that its infinite
            # this is the part that makes it wrap
            self.rect.x += self.rect.width * 2

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
