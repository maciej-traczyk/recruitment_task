import pygame
from pathlib import Path
from game.src.base_scene import BaseScene
from game.src.menu_button import MenuButton

class MenuScene(BaseScene):

    def __init__(self):
        super().__init__("menu_background.png")

        self.__start_button = MenuButton(
            x = (1024 // 2) - (200 // 2), 
            y = 200,
            text="START"
        )

    def handle_events(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.__start_button.check_click(event.pos):
                return "PLAY_GROUND"

    def update(self, mouse_pos) -> None:
        self.__start_button.change_bg_color(mouse_pos)

    def display_conent(self, screen) -> None:
        self.__start_button.draw(screen)