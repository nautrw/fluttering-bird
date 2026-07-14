import pygame as pg
from pygame.locals import *
from scripts.utils import load_sprite

class Bird(pg.sprite.Sprite):
    rect: pg.Rect | pg.FRect
    image: pg.Surface

    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.image = load_sprite('bird')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.fall_speed = 250

    def update(self, dt: int | float):
        pressed = pg.key.get_pressed()

        if pressed[K_SPACE]:
            self.rect.bottom -= round(self.fall_speed * dt)
        else:
            self.rect.bottom += round(self.fall_speed * dt)

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
