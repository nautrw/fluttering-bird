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

        self.ui_manager = pgui.UIManager((self.width, self.height))
        self.manager = SceneManager(self.screen, self.ui_manager)
        self.manager.go_to(TitleScene(self.manager))

    def run(self):
        while self.running: 
            if pg.event.get(QUIT):
                exit()

            self.manager.scene.handle_events(pg.event.get())
            self.manager.scene.update(self.dt)
            self.manager.scene.render()

            pg.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
