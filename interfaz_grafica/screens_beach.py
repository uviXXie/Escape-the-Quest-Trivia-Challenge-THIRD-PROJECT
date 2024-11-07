import pygame
import constantes
from gallina import Gallina
from obstaculos import Obstaculos
from fondo import Background
import sys
from screen_manager import Screen
from screens_city import scale_img


class BeachEasyScreen(Screen):
    """
    Represents the easy level of the beach screen in the game.

    Args:
        screen_manager (ScreenManager): Manages transitions between game screens.
    """

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        # Load and set up the background
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/beach.png")
        self.background = Background(bg)

        # Load player animations
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Load and create obstacles
        cangrejo_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/cangrejo.png"), constantes.SCALA_CANGREJO_EASY)
        self.crab_obstacle = Obstaculos(0, 90, cangrejo_image, 5, constantes.CANGREJO_WIDTH_EASY, constantes.CANGREJO_HEIGHT_EASY)
        self.crab_obstacle_2 = Obstaculos(200, 220, cangrejo_image, 7, constantes.CANGREJO_WIDTH_EASY, constantes.CANGREJO_HEIGHT_EASY)
        self.crab_obstacle_3 = Obstaculos(760, 320, cangrejo_image, 8, constantes.CANGREJO_WIDTH_EASY, constantes.CANGREJO_HEIGHT_EASY)
        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles player events on the screen.

        Args:
            events (list): List of Pygame events to process.
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
        Manages player movement based on key presses.

        Args:
            key (int): Key code of the pressed key.
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
        Stops player movement when keys are released.

        Args:
            key (int): Key code of the released key.
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
        Updates player and obstacles positions, checks for collisions, 
        and transitions screens based on conditions.
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

        # Update obstacles
        self.crab_obstacle.update()
        self.crab_obstacle_2.update()
        self.crab_obstacle_3.update()

        # Collision detection
        if (self.player.shape.colliderect(self.crab_obstacle.shape) or
            self.player.shape.colliderect(self.crab_obstacle_2.shape) or
            self.player.shape.colliderect(self.crab_obstacle_3.shape)):
            self.screen_manager.set_current_screen("game_over")

        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("space_hard")  # Trivia screen transition

    def render(self, screen):
        """
        Renders background, player, and obstacles on the screen.

        Args:
            screen (Surface): Surface to draw the screen contents.
        """
        self.background.draw(screen)
        self.player.draw(screen)
        self.crab_obstacle.draw(screen) 
        self.crab_obstacle_2.draw(screen)
        self.crab_obstacle_3.draw(screen)


class BeachHardScreen(Screen):
    """
    Represents the hard level of the beach screen in the game.

    Args:
        screen_manager (ScreenManager): Manages transitions between game screens.
    """

    def __init__(self, screen_manager):
        self.screen_manager = screen_manager

        # Load and set up the background
        bg = pygame.image.load("interfaz_grafica/assets/images/scenarios/beach.png")
        self.background = Background(bg)

        # Load player animations
        animations = [
            scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER)
            for i in range(4)
        ]
        self.player = Gallina(400, 40, animations)

        # Load and create obstacles
        cangrejo_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/cangrejo.png"), constantes.SCALA_CANGREJO_HARD)
        self.crab_obstacle = Obstaculos(0, 90, cangrejo_image, 5, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)
        self.crab_obstacle_2 = Obstaculos(200, 175, cangrejo_image, 7, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)
        self.crab_obstacle_3 = Obstaculos(800, 130, cangrejo_image, 6, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)
        self.crab_obstacle_4 = Obstaculos(500, 270, cangrejo_image, 3, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)
        self.crab_obstacle_5 = Obstaculos(800, 230, cangrejo_image, 7, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)
        self.crab_obstacle_6 = Obstaculos(760, 330, cangrejo_image, 8, constantes.CANGREJO_WIDTH_HARD, constantes.CANGREJO_HEIGHT_HARD)

        self.move_up = self.move_down = self.move_left = self.move_right = False

    def handle_events(self, events):
        """
        Handles player events on the screen.

        Args:
            events (list): List of Pygame events to process.
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
        Manages player movement based on key presses.

        Args:
            key (int): Key code of the pressed key.
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
        Stops player movement when keys are released.

        Args:
            key (int): Key code of the released key.
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
        Updates player and obstacles positions, checks for collisions, 
        and transitions screens based on conditions.
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

        # Update obstacles
        self.crab_obstacle.update()
        self.crab_obstacle_2.update()
        self.crab_obstacle_3.update()
        self.crab_obstacle_4.update()
        self.crab_obstacle_5.update()
        self.crab_obstacle_6.update()

        # Collision detection
        if (self.player.shape.colliderect(self.crab_obstacle.shape) or
            self.player.shape.colliderect(self.crab_obstacle_2.shape) or
            self.player.shape.colliderect(self.crab_obstacle_3.shape) or
            self.player.shape.colliderect(self.crab_obstacle_4.shape) or
            self.player.shape.colliderect(self.crab_obstacle_5.shape) or
            self.player.shape.colliderect(self.crab_obstacle_6.shape)):
            self.screen_manager.set_current_screen("game_over")

        if self.player.shape.bottom >= constantes.HEIGHT_SCREEN:
            self.screen_manager.set_current_screen("blank_screen")  # Trivia screen transition

    def render(self, screen):
        """
        Renders background, player, and obstacles on the screen.

        Args:
            screen (Surface): Surface to draw the screen contents.
        """
        self.background.draw(screen)
        self.player.draw(screen)
        self.crab_obstacle.draw(screen)
        self.crab_obstacle_2.draw(screen)
        self.crab_obstacle_3.draw(screen)
        self.crab_obstacle_4.draw(screen)
        self.crab_obstacle_5.draw(screen)
        self.crab_obstacle_6.draw(screen)

