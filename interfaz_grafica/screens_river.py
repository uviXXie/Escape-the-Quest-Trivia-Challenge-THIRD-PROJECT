import pygame
import constantes
from gallina import Gallina
from obstaculos import Obstaculos
from fondo import Background
import sys
from screen_manager import Screen
from screens_city import scale_img
# Definimos la función scale_img


# class StartScreen(Screen):
#     def __init__(self, screen_manager):
#         self.screen_manager = screen_manager

#     def handle_events(self, events):
#         for event in events:
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     # Transición a la pantalla de nivel fácil
#                     self.screen_manager.set_current_screen("farm_easy")
                    

#     def render(self, screen):
#         screen.fill((255, 255, 255))
#         font = pygame.font.Font(None, 74)
#         text = font.render("Press ENTER to Start", True, (0, 0, 0))
#         screen.blit(text, (constantes.WIDHT_SCREEN // 2 - text.get_width() // 2,
#                            constantes.HEIGHT_SCREEN // 2 - text.get_height() // 2))

class RiverEasyScreen(Screen):
    """
    Screen class for the easy river level where the player controls a character (Gallina) 
    avoiding obstacles (troncos).
    """
    def __init__(self, screen_manager):
        """
        Initializes the RiverEasyScreen with background, player, and obstacles.

        Args:
            screen_manager (ScreenManager): The screen manager to handle screen transitions.
        """
        self.screen_manager = screen_manager

        # Load background image for the RiverEasy level
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/river.png")
        self.background = Background(bg)

        # Load animations for the player (Gallina)
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Initialize obstacles (troncos) for this level with images and properties
        tronco_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/tronco.png"), constantes.SCALA_TRONCO_EASY)
        self.tronco_obstacle = Obstaculos(0, 100, tronco_image, 5, constantes.TRONCO_WIDTH_EASY, constantes.TRONCO_HEIGHT_EASY)
        self.tronco_obstacle_2 = Obstaculos(150, 180, tronco_image, 9, constantes.TRONCO_WIDTH_EASY, constantes.TRONCO_HEIGHT_EASY)
        self.tronco_obstacle_3 = Obstaculos(799, 270, tronco_image, 7, constantes.TRONCO_WIDTH_EASY, constantes.TRONCO_HEIGHT_EASY)

        # Movement flags for player controls
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles all events, including user input for movement and quitting the game.

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
        Updates movement flags when a key is pressed.

        Args:
            key (pygame.key): The key that was pressed.
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
        Resets movement flags when a key is released.

        Args:
            key (pygame.key): The key that was released.
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
        Updates the game logic, including player movement, obstacle movement, 
        and collision detection.
        """
        # Update player movement based on input flags
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

        # Update obstacles (troncos)
        self.tronco_obstacle.update()
        self.tronco_obstacle_2.update()
        self.tronco_obstacle_3.update()

        # Check for collisions with obstacles
        if (self.player.shape.colliderect(self.tronco_obstacle.shape) or 
            self.player.shape.colliderect(self.tronco_obstacle_2.shape) or 
            self.player.shape.colliderect(self.tronco_obstacle_3.shape)):
            self.screen_manager.set_current_screen("game_over")  # Transition to game over screen if collision occurs

        # Transition to the harder level when player reaches the bottom of the screen
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("river_hard")  # Transition to harder level

    def render(self, screen):
        """
        Renders the current screen, including background, player, and obstacles.

        Args:
            screen (pygame.Surface): The surface on which to draw the screen.
        """
        # Draw the background, player, and obstacles on the screen
        self.background.draw(screen)
        self.player.draw(screen)
        self.tronco_obstacle.draw(screen)
        self.tronco_obstacle_2.draw(screen)
        self.tronco_obstacle_3.draw(screen)

    

class RiverHardScreen(Screen):
    """
    Screen class for the hard river level, with more obstacles and challenging gameplay.
    """
    def __init__(self, screen_manager):
        """
        Initializes the RiverHardScreen with background, player, and more obstacles.

        Args:
            screen_manager (ScreenManager): The screen manager to handle screen transitions.
        """
        self.screen_manager = screen_manager

        # Load background image for the RiverHard level
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/river.png")
        self.background = Background(bg)

        # Load animations for the player (Gallina)
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Initialize more challenging obstacles (troncos) for the harder level
        tronco_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/tronco.png"), constantes.SCALA_TRONCO_HARD)
        self.tronco_obstacle = Obstaculos(0, 90, tronco_image, 5, constantes.TRONCO_WIDTH_HARD, constantes.TRONCO_HEIGHT_HARD)
        self.tronco_obstacle_2 = Obstaculos(200, 175, tronco_image, 3, constantes.TRONCO_WIDTH_HARD, constantes.TRONCO_HEIGHT_HARD)
        self.tronco_obstacle_3 = Obstaculos(800, 130, tronco_image, 8, constantes.TRONCO_WIDTH_HARD, constantes.TRONCO_HEIGHT_HARD)
        self.tronco_obstacle_4 = Obstaculos(50, 270, tronco_image, 6, constantes.TRONCO_WIDTH_HARD, constantes.TRONCO_HEIGHT_HARD)
        self.tronco_obstacle_5 = Obstaculos(700, 330, tronco_image, 9, constantes.TRONCO_WIDTH_HARD, constantes.TRONCO_HEIGHT_HARD)

        # Movement flags for player controls
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles all events, including user input for movement and quitting the game.

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
        Updates movement flags when a key is pressed.

        Args:
            key (pygame.key): The key that was pressed.
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
        Resets movement flags when a key is released.

        Args:
            key (pygame.key): The key that was released.
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
        Updates the game logic, including player movement, obstacle movement, 
        and collision detection.
        """
        # Update player movement based on input flags
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

        # Update obstacles (troncos)
        self.tronco_obstacle.update()
        self.tronco_obstacle_2.update()
        self.tronco_obstacle_3.update()
        self.tronco_obstacle_4.update()
        self.tronco_obstacle_5.update()

        # Check for collisions with obstacles
        if (self.player.shape.colliderect(self.tronco_obstacle.shape) or 
            self.player.shape.colliderect(self.tronco_obstacle_2.shape) or 
            self.player.shape.colliderect(self.tronco_obstacle_3.shape) or
            self.player.shape.colliderect(self.tronco_obstacle_4.shape) or
            self.player.shape.colliderect(self.tronco_obstacle_5.shape)):
            self.screen_manager.set_current_screen("game_over")  # Transition to game over screen if collision occurs

        # Transition to next level when player reaches the bottom of the screen
        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("end_screen")  # Transition to end screen

    def render(self, screen):
        """
        Renders the current screen, including background, player, and obstacles.

        Args:
            screen (pygame.Surface): The surface on which to draw the screen.
        """
        # Draw the background, player, and obstacles on the screen
        self.background.draw(screen)
        self.player.draw(screen)
        self.tronco_obstacle.draw(screen)
        self.tronco_obstacle_2.draw(screen)
        self.tronco_obstacle_3.draw(screen)
        self.tronco_obstacle_4.draw(screen)
        self.tronco_obstacle_5.draw(screen)
