import pygame as pg

class SceneManager:
    def __init__(self):
        pass

    def go_to(self, scene: Scene):
        self.scene = scene
        self.scene.manager = self

class Scene:
    manager: SceneManager

    def __init__(self):
        pass

    def handle_event(self, event: list[pg.event.Event]):
        pass
    
    def update(self):
        pass
    
    def render(self, screen: pg.Surface):
        pass
