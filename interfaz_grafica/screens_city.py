import pygame
import constantes
from gallina import Gallina
from obstaculos import Obstaculos
from fondo import Background
import sys
from screen_manager import Screen

# Defining the scale_img function
def scale_img(image, scale):
    """
    Scales the input image by the given scale factor.
    
    Args:
        image (pygame.Surface): The image to scale.
        scale (float): The scale factor to apply to the image size.
    
    Returns:
        pygame.Surface: The scaled image.
    """
    w, h = image.get_width(), image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

# StartScreen class is commented out

class BlankScreen(Screen):
    """
    A blank screen that fills the entire window with a white color.
    Used for transitions or when the game ends.

    Args:
        screen_manager (ScreenManager): The screen manager responsible for managing screen transitions.
    """
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

    def handle_events(self, events):
        """
        Handles the events for the blank screen.

        Args:
            events (list): List of events to process.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):
        """ 
        Updates the blank screen (no updates needed).
        """
        pass

    def render(self, screen):
        """
        Renders the blank screen.

        Args:
            screen (pygame.Surface): The screen to render the content onto.
        """
        screen.fill((255, 255, 255))  # White background

class GameOverScreen(Screen):
    """
    The game over screen is shown when the player loses the game.
    It provides options to restart or quit the game.

    Args:
        screen_manager (ScreenManager): The screen manager responsible for managing screen transitions.
    """
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

    def handle_events(self, events):
        """
        Handles the events for the game over screen.

        Args:
            events (list): List of events to process.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Restart the game by returning to the start screen
                    self.screen_manager.set_current_screen("start")
                elif event.key == pygame.K_ESCAPE:
                    # Exit the game
                    pygame.quit()
                    sys.exit()

    def render(self, screen):
        """
        Renders the game over screen.

        Args:
            screen (pygame.Surface): The screen to render the content onto.
        """
        screen.fill((0, 0, 0))  # Black background
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(text, (constantes.WIDHT_SCREEN // 2 - text.get_width() // 2,
                           constantes.HEIGHT_SCREEN // 2 - text.get_height() // 2))
        font_small = pygame.font.Font(None, 36)
        text_small = font_small.render("Press ENTER to go back to the start", True, (255, 255, 255))
        screen.blit(text_small, (constantes.WIDHT_SCREEN // 2 - text_small.get_width() // 2,
                                 constantes.HEIGHT_SCREEN // 2 + text.get_height()))

class CityEasyScreen(Screen):
    """
    The 'Easy' level screen where the player controls a chicken character and avoids cars as obstacles.

    Args:
        screen_manager (ScreenManager): The screen manager responsible for managing screen transitions.
    """
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        # Load background and set up obstacles
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/city_road.png")
        self.background = Background(bg)

        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        car_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/car.png"), constantes.SCALA_CAR_EASY)
        self.car_obstacle = Obstaculos(0, 100, car_image, 5, constantes.CAR_WIDTH_EASY, constantes.CAR_HEIGHT_EASY)
        self.car_obstacle_2 = Obstaculos(200, 175, car_image, 2, constantes.CAR_WIDTH_EASY, constantes.CAR_HEIGHT_EASY)
        self.car_obstacle_3 = Obstaculos(90, 350, car_image, 8, constantes.CAR_WIDTH_EASY, constantes.CAR_HEIGHT_EASY)

        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles the events for the easy city level.

        Args:
            events (list): List of events to process.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event.key)

    def handle_keydown(self, key):
        """
        Handles keydown events for movement.

        Args:
            key (pygame.key): The key pressed.
        """
        if key in (pygame.K_a, pygame.K_LEFT):
            self.move_left = True
        if key in (pygame.K_d, pygame.K_RIGHT):
            self.move_right = True
        if key in (pygame.K_w, pygame.K_UP):
            self.move_up = True
        if key in (pygame.K_s, pygame.K_DOWN):
            self.move_down = True

    def handle_keyup(self, key):
        """
        Handles keyup events for movement.

        Args:
            key (pygame.key): The key released.
        """
        if key in (pygame.K_a, pygame.K_LEFT):
            self.move_left = False
        if key in (pygame.K_d, pygame.K_RIGHT):
            self.move_right = False
        if key in (pygame.K_w, pygame.K_UP):
            self.move_up = False
        if key in (pygame.K_s, pygame.K_DOWN):
            self.move_down = False

    def update(self):
        """
        Updates the game state for the easy city level (movement, obstacles, collisions).
        """
        delta_x, delta_y = 0, 0
        if self.move_right:
            delta_x = 5
        if self.move_left:
            delta_x = -5
        if self.move_up:
            delta_y = -5
        if self.move_down:
            delta_y = 5

        self.player.movement(delta_x, delta_y)
        self.player.update()

        # Move obstacles
        self.car_obstacle.update()
        self.car_obstacle_2.update()
        self.car_obstacle_3.update()

        # Check for collisions
        if (self.player.shape.colliderect(self.car_obstacle.shape) or 
            self.player.shape.colliderect(self.car_obstacle_2.shape) or 
            self.player.shape.colliderect(self.car_obstacle_3.shape)):
            self.screen_manager.set_current_screen("game_over")

        # Check if player reaches the bottom of the screen
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("city_hard")

    def render(self, screen):
        """
        Renders the easy city level (background, player, obstacles).

        Args:
            screen (pygame.Surface): The screen to render the content onto.
        """
        self.background.draw(screen)
        self.player.draw(screen)
        self.car_obstacle.draw(screen)
        self.car_obstacle_2.draw(screen)
        self.car_obstacle_3.draw(screen)

class CityHardScreen(Screen):
    """
    The 'Hard' level screen where the player controls a chicken character and avoids multiple car obstacles.

    Args:
        screen_manager (ScreenManager): The screen manager responsible for managing screen transitions.
    """
    def __init__(self, screen_manager):
        """
        Initializes the 'Hard' level screen by setting up background, player, and obstacles.

        Args:
            screen_manager (ScreenManager): The screen manager responsible for managing screen transitions.
        """
        self.screen_manager = screen_manager

        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/city_road.png")
        self.background = Background(bg)

        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        car_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/car.png"), constantes.SCALA_CAR_HARD)
        self.car_obstacle = Obstaculos(0, 90, car_image, 5, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)
        self.car_obstacle_2 = Obstaculos(200, 175, car_image, 2, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)
        self.car_obstacle_3 = Obstaculos(90, 130, car_image, 8, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)
        self.car_obstacle_4 = Obstaculos(50, 270, car_image, 4, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)
        self.car_obstacle_5 = Obstaculos(25, 330, car_image, 6, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)
        self.car_obstacle_6 = Obstaculos(70, 380, car_image, 7, constantes.CAR_WIDTH_HARD, constantes.CAR_HEIGHT_HARD)

        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles the events for the hard city level, including key presses and window events.

        Args:
            events (list): List of events to process.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self.handle_keydown(event.key)
            elif event.type == pygame.KEYUP:
                self.handle_keyup(event.key)

    def handle_keydown(self, key):
        """
        Handles keydown events for movement controls.

        Args:
            key (pygame.key): The key pressed.
        """
        if key in (pygame.K_a, pygame.K_LEFT):
            self.move_left = True
        if key in (pygame.K_d, pygame.K_RIGHT):
            self.move_right = True
        if key in (pygame.K_w, pygame.K_UP):
            self.move_up = True
        if key in (pygame.K_s, pygame.K_DOWN):
            self.move_down = True

    def handle_keyup(self, key):
        """
        Handles keyup events to stop movement.

        Args:
            key (pygame.key): The key released.
        """
        if key in (pygame.K_a, pygame.K_LEFT):
            self.move_left = False
        if key in (pygame.K_d, pygame.K_RIGHT):
            self.move_right = False
        if key in (pygame.K_w, pygame.K_UP):
            self.move_up = False
        if key in (pygame.K_s, pygame.K_DOWN):
            self.move_down = False

    def update(self):
        """
        Updates the game state for the hard city level, including player movement, obstacle movement,
        and collision detection.

        Checks for collisions with obstacles and transitions to the game over screen if a collision occurs.
        If the player reaches the bottom of the screen, transitions to the trivia screen (blank_screen).
        """
        # Movement control for player
        delta_x, delta_y = 0, 0
        if self.move_right:
            delta_x = 5
        if self.move_left:
            delta_x = -5
        if self.move_up:
            delta_y = -5
        if self.move_down:
            delta_y = 5

        self.player.movement(delta_x, delta_y)
        self.player.update()

        # Update obstacles
        self.car_obstacle.update()
        self.car_obstacle_2.update()
        self.car_obstacle_3.update()
        self.car_obstacle_4.update()
        self.car_obstacle_5.update()
        self.car_obstacle_6.update()

        # Collision detection with obstacles
        if (self.player.shape.colliderect(self.car_obstacle.shape) or 
            self.player.shape.colliderect(self.car_obstacle_2.shape) or 
            self.player.shape.colliderect(self.car_obstacle_3.shape) or
            self.player.shape.colliderect(self.car_obstacle_4.shape) or
            self.player.shape.colliderect(self.car_obstacle_5.shape) or 
            self.player.shape.colliderect(self.car_obstacle_6.shape)):
            self.screen_manager.set_current_screen("game_over")

        # Check if player reaches the bottom of the screen
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("blank_screen")  # Transition to trivia screen

    def render(self, screen):
        """
        Renders the hard city level on the screen, including background, player, and obstacles.

        Args:
            screen (pygame.Surface): The screen to render the content onto.
        """
        self.background.draw(screen)
        self.player.draw(screen)
        self.car_obstacle.draw(screen)
        self.car_obstacle_2.draw(screen)
        self.car_obstacle_3.draw(screen)
        self.car_obstacle_4.draw(screen)
        self.car_obstacle_5.draw(screen)
        self.car_obstacle_6.draw(screen)
