import pygame
import constantes
from personajes import Gallina


pygame.init()





def scale_img(image,scale):
    w = image.get_width()
    h = image.get_height()
    new_image = pygame.transform.scale(image,(w*scale,h*scale))
    return new_image

animations =  []
for i in range(0,4):
    img = pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png")
    img = scale_img(img, constantes.SCALA_CHARACTER)
    animations.append(img)


player = Gallina(50, 50,animations)

window = pygame.display.set_mode((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Escape the Quest: Trivia Challenge")

icon = pygame.image.load("interfaz_grafica\chicken.png")
pygame.display.set_icon(icon)



move_up = False
move_down = False
move_right = False
move_left = False


clock = pygame.time.Clock()
run = True 

while run:

    clock.tick(constantes.FPS)
    window.fill(constantes.BG_COLOR)
    
   
    delta_x = 0 
    delta_y = 0
    
    if move_right :
        delta_x = 5
    if move_left:
        delta_x = -5
    if move_up:
        delta_y = -5
    if move_down:
        delta_y = 5

    player.update()

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
            if events.key == pygame.K_LEFT:
                move_left = True
                print('left')
            if events.key == pygame.K_RIGHT:
                move_right = True
                print('Right')
            if events.key == pygame.K_UP:
                move_up = True
                print('Up')
            if events.key == pygame.K_DOWN:
                move_down = True
                print('Down')
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_a:
                move_left = False
            if events.key == pygame.K_d:
                move_right = False
            if events.key == pygame.K_w:
                move_up = False
            if events.key == pygame.K_s:
                move_down = False
            if events.key == pygame.K_LEFT:
                move_left = False
            if events.key == pygame.K_RIGHT:
                move_right = False
            if events.key == pygame.K_UP:
                move_up = False
            if events.key == pygame.K_DOWN:
                move_down = False
               
            

    player.movement(delta_x, delta_y)
    pygame.display.update()

pygame.quit()
