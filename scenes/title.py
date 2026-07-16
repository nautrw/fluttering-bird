import pygame as pg
from core.scene_manager import Scene, SceneManager
from scenes.main_game import MainGameScene
import pygame_gui as pgui

class TitleScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)

        title_rect = pg.Rect(0, 0, 200, 100)
        self.title = pgui.elements.UILabel(title_rect, "Fluttering Bird", self.manager.ui_manager, anchors = {'centerx': 'centerx'})

        play_button_rect = pg.Rect(0, 0, 200, 100)
        self.play_button = pgui.elements.UIButton(play_button_rect, "Play", self.manager.ui_manager, anchors={'center': 'center'})

    def render(self):
        self.manager.screen.fill("black")
        self.manager.ui_manager.draw_ui(self.manager.screen)

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            self.manager.ui_manager.process_events(event)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.manager.go_to(MainGameScene(self.manager))

    def update(self, dt: int | float):
        self.manager.ui_manager.update(dt)
