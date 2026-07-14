import pygame as pg
from pygame.locals import *
from scripts.bird import Bird

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

        self.bird = Bird(self.width * .15, self.height / 2)

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

            pg.display.flip()
            self.dt = self.clock.tick(self.fps) / 1000

if __name__ == "__main__":
    Game().run()
