import pygame
import constantes

class Gallina:
    """The Gallina class represents the first character: a chicken :)"""

    def __init__(self, x, y, animations) -> None:
        """Constructor for the Gallina class.

        Args:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
            image (pygame.Surface): Image of the chicken.
        """

        self.shape = pygame.Rect(0, 0, constantes.GALLINA_HEIGHT, constantes.GALLINA_WIDTH)
        self.shape.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks() #se almacena el tiempo en milisegundos
        self.image = animations[self.frame_index]
        self.animations = animations
        self.flip = False


    def uptade(self):
        animation_cooldown = 100
        self.image = self.animations[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.frame_index = self.frame_index + 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animations):
                self.frame_index = 0 
            else:
                pass


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
