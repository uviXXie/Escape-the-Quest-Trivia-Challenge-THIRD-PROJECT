import pygame
import constantes
from personajes import Gallina
from obstaculos import Obstaculos  # Cambia el nombre a Obstaculos

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("interfaz_grafica/assets/audio/audio_for_third_project.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 

pause = False

def scale_img(image, scale):
    """Escala la imagen a un nuevo tamaño."""
    w, h = image.get_width(), image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

def handle_events():
    """Maneja eventos de teclado y cierre."""
    global move_left, move_right, move_up, move_down, run, pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_p:
                pause = not pause
                pygame.mixer.music.set_volume(0.1 if pause else 0.5)
            handle_keydown(event.key)
        if event.type == pygame.KEYUP:
            handle_keyup(event.key)

def handle_keydown(key):
    """Maneja las teclas presionadas."""
    global move_left, move_right, move_up, move_down
    if key in (pygame.K_a, pygame.K_LEFT):
        move_left = True
    if key in (pygame.K_d, pygame.K_RIGHT):
        move_right = True
    if key in (pygame.K_w, pygame.K_UP):
        move_up = True
    if key in (pygame.K_s, pygame.K_DOWN):
        move_down = True

def handle_keyup(key):
    """Manages the keys unpressed

    Args:
        key: key being unpressed
    """
    global move_left, move_right, move_up, move_down
    if key in (pygame.K_a, pygame.K_LEFT):
        move_left = False
    if key in (pygame.K_d, pygame.K_RIGHT):
        move_right = False
    if key in (pygame.K_w, pygame.K_UP):
        move_up = False
    if key in (pygame.K_s, pygame.K_DOWN):
        move_down = False


animations = [scale_img(pygame.image.load(f"interfaz_grafica/assets/images/characters/gallina/chicken({i}).png"), constantes.SCALA_CHARACTER) for i in range(4)]
player = Gallina(50, 50, animations)

tronco_image = scale_img(pygame.image.load("interfaz_grafica/assets/images/obstacles/tronco.png"),constantes.SCALA_TRONCO)
tronco_obstacle = Obstaculos(0, 200, tronco_image)


window = pygame.display.set_mode((constantes.WIDHT_SCREEN, constantes.HEIGHT_SCREEN))
pygame.display.set_caption("Escape the Quest: Trivia Challenge")

icon = pygame.image.load("interfaz_grafica/chicken.png")
pygame.display.set_icon(icon)

move_up = move_down = move_right = move_left = False

clock = pygame.time.Clock()
run = True


while run:

    clock.tick(constantes.FPS)
    window.fill(constantes.BLACK_COLOR)


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

    tronco_obstacle.draw(window)

    handle_events()

    pygame.display.update()




pygame.quit()
