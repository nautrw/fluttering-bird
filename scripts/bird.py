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

        self.direction = pg.math.Vector2(0, 0)
        self.gravity = 0.4
        self.flap_y_delta = -9

    def update(self, dt: int | float):
        pressed = pg.key.get_pressed()

        if pressed[K_SPACE]:
            if self.direction.y > 0:
                self.flap()

        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def flap(self):
        self.direction.y = self.flap_y_delta

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
