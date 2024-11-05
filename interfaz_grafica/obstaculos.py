import threading
import time
import pygame
import constantes

class Obstaculos:
    def __init__(self, x, y, image) -> None:
        self.shape = pygame.Rect(x, y, constantes.TRONCO_WIDTH, constantes.TRONCO_HEIGHT)
        self.image = image
        self.move_speed = 5
        self.moving_right = True
        self.pause = False  
        self.moving = True  
        self.flip = False  

        self.thread = threading.Thread(target=self.move_image)
        self.thread.daemon = True  
        self.thread.start()

    def move_image(self):
        while self.moving:
            if not self.pause:
               
                if self.moving_right:
                    self.shape.x += self.move_speed
                    if self.shape.right >= constantes.WIDHT_SCREEN:
                        self.moving_right = False
                        self.flip = not self.flip  
                else:
                    self.shape.x -= self.move_speed
                    if self.shape.left <= 0:
                        self.moving_right = True
                        self.flip = not self.flip  

            time.sleep(0.02)  

    def toggle_pause(self):
        """Alterna el estado de pausa para el movimiento del obstáculo."""
        self.pause = not self.pause

    def stop(self):
        """Detiene el movimiento y cierra el hilo."""
        self.moving = False
        self.thread.join()

    def draw(self, screen):
        """Dibuja el obstáculo, con flip en función de la dirección horizontal."""
        pygame.draw.rect(screen,constantes.TRONCO_COLOR,self.shape,1)
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.shape)