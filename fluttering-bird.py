from math import floor

import pygame as pg
from pygame.locals import *

from scripts.bird import Bird
from scripts.floor import Floor


class Game:
    def __init__(self, width: int = 400, height=800, fps: int = 60):
        pg.init()

        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pg.display.set_mode((self.width, self.height))

        self.running = True
        self.clock = pg.time.Clock()
        self.dt = 0

        self.bird = Bird(self.width * 0.15, self.height / 2)

        # The floors are actually 2 floor sprites that keep wrapping behind
        # each other, so as to create the effect that its infinite
        floor_y = 688
        self.floor = pg.sprite.Group(Floor(0, floor_y), Floor(self.width, floor_y))

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.bird.flap()

            self.bird.update(self.dt)
            self.bird.draw(self.screen)

            self.floor.update(self.width)
            self.floor.draw(self.screen)

            pg.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000


if __name__ == "__main__":
    Game().run()
