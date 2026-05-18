import pygame
from pathlib import Path
from game.src.octagon_shape import OctagonShape

class OctagonButton(OctagonShape):

    __WIDTH = 200
    __HEIGHT = 40
    __BORDER_THICKNESS = 6
    __FONT_SIZE = 24
    __CORNER_ANGLE = 10

    __CURRENT_DIR = Path(__file__).resolve().parent
    __ASSET_FONTS_DIR = __CURRENT_DIR.parent / "assets" / "fonts" 

    def __init__(self, x: int, y: int, text: str, base_color: str, hover_color: str, border_color: str, text_color: str):
        super().__init__(
            x=x, 
            y=y,
            width=self.__WIDTH,
            height=self.__HEIGHT,
            coner_angle=self.__CORNER_ANGLE
        )

        self.__base_color = base_color
        self.__hover_color = hover_color
        self.__border_color = border_color
        self.__text_color = text_color

        self.__current_color = self.__base_color

        self.__text_surf = None
        self.__text_rect = None

        self.__text_font = pygame.font.Font((self.__ASSET_FONTS_DIR / "VCR_OSD_MONO_1.001.ttf"), self.__FONT_SIZE)
        self.set_text(text)

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, self.__current_color, self._shape_points)
        pygame.draw.polygon(screen, self.__border_color, self._shape_points, self.__BORDER_THICKNESS)

        screen.blit(self.__text_surf, self.__text_rect)

    def change_bg_color(self, mouse_pos) -> None:
        if self.rect.collidepoint(mouse_pos):
            self.__current_color = self.__hover_color
        else:
            self.__current_color = self.__base_color

    def check_click(self, mouse_pos) -> bool:
        return self.rect.collidepoint(mouse_pos)
    
    def set_text(self, text: str) -> None:
        self.__text_surf = self.__text_font.render(text, True, self.__text_color)
        self.__text_rect = self.__text_surf.get_rect(center=self.rect.center)