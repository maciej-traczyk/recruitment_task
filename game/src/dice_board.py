
import pygame
import dicelib
from functools import wraps
from game.src.dice_placeholder import DicePlaceHolder


class DiceBoard():

    __WIDTH = 700
    __HEIGHT = 200
    __BORDER_THICKNESS = 10
    __BASE_COLOR = "#ffffe6"
    __BORDER_COLOR = "#341d08"

    __DICE_AMOUNT = 5
    __DICE_SPACEING = 50 

    def __init__(self, x: int, y: int, interactive: bool = False):
        self._interactive_mode = interactive
        self.__rect = pygame.Rect(x, y, self.__WIDTH, self.__HEIGHT)
        
        self.__dices = []
        dice_y = self.__rect.y + (self.__HEIGHT // 2) - (DicePlaceHolder._HEIGHT // 2)

        for i in range(self.__DICE_AMOUNT):
            dice_x = (self.__rect.x + self.__DICE_SPACEING) if i == 0 else (self.__dices[i - 1].rect.right + self.__DICE_SPACEING)
            self.__dices.append(DicePlaceHolder(dice_x, dice_y))

    def _require_interactive(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if not self._interactive_mode:
                print("[err]: This method is unavailable for current DiceBoard configuration")
                return None
            return func(self, *args, **kwargs)
        return wrapper
    
    @_require_interactive
    def check_for_dice_click(self, mouse_pos) -> bool:
        for dice in self.__dices:
            if dice.rect.collidepoint(mouse_pos):
                return True
        return False

    @_require_interactive
    def handle_dice_click(self, mouse_pos) -> None:
        [dice.toggle_dice_picked() for dice in self.__dices if dice.rect.collidepoint(mouse_pos)]
                
    @_require_interactive
    def unpick_all_dices(self) -> None:
        [dice.unpick_dice() for dice in self.__dices]

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.__BORDER_COLOR, self.__rect)
        inner_rect = self.__rect.inflate(-self.__BORDER_THICKNESS * 2, -self.__BORDER_THICKNESS * 2)
        pygame.draw.rect(screen, self.__BASE_COLOR, inner_rect)

        for dice in self.__dices:
            dice.draw(screen)

    def roll_and_fillup(self) -> None:
        data = dicelib.roll(self.__DICE_AMOUNT)

        for i in range(self.__DICE_AMOUNT):
            self.__dices[i].set_text(str(data[i]))

    def look_for_reroll(self) -> None:
        idx_to_rerool = []

        for i in range(self.__DICE_AMOUNT):
            if self.__dices[i].is_picked():
                idx_to_rerool.append(i)

        data = dicelib.roll(len(idx_to_rerool))
        for i in range(len(data)):
            self.__dices[idx_to_rerool[i]].set_text(str(data[i]))

    def get_all_dices_val(self) -> list[int]:
        res = []
        for dice in self.__dices:
            res.append(dice.get_dice_val())

        return res
