import pygame
from game.src.menu_scene import MenuScene
from game.src.play_board_scene import PlayBoardScene

class GameManager:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Recruitment Poker")

        self.game_window = pygame.display.set_mode((1024, 768))
        self.clock = pygame.time.Clock()

        self.scenes = {
            "MENU": MenuScene,
            "PLAY_GROUND": PlayBoardScene
        }

        self.current_scene = self.scenes["MENU"]()
        self.current_scene.load_background(self.game_window)

    def run(self) -> None:
        running = True
        while running:

            mouse_pos = pygame.mouse.get_pos()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False 
                    break

                next_scene_name = self.current_scene.handle_events(event)
            
                if next_scene_name and next_scene_name in self.scenes:
                    self.current_scene = self.scenes[next_scene_name]()
                    self.current_scene.load_background(self.game_window)
                    break

            self.current_scene.update(mouse_pos)
            self.current_scene.display_conent(self.game_window)

            pygame.display.flip()
            self.clock.tick(60)