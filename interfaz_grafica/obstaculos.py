import pygame
import constantes

class Obstaculos:
    def __init__(self, x, y, image, speed, width, height):
        self.shape = pygame.Rect(x, y, width, height)
        self.image = image
        self.move_speed = speed
        self.moving_right = True
        self.pause = False
        self.flip = False

    def update(self):
        """Actualizar la posición del obstáculo"""
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

    def set_speed(self, speed):
        """Permite ajustar la velocidad del movimiento del obstáculo."""
        self.move_speed = speed

    def toggle_pause(self):
        """Alterna el estado de pausa para el movimiento del obstáculo."""
        self.pause = not self.pause

    def draw(self, screen):
        """Dibuja el obstáculo, con flip en función de la dirección horizontal."""
        # Dibuja un rectángulo para depuración (opcional)
        pygame.draw.rect(screen, constantes.OBSTACLE_COLOR, self.shape, 1)

        # Dibuja la imagen del obstáculo
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.shape)
