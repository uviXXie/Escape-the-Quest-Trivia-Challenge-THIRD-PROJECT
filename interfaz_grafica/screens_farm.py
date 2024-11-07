import pygame
import constantes
from gallina import Gallina
from obstaculos import Obstaculos
from fondo import Background
import sys
from screen_manager import Screen
from screens_city import scale_img
# Defining the scale_img function


class FarmEasyScreen(Screen):
    """
    Easy difficulty level screen for the 'Farm' level.

    This class handles the setup of the screen, background, chicken animations, obstacles, 
    and collision detection for the easy level. It allows the player to move using arrow keys and 
    detects screen transitions when the chicken reaches the bottom or collides with an obstacle.
    """
    
    def __init__(self, screen_manager):
        """
        Initializes the elements for the easy level screen in the farm.

        Args:
            screen_manager (ScreenManager): Screen manager that handles screen transitions.
        """
        self.screen_manager = screen_manager

        # Background setup
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/farm.png")
        self.background = Background(bg)

        # Chicken animations setup
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Tractor obstacle setup
        tracteur_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/tracteur.png"), constantes.SCALA_TRACTEUR_EASY)
        self.tracteur_obstacle = Obstaculos(0, 100, tracteur_image, 5, constantes.TRACTEUR_WITDTH_EASY, constantes.TRACTEUR_HEIGHT_EASY)
        self.tracteur_obstacle_2 = Obstaculos(500, 175, tracteur_image, 2, constantes.TRACTEUR_WITDTH_EASY, constantes.TRACTEUR_HEIGHT_EASY)
        self.tracteur_obstacle_3 = Obstaculos(690, 350, tracteur_image, 8, constantes.TRACTEUR_WITDTH_EASY, constantes.TRACTEUR_HEIGHT_EASY)

        # Player movement flags
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles input events such as key presses and window closing.

        Args:
            events (list): List of Pygame events to be processed.
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
        Handles key press events.

        Args:
            key (pygame.key): The key pressed by the player.
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
        Handles key release events.

        Args:
            key (pygame.key): The key released by the player.
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
        Updates the game state, including player movement, obstacle movement, and collision detection.

        Detects if the player collides with any obstacle or reaches the bottom of the screen to trigger 
        screen transitions.
        """
        # Player movement
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

        # Obstacle movement
        self.tracteur_obstacle.update()
        self.tracteur_obstacle_2.update()
        self.tracteur_obstacle_3.update()

        # Collision detection
        if (self.player.shape.colliderect(self.tracteur_obstacle.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_2.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_3.shape)):
            self.screen_manager.set_current_screen("game_over")

        # Transition to next screen if the player reaches the bottom
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("farm_hard")  # Transition to the next level screen

    def render(self, screen):
        """
        Renders the game elements (background, player, obstacles) onto the screen.

        Args:
            screen (pygame.Surface): The surface to render the game elements.
        """
        # Draw the background
        self.background.draw(screen)
        # Draw the player
        self.player.draw(screen)
        # Draw obstacles
        self.tracteur_obstacle.draw(screen)
        self.tracteur_obstacle_2.draw(screen)
        self.tracteur_obstacle_3.draw(screen)


class FarmHardScreen(Screen):
    """
    Hard difficulty level screen for the 'Farm' level.

    This class handles the setup of the screen, background, chicken animations, obstacles, 
    and collision detection for the hard level. It allows the player to move using arrow keys and 
    detects screen transitions when the chicken reaches the bottom or collides with an obstacle.
    """

    def __init__(self, screen_manager):
        """
        Initializes the elements for the hard level screen in the farm.

        Args:
            screen_manager (ScreenManager): Screen manager that handles screen transitions.
        """
        self.screen_manager = screen_manager

        # Background setup
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/farm.png")
        self.background = Background(bg)

        # Chicken animations setup
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Tractor obstacle setup for the hard level
        tracteur_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/tracteur.png"), constantes.SCALA_TRACTEUR_HARD)
        self.tracteur_obstacle = Obstaculos(0, 90, tracteur_image, 5, constantes.TRACTEUR_WITDTH_HARD, constantes.TRACTEUR_HEIGHT_HARD)
        self.tracteur_obstacle_2 = Obstaculos(200, 175, tracteur_image, 3, constantes.TRACTEUR_WITDTH_HARD, constantes.TRACTEUR_HEIGHT_HARD)
        self.tracteur_obstacle_3 = Obstaculos(760, 130, tracteur_image, 8, constantes.TRACTEUR_WITDTH_HARD, constantes.TRACTEUR_HEIGHT_HARD)
        self.tracteur_obstacle_4 = Obstaculos(800, 270, tracteur_image, 5, constantes.TRACTEUR_WITDTH_HARD, constantes.TRACTEUR_HEIGHT_HARD)
        self.tracteur_obstacle_5 = Obstaculos(25, 330, tracteur_image, 7, constantes.TRACTEUR_WITDTH_HARD, constantes.TRACTEUR_HEIGHT_HARD)
        self.tracteur_obstacle_6 = Obstaculos(580, 380, tracteur_image, 5, constantes.TRONCO_WIDTH_EASY, constantes.TRACTEUR_HEIGHT_HARD)

        # Player movement flags
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles input events such as key presses and window closing.

        Args:
            events (list): List of Pygame events to be processed.
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
        Handles key press events.

        Args:
            key (pygame.key): The key pressed by the player.
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
        Handles key release events.

        Args:
            key (pygame.key): The key released by the player.
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
        Updates the game state, including player movement, obstacle movement, and collision detection.

        Detects if the player collides with any obstacle or reaches the bottom of the screen to trigger 
        screen transitions.
        """
        # Player movement
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

        # Obstacle movement
        self.tracteur_obstacle.update()
        self.tracteur_obstacle_2.update()
        self.tracteur_obstacle_3.update()
        self.tracteur_obstacle_4.update()
        self.tracteur_obstacle_5.update()
        self.tracteur_obstacle_6.update()

        # Collision detection
        if (self.player.shape.colliderect(self.tracteur_obstacle.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_2.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_3.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_4.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_5.shape) or 
            self.player.shape.colliderect(self.tracteur_obstacle_6.shape)):
            self.screen_manager.set_current_screen("game_over")

        # Transition to next screen if the player reaches the bottom
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("farm_hard")  # Transition to the next level screen

    def render(self, screen):
        """
        Renders the game elements (background, player, obstacles) onto the screen.

        Args:
            screen (pygame.Surface): The surface to render the game elements.
        """
        # Draw the background
        self.background.draw(screen)
        # Draw the player
        self.player.draw(screen)
        # Draw obstacles
        self.tracteur_obstacle.draw(screen)
        self.tracteur_obstacle_2.draw(screen)
        self.tracteur_obstacle_3.draw(screen)
        self.tracteur_obstacle_4.draw(screen)
        self.tracteur_obstacle_5.draw(screen)
        self.tracteur_obstacle_6.draw(screen)
