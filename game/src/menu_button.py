import pygame
from pathlib import Path

class MenuButton():

    __WIDTH = 200
    __HEIGHT = 50
    __BORDER_THICKNESS = 5
    __FONT_SIZE = 24
    
    __BASE_COLOR = "#1f1204"
    __HOVER_COLOR = "#4b280a"
    __BORDER_COLOR = "#341d08"
    __TEXT_COLOR = "#ffffff"
    
    __CURRENT_DIR = Path(__file__).resolve().parent
    __ASSET_FONTS_DIR = __CURRENT_DIR.parent / "assets" / "fonts" 

    def __init__(self, x : int, y: int, text: str):
        self.__current_color = self.__BASE_COLOR

        self.__rect = pygame.Rect(x, y, self.__WIDTH, self.__HEIGHT)

        self.__text_font = pygame.font.Font((self.__ASSET_FONTS_DIR / "VCR_OSD_MONO_1.001.ttf"), self.__FONT_SIZE)
        self.__text_surf = self.__text_font.render(text, True, self.__TEXT_COLOR)
        self.__text_rect = self.__text_surf.get_rect(center=self.__rect.center)
    
    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.__BORDER_COLOR, self.__rect)
        inner_rect = self.__rect.inflate(-self.__BORDER_THICKNESS * 2, -self.__BORDER_THICKNESS * 2)
        pygame.draw.rect(screen, self.__current_color, inner_rect)
        screen.blit(self.__text_surf, self.__text_rect)

    def change_bg_color(self, mouse_pos) -> None:
        if self.__rect.collidepoint(mouse_pos):
            self.__current_color = self.__HOVER_COLOR
        else:
            self.__current_color = self.__BASE_COLOR

    def check_click(self, mouse_pos) -> bool:
        return self.__rect.collidepoint(mouse_pos)
