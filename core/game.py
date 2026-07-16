import random
from math import floor

import pygame as pg
from pygame.locals import *
from utils import load_sprite
from core.scene_manager import SceneManager
from scenes.title import TitleScene
import pygame_gui as pgui

from entities.bird import Bird
from entities.floor import Floor
from entities.pipe import Pipe


class Game:
    def __init__(self, width: int = 400, height=700, fps: int = 60):
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
        floor_height = load_sprite("floor").get_rect().height
        floor_y = self.height - floor_height
        self.floor = pg.sprite.Group(Floor(0, floor_y), Floor(self.width, floor_y))
        
        self.pipes = pg.sprite.Group()
        self.pipe_spawn_dt_count = 1.5
        self.pipe_spawn_dt_timer = 0
        self.pipe_min_y = int(load_sprite('pipe').get_rect().height * .35)
        self.pipe_max_y = floor_y - 150

        self.paused = False

        self.ui_manager = pgui.UIManager((self.width, self.height))
        self.manager = SceneManager(self.screen, self.ui_manager)
        self.manager.go_to(TitleScene())

    def run(self):
        # while self.running:
        #     self.screen.fill((0, 0, 0))

            #
            # if self.pipe_spawn_dt_timer >= self.pipe_spawn_dt_count:
            #     pipe_y = random.randint(self.pipe_min_y, self.pipe_max_y)
            #     pipe = Pipe(self.width, pipe_y)
            #     self.pipes.add(pipe)
            #     self.pipe_spawn_dt_timer = 0

            # self.bird.draw(self.screen)
            # self.pipes.draw(self.screen)
            # self.floor.draw(self.screen)

            # if not self.paused:
            #     self.bird.update(self.dt)
            #     self.floor.update(self.dt)
            #     self.pipes.update(self.dt)

            # if pg.sprite.spritecollide(self.bird, self.pipes, False, pg.sprite.collide_mask): # ty:ignore
            #     exit()

            # for pipe in self.pipes:
            #     if not pipe.passed and pipe.rect.right < self.bird.rect.centerx:
            #         pipe.passed = True
            #         print("score")

            # pg.display.flip()
            # self.dt = self.clock.tick(self.fps) / 1000
            # self.pipe_spawn_dt_timer += self.dt
        while self.running: 
            if pg.event.get(QUIT):
                exit()

            self.manager.scene.handle_events(pg.event.get())
            self.manager.scene.update()
            self.manager.scene.render()

            self.dt = self.clock.tick(self.fps) / 1000
            self.ui_manager.update(self.dt)
            self.ui_manager.draw_ui(self.screen)
            pg.display.flip()
