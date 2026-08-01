import sys
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

from utils import resource


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

        # Adding the font path and then reloading the theme makes it so that
        # it will use the correct resource path when ran as a binary
        self.ui_manager = pgui.UIManager((self.width, self.height))
        self.ui_manager.add_font_paths("Pizel", resource("assets/fonts/Pizel.ttf"))
        self.ui_manager.get_theme().load_theme('assets/themes/theme.json')

        self.manager = SceneManager(self.screen, self.ui_manager)
        self.manager.go_to(TitleScene(self.manager))

    def run(self):
        while self.running: 
            if pg.event.get(QUIT):
                sys.exit()

            self.manager.scene.handle_events(pg.event.get())
            self.manager.scene.update(self.dt)
            self.manager.scene.render()

            pg.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000
