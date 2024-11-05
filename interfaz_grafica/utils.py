import pygame

def scale_img(image, scale):
    """Escala la imagen a un nuevo tamaño."""
    w, h = image.get_width(), image.get_height()
    new_image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return new_image

def manejar_movimiento(player, move_left, move_right, move_up, move_down):
    """Maneja el movimiento del jugador."""
    delta_x, delta_y = 0, 0

    if move_left:
        delta_x = -5
    if move_right:
        delta_x = 5
    if move_up:
        delta_y = -5
    if move_down:
        delta_y = 5

    player.movement(delta_x, delta_y)

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
    """Maneja las teclas soltadas."""
    global move_left, move_right, move_up, move_down
    if key in (pygame.K_a, pygame.K_LEFT):
        move_left = False
    if key in (pygame.K_d, pygame.K_RIGHT):
        move_right = False
    if key in (pygame.K_w, pygame.K_UP):
        move_up = False
    if key in (pygame.K_s, pygame.K_DOWN):
        move_down = False
