import pygame as pg
from pygame.locals import *
from utils import load_sprite

class Bird(pg.sprite.Sprite):
    rect: pg.Rect | pg.FRect
    image: pg.Surface

    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.original_image = load_sprite('bird')
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.velocity = 0
        self.gravity = 1200
        self.flap_y_delta = -400

        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt: int | float):
        self.velocity += self.gravity * dt # apply gravity
        self.rect.y += self.velocity * dt

    def flap(self):
        self.velocity = self.flap_y_delta

    def draw(self, screen: pg.Surface):
        angle = min(90, self.velocity * 0.1)
        self.image = pg.transform.rotate(self.original_image, -angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        screen.blit(self.image, self.rect)
