import pygame
from pathlib import Path

class BaseScene:

    __CURRENT_DIR = Path(__file__).resolve().parent
    __ASSET_IMG_DIR = __CURRENT_DIR.parent / "assets" / "img" 

    def __init__(self, background_img: str):
        background_path_img_full_path = self.__ASSET_IMG_DIR / background_img
        background = pygame.image.load(background_path_img_full_path).convert() 
        self.__scaled_background = pygame.transform.scale(background, (1024, 768))

    def load_background(self, screen) -> None:
        screen.blit(self.__scaled_background , (0, 0))