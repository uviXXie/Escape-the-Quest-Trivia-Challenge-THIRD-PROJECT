import pygame
import constantes

class Gallina:
    """The Gallina class represents the first character: a chicken :)"""

    def __init__(self, x, y, animations) -> None:
        """Constructor for the Gallina class.

        Args:
            x (int): Initial x-coordinate.
            y (int): Initial y-coordinate.
            animations (list): List of animation frames for the chicken.
        """
        self.shape = pygame.Rect(0, 0, constantes.GALLINA_HEIGHT, constantes.GALLINA_WIDTH)
        self.shape.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()  
        self.image = animations[self.frame_index]
        self.animations = animations
        self.flip = False

    def update(self):
        """Updates the animation frame for the chicken based on a cooldown."""
        animation_cooldown = 100
        self.image = self.animations[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animations):
                self.frame_index = 0

    def draw_chicken(self, screen):
        """Draws the chicken on the screen.

        Args:
            screen (pygame.Surface): Surface on which to draw the chicken.
        """
        pygame.draw.rect(screen,constantes.GALLINA_COLOR,self.shape,1)
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.shape)

    def movement(self, delta_x, delta_y):
        """Allows movement for the character with screen boundary checks.

        Args:
            delta_x (int): Movement in the x-axis.
            delta_y (int): Movement in the y-axis.
        """
        if delta_x < 0:
                self.flip = True
        elif delta_x > 0:
                self.flip = False

        new_x = self.shape.x + delta_x
        new_y = self.shape.y + delta_y

     
        if 0 <= new_x <= constantes.WIDHT_SCREEN - self.shape.width:
            self.shape.x = new_x

        if 0 <= new_y <= constantes.HEIGHT_SCREEN - self.shape.height:
            self.shape.y = new_y
    
                
                