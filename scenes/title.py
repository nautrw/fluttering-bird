from utils import load_font
import pygame as pg
from pygame import freetype as ft
from core.scene_manager import Scene, SceneManager
import pygame_gui as pgui

class TitleScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        ft.init()

        self.font = load_font("Boxy-Bold")

        play_button_rect = pg.Rect(0, 0, 200, 100)
        self.play_button = pgui.elements.UIButton(play_button_rect, "Play", self.manager.ui_manager, anchors={'center': 'center'})

    def render(self):
        self.manager.screen.fill("black")

        text, rect = self.font.render("Fluttering Bird", "white", size=32)
        rect.center = (self.manager.screen.width // 2, self.manager.screen.height * .25)
        self.manager.screen.blit(text, rect)

        self.manager.ui_manager.draw_ui(self.manager.screen)

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            self.manager.ui_manager.process_events(event)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    print("pressed")

    def update(self, dt: int | float):
        self.manager.ui_manager.update(dt)
