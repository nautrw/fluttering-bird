import pygame as pg
import pygame_gui as pgui

class SceneManager:
    def __init__(self, screen: pg.Surface, ui_manager: pgui.UIManager):
        self.screen = screen
        self.ui_manager = ui_manager
        self.scene = Scene(self) # default empty scene

    def go_to(self, scene: Scene):
        self.scene.on_exit()
        self.scene = scene
        self.scene.on_enter()

class Scene:
    def __init__(self, manager: SceneManager):
        self.manager = manager

    def handle_events(self, events: list[pg.event.Event]):
        pass
    
    def update(self, dt: int | float):
        pass
    
    def render(self):
        pass

    def on_enter(self):
        pass

    def on_exit(self):
        pass
