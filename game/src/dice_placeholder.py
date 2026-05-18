import pygame
from pathlib import Path
from game.src.octagon_shape import OctagonShape

class DicePlaceHolder(OctagonShape):

    _WIDTH = 80
    _HEIGHT = 110
    __CORNER_ANGLE = 20
    __BASE_COLOR = "#4b280a"
    __SECONDARY_COLOR = "#261a0d"

    __FONT_SIZE = 24
    __TEXT_COLOR = "#ffffff"

    __CURRENT_DIR = Path(__file__).resolve().parent
    __ASSET_FONTS_DIR = __CURRENT_DIR.parent / "assets" / "fonts" 

    def __init__(self, x: int, y: int):
        super().__init__(
            x=x, 
            y=y,
            width=self._WIDTH,
            height=self._HEIGHT,
            coner_angle=self.__CORNER_ANGLE
        )

        self.__text_surf = None
        self.__text_rect = None

        self.__dice_picked = False
        self.__text = None

        self.__text_font = pygame.font.Font((self.__ASSET_FONTS_DIR / "VCR_OSD_MONO_1.001.ttf"), self.__FONT_SIZE)
        self.set_text(str("?"))


    def draw(self, screen) -> None:
        """Rysuje kwadratowy przycisk ze stałą obwolutą na wskazanym ekranie."""
        pygame.draw.polygon(screen, self.__SECONDARY_COLOR if self.__dice_picked else self.__BASE_COLOR, self._shape_points)
        screen.blit(self.__text_surf, self.__text_rect)

    def set_text(self, text: str) -> None:
        self.__text = text
        self.__text_surf = self.__text_font.render(self.__text, True, self.__TEXT_COLOR)
        self.__text_rect = self.__text_surf.get_rect(center=self.rect.center)

    def toggle_dice_picked(self) -> None:
        self.__dice_picked = True if not self.__dice_picked else False
    
    def unpick_dice(self) -> None:
        self.__dice_picked = False

    def is_picked(self) -> bool:
        return True if self.__dice_picked else False
    
    def get_dice_val(self) -> int:
        return int(self.__text)

