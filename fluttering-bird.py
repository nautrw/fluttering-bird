import pygame as pg
from pygame.locals import *

class Game:
    def __init__(self, width: int = 400, height = 800, fps: int = 60):
        pg.init()

        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pg.display.set_mode((self.width, self.height))

        self.running = True
        self.clock = pg.time.Clock()
        self.dt = 0

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == QUIT:
                    self.running = False

        pg.display.flip()
        self.dt = self.clock.tick(self.fps)

if __name__ == "__main__":
    Game().run()
