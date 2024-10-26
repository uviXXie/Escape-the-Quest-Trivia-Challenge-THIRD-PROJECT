import pygame
import constantes
from personajes import Gallina

#TOMAR PERSONAJES DE ITCH.IO

pygame.init()

player = Gallina(50, 50)

window = pygame.display.set_mode((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Escape the Quest: Trivia Challenge")

# Definir variables del movimiento
move_up = False
move_down = False
move_right = False
move_left = False


clock = pygame.time.Clock()
run = True 

while run:
    # Establece 60fps
    clock.tick(constantes.FPS)
    window.fill(constantes.BG_COLOR)
    
    # Calcular movimiento del jugador
    delta_x = 0 
    delta_y = 0
    
    if move_right:
        delta_x += 5
    if move_left:
        delta_x -= 5
    if move_up:
        delta_y -= 5
    if move_down:
        delta_y += 5

    player.draw_chicken(window)
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_a:
                move_left = True 
                print("Left")
            if events.key == pygame.K_d:
                move_right = True
                print("Right")
            if events.key == pygame.K_w:
                move_up = True
                print("Up")
            if events.key == pygame.K_s:
                move_down = True
                print("Down")
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_a:
                move_left = False
            if events.key == pygame.K_d:
                move_right = False
            if events.key == pygame.K_w:
                move_up = False
            if events.key == pygame.K_s:
                move_down = False

    player.movement(delta_x, delta_y)
    pygame.display.update()

pygame.quit()
