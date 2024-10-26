import pygame 
import  constantes
class Gallina:
    """The Gallina class is for the first charater: a chicken :) 
    """

    def __init__(self,x,y) -> None:
        """constructor

        Args:
            x (int): cordanate x
            y (int): cordanate y
        """
        self.shape = pygame.Rect(0,0,constantes.GALLINA_HEIGHT,constantes.GALLINA_WIDHT) #meter el tamano a constantes
        self.shape.center = (x,y)


    def draw_chicken(self,screen):
        pygame.draw.rect(screen,constantes.GALLINA_COLOR, self.shape)

    def movement(self,delta_x,delta_y):
        """Allows the movement for the character

        Args:
            delta_x (int): object movement in x
            delta_y (int): object movement in y
        """
        self.shape.x = self.shape.x + delta_x
        self.shape.y = self.shape.y + delta_y