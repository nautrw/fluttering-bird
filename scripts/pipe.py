import pygame as pg
from pygame.locals import *
from scripts.utils import load_sprite

class Pipe(pg.sprite.Sprite):
    rect: pg.Rect | pg.FRect
    image: pg.Surface

    def __init__(self, x: int | float, y: int | float):
        super().__init__()

        self.gap = 150
        self.speed = 200

        self.pipe_sprite = load_sprite("pipe")
        self.pipe_rect = self.pipe_sprite.get_rect()

        self.top = pg.transform.flip(self.pipe_sprite, False, True)
        self.top_rect = self.top.get_rect(topleft=(x, 0))

        self.bottom = self.pipe_sprite
        self.bottom_rect = self.bottom.get_rect(topleft=(x, self.pipe_rect.height + self.gap))
        
        self.image = pg.Surface((self.pipe_rect.width, self.pipe_rect.height * 2 + self.gap), flags=SRCALPHA)
        self.image.blit(self.top, (0, 0)) 
        self.image.blit(self.bottom, (0, self.pipe_rect.height + self.gap)) 
        self.rect = self.image.get_rect(midleft=(x, y))

    def update(self, dt: int | float):
        self.rect.x -= round(self.speed * dt)
        
        if self.rect.right <= 0:
            self.kill()
