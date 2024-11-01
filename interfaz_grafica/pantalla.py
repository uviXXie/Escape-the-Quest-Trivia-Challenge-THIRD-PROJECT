import pygame
import constantes
from personajes import Gallina
from obstaculos import obstaculos

pygame.init()
pygame.mixer.init()


pygame.mixer.music.load("interfaz_grafica/assets/audio/audio_for_third_project.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 

pause = False

def scale_img(image, scale):
    """Imagen Scale

    Args:
        image (png): the image
        scale (int): image scale

    Returns:
        png: the image with the new scale
    """
    w, h = image.get_width(), image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image


animations = []
for i in range(4):
    img = pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png")
    img = scale_img(img, constantes.SCALA_CHARACTER)
    animations.append(img)


player = Gallina(50, 50, animations)
tronco_image = pygame.image.load("interfaz_grafica/assets/images/obstacles/tronco.png")
tronco_obstacle = obstaculos(0,200,tronco_image)

window = pygame.display.set_mode((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Escape the Quest: Trivia Challenge")


icon = pygame.image.load("interfaz_grafica/chicken.png")
pygame.display.set_icon(icon)

move_up = move_down = move_right = move_left = False

clock = pygame.time.Clock()
run = True

while run:

    

    clock.tick(constantes.FPS)
    window.fill(constantes.BG_COLOR)

    # Movement deltas
    delta_x, delta_y = 0, 0
    if move_right:
        delta_x = 5
    if move_left:
        delta_x = -5
    if move_up:
        delta_y = -5
    if move_down:
        delta_y = 5

    player.update()
    player.movement(delta_x, delta_y)
    player.draw_chicken(window)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_p:  
                pause = not pause
                pygame.mixer.music.set_volume(0.1 if pause else 0.5)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                move_down = False

    pygame.display.update()

pygame.quit()
