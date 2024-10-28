import pygame
import constantes

class Gallina:
    """The Gallina class represents the first character: a chicken :)"""

    def __init__(self, x, y, image) -> None:
        """Constructor for the Gallina class.

        Args:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
            image (pygame.Surface): Image of the chicken.
        """

        self.shape = pygame.Rect(0, 0, constantes.GALLINA_HEIGHT, constantes.GALLINA_WIDTH)
        self.shape.center = (x, y)
        self.image = image
        self.flip = False

    def draw_chicken(self, screen):
        """Draws the chicken on the screen.

        Args:
            screen (pygame.Surface): Surface on which to draw the chicken.
        """
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)  # Flip based on self.flip value
        screen.blit(imagen_flip, self.shape)
        # pygame.draw.rect(screen, constantes.GALLINA_COLOR, self.shape, 1)  # Optional line to see the rectangle's border

    def movement(self, delta_x, delta_y):
        """Allows movement for the character.

        Args:
            delta_x (int): Movement in the x-axis.
            delta_y (int): Movement in the y-axis.
        """
        if delta_x < 0:
            self.flip = True  
        elif delta_x > 0:
            self.flip = False  
        self.shape.x += delta_x
        self.shape.y += delta_y
