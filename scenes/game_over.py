import pygame as pg
from core.scene_manager import Scene, SceneManager
import scenes.title
import pygame_gui as pgui

class GameOverScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)

        game_over_text_rect = pg.Rect(0, 0, 300, 200)
        self.game_over_text = pgui.elements.UILabel(game_over_text_rect, "Game Over", self.manager.ui_manager, anchors = {'centerx': 'centerx'})

        restart_button_rect = pg.Rect(0, 0, 300, 100)
        self.restart_button = pgui.elements.UIButton(restart_button_rect, "Play Again", self.manager.ui_manager, anchors={'center': 'center'})
    
    def render(self):
        self.manager.screen.fill("brown1") # its a reddish color
        self.manager.ui_manager.draw_ui(self.manager.screen)

    def handle_events(self, events: list[pg.event.Event]):
        for event in events:
            self.manager.ui_manager.process_events(event)

            if event.type == pgui.UI_BUTTON_PRESSED:
                if event.ui_element == self.restart_button:
                    self.manager.go_to(scenes.title.TitleScene(self.manager))

    def on_exit(self):
        self.game_over_text.kill()
        self.restart_button.kill()
    
    def update(self, dt: int | float):
        self.manager.ui_manager.update(dt)
