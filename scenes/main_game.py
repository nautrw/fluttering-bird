import random
from math import floor

import pygame as pg
from pygame.locals import *
from utils import load_sprite
from core.scene_manager import Scene, SceneManager
import pygame_gui as pgui

from entities.bird import Bird
from entities.floor import Floor
from entities.pipe import Pipe

class MainGameScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)

        self.screen_width = self.manager.screen.get_width()
        self.screen_height = self.manager.screen.get_height()

        self.bird = Bird(self.screen_width * 0.15, self.screen_height / 2)

        # The floors are actually 2 floor sprites that keep wrapping behind
        # each other, so as to create the effect that its infinite
        floor_height = load_sprite("floor").get_rect().height
        floor_y = self.manager.screen.get_height() - floor_height
        self.floor = pg.sprite.Group(Floor(0, floor_y), Floor(self.screen_width, floor_y))
        
        self.pipes = pg.sprite.Group()
        self.pipe_spawn_dt_count = 1.5
        self.pipe_spawn_dt_timer = 0
        self.pipe_min_y = int(load_sprite('pipe').get_rect().height * .35)
        self.pipe_max_y = floor_y - 150

        self.score = 0
        score_rect = pg.Rect(0, 0, 300, 200)
        self.score_label = pgui.elements.UILabel(score_rect, str(self.score), self.manager.ui_manager, anchors={'centerx': 'centerx'})

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            self.manager.ui_manager.process_events(event)

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.bird.flap()

    def render(self):
        self.manager.screen.fill("black")
        self.bird.draw(self.manager.screen)
        self.pipes.draw(self.manager.screen)
        self.floor.draw(self.manager.screen)
        self.manager.ui_manager.draw_ui(self.manager.screen)
    
    def update(self, dt: int | float):
        self.manager.ui_manager.update(dt)

        if self.pipe_spawn_dt_timer >= self.pipe_spawn_dt_count:
            pipe_y = random.randint(self.pipe_min_y, self.pipe_max_y)
            pipe = Pipe(self.screen_width, pipe_y)
            self.pipes.add(pipe)
            self.pipe_spawn_dt_timer = 0

        if pg.sprite.spritecollide(self.bird, self.pipes, False, pg.sprite.collide_mask): # ty:ignore
            exit()

        for pipe in self.pipes:
            if not pipe.passed and pipe.rect.right < self.bird.rect.centerx:
                pipe.passed = True
                self.score += 1

        self.bird.update(dt)
        self.floor.update(dt)
        self.pipes.update(dt)

        self.pipe_spawn_dt_timer += dt
