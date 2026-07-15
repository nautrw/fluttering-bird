import random
from math import floor

import pygame as pg
from pygame.locals import *

from scripts.bird import Bird
from scripts.floor import Floor
from scripts.pipe import Pipe


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
        
        self.pipes = pg.sprite.Group()
        self.pipe_spawn_dt_count = 2
        self.pipe_spawn_dt_timer = 0

        self.paused = False

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and not self.paused:
                        self.bird.flap()
                    elif event.key == K_p:
                        self.paused = not self.paused
            
            if self.pipe_spawn_dt_timer >= self.pipe_spawn_dt_count:
                pipe = Pipe(self.width, random.randint(0, 588))
                self.pipes.add(pipe)
                self.pipe_spawn_dt_timer = 0

            self.bird.draw(self.screen)
            self.floor.draw(self.screen)
            self.pipes.draw(self.screen)

            if not self.paused:
                self.bird.update(self.dt)
                self.floor.update(self.dt)
                self.pipes.update(self.dt)

            pg.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
            self.pipe_spawn_dt_timer += self.dt


if __name__ == "__main__":
    Game().run()
