import pygame as pg
import pygame_gui as pgui

class SceneManager:
    def __init__(self, screen: pg.Surface, ui_manager: pgui.UIManager):
        self.screen = screen
        self.ui_manager = ui_manager

    def go_to(self, scene: Scene):
        self.scene = scene

class Scene:
    def __init__(self, manager: SceneManager):
        self.manager = manager

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            self.manager.ui_manager.process_events(event)
    
    def update(self):
        pass
    
    def render(self):
        pass
