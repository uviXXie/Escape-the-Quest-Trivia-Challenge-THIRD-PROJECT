import pygame
import constantes

class Background:

    def __init__(self, image_path) -> None:
        try:
            self.image = pygame.image.load(image_path)
        except pygame.error as e:
            print(f"No se pudo cargar la imagen en la ruta: {image_path}. Error: {e}")
            # Aquí puedes cargar una imagen predeterminada o manejar el error de otra manera
            self.image = pygame.Surface((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))  # Superficie en blanco
        self.x = 0
        self.y = 0
        self.shape = pygame.Rect(0, 0, constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    

