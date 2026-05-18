import pygame
import dicelib
from game.src.base_scene import BaseScene
from game.src.octagon_button import OctagonButton
from game.src.dice_board import DiceBoard

class PlayBoardScene(BaseScene):

    def __init__(self):
        super().__init__("playboard_background.png")

        self.__end_game_button = OctagonButton(
            x = (1024 // 2) - (200 // 2), 
            y = 20,
            text = "surrender",
            base_color = "#660000",
            hover_color = "#990000",
            border_color = "#000000",
            text_color = "#ffffff"
        )

        self.__enemy_board = DiceBoard(
            x = (1024 // 2) - (700 // 2),
            y =  100
        )

        self.__player_bard = DiceBoard(
            x = (1024 // 2) - (700 // 2),
            y =  350,
            interactive=True
        )

        self.__action_button = OctagonButton(
            x = (1024 // 2) - (200 // 2), 
            y = 700,
            text = "roll",
            base_color = "#1f1204",
            hover_color = "#4b280a",
            border_color = "#341d08",
            text_color = "#ffffff"
        )

        self.__game_stage = 0
        self.__game_stages_handler(self.__game_stage)

    def handle_events(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.__end_game_button.check_click(event.pos):
                return "MENU"
            elif self.__game_stage < 2 and self.__action_button.check_click(event.pos):
                self.__game_stage += 1
                self.__game_stages_handler(self.__game_stage)
            elif self.__game_stage == 1 and self.__player_bard.check_for_dice_click(event.pos):
                self.__player_bard.handle_dice_click(event.pos)
    
    def update(self, mouse_pos) -> None:
        self.__end_game_button.change_bg_color(mouse_pos)

        if self.__game_stage != 2:
            self.__action_button.change_bg_color(mouse_pos)

    def display_conent(self, screen) -> None:
        self.__end_game_button.draw(screen)

        self.__enemy_board.draw(screen)
        self.__player_bard.draw(screen)

        self.__action_button.draw(screen)

    def __game_stages_handler(self, stage: int) -> None:
        match stage:
            case 0:
                self.__enemy_board.roll_and_fillup()
            case 1:
                self.__player_bard.roll_and_fillup()
                self.__action_button.set_text("submit")
            case 2:
                self.__player_bard.look_for_reroll()
                self.__player_bard.unpick_all_dices()
                
                game_res = dicelib.compare(self.__player_bard.get_all_dices_val(), self.__enemy_board.get_all_dices_val())
                
                if game_res.value == 1:
                    self.__action_button.set_text("you won!")
                elif game_res.value == 2:
                    self.__action_button.set_text("you lost!")
                else:
                    self.__action_button.set_text("draw!")    

                self.__end_game_button.set_text("leave")


