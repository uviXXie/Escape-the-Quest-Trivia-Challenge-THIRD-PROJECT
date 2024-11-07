import pygame
import pygame.mixer
import constantes
from screen_manager import ScreenManager
from screens_city import CityEasyScreen, GameOverScreen , CityHardScreen, BlankScreen
from screens_farm import FarmEasyScreen, FarmHardScreen
from screens_river import RiverEasyScreen, RiverHardScreen
from screens_beach import BeachEasyScreen, BeachHardScreen
from screen_manager import Screen
from screens_space import SpaceEasyScreen, SpaceHardScreen
import sys

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("interfaz_grafica/assets/audio/audio_for_third_project.mp3") 
pygame.mixer.music.play(-1)  
pygame.mixer.music.set_volume(0.3)

icon = pygame.image.load("interfaz_grafica/chicken.png")
pygame.display.set_icon(icon)

class StartScreen(Screen):
    """
    The initial game screen.

    Args:
        screen_manager (ScreenManager): Screen manager to handle screen transitions.
    """

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

    def handle_events(self, events):
        """
        Handles events on the start screen.

        Args:
            events (list): List of Pygame events.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Transition to the desired screen
                    self.screen_manager.set_current_screen("beach_hard")

    def render(self, screen):
        """
        Renders content on the start screen.

        Args:
            screen (Surface): Pygame surface where the screen content is drawn.
        """
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 74)
        text = font.render("Press ENTER to Start", True, (0, 0, 0))
        screen.blit(text, (constantes.WIDHT_SCREEN // 2 - text.get_width() // 2,
                           constantes.HEIGHT_SCREEN // 2 - text.get_height() // 2))


class Game:
    """
    Main game class to manage screens and run the game loop.
    """

    def __init__(self):
        """
        Initializes screens and the ScreenManager.
        """
        self.screen_manager = ScreenManager()

        # Create screens
        start_screen = StartScreen(self.screen_manager)
        city_easy_screen = CityEasyScreen(self.screen_manager)
        city_hard_screen = CityHardScreen(self.screen_manager)
        game_over_screen = GameOverScreen(self.screen_manager)
        blank_screen = BlankScreen(self.screen_manager)
        farm_easy = FarmEasyScreen(self.screen_manager)
        farm_hard  = FarmHardScreen(self.screen_manager)
        river_easy_screen = RiverEasyScreen(self.screen_manager)
        river_hard_screen = RiverHardScreen(self.screen_manager)
        space_easy_screen = SpaceEasyScreen(self.screen_manager)
        space_hard_screen = SpaceHardScreen(self.screen_manager)
        beach_easy_screen = BeachEasyScreen(self.screen_manager)
        beach_hard_screen = BeachHardScreen(self.screen_manager)

        # Register screens
        self.screen_manager.register_screen("start", start_screen)
        self.screen_manager.register_screen("city_easy", city_easy_screen)
        self.screen_manager.register_screen("city_hard", city_hard_screen)
        self.screen_manager.register_screen("farm_easy", farm_easy)
        self.screen_manager.register_screen("farm_hard", farm_hard)
        self.screen_manager.register_screen("river_easy", river_easy_screen)
        self.screen_manager.register_screen("river_hard", river_hard_screen)
        self.screen_manager.register_screen("space_easy", space_easy_screen)
        self.screen_manager.register_screen("space_hard", space_hard_screen)
        self.screen_manager.register_screen("beach_easy", beach_easy_screen)
        self.screen_manager.register_screen("beach_hard", beach_hard_screen)
        self.screen_manager.register_screen("game_over", game_over_screen)
        self.screen_manager.register_screen("blank_screen", blank_screen)  # TRIVIA SCREEN

        self.screen_manager.set_current_screen("start")

    def run(self):
        """
        Runs the main game loop, handles events, updates, and renders the current screen.
        
        Raises:
            RuntimeError: If no initial screen is defined.
        """
        if self.screen_manager.current_screen is None:
            raise RuntimeError("The initial screen is not defined.")

        window = pygame.display.set_mode((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))
        pygame.display.set_caption("Escape the Quest: Trivia Challenge")
        clock = pygame.time.Clock()

        run = True
        while run:
            clock.tick(constantes.FPS)
            window.fill(constantes.BLACK_COLOR)

            events = pygame.event.get()
            self.screen_manager.handle_events(events)

            self.screen_manager.update()
            self.screen_manager.render(window)

            pygame.display.update()


# Initialize the game
if __name__ == "__main__":
    game = Game()
    game.run()
