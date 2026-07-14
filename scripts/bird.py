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
        self.gravity = 1200
        self.flap_y_delta = -400

    def update(self, dt: int | float):
        self.direction.y += self.gravity * dt
        self.rect.y += self.direction.y * dt

    def flap(self):
        self.direction.y = self.flap_y_delta

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, self.rect)
