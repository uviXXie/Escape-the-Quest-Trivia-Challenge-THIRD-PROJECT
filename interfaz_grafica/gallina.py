import pygame
import constantes

class Gallina:
    """La clase Gallina representa el personaje principal: una gallina :)"""

    def __init__(self, x, y, animations) -> None:
        self.shape = pygame.Rect(0, 0, constantes.GALLINA_WIDTH, constantes.GALLINA_HEIGHT)
        self.shape.center = (x, y)
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animations[self.frame_index]
        self.animations = animations
        self.flip = False

    def update(self):
        animation_cooldown = 100
        if pygame.time.get_ticks() - self.update_time >= animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_index >= len(self.animations):
                self.frame_index = 0
        self.image = self.animations[self.frame_index]

    def draw(self, screen):
        pygame.draw.rect(screen, constantes.GALLINA_COLOR, self.shape, 1)
        imagen_flip = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(imagen_flip, self.shape)

    def movement(self, delta_x, delta_y):
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
