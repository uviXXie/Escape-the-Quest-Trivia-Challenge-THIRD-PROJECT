import pygame
import constantes 

def game_over_screen(screen):
    """Muestra la pantalla de Game Over y espera a que el jugador presione una tecla."""
    font = pygame.font.Font("Berlin Sans FB", 74)  
    small_font = pygame.font.Font("Berlin Sans FB", 36)  
    game_over_text = font.render("Game Over", True, constantes.RED_COLOR)
    retry_text = small_font.render("Presiona cualquier tecla para continuar...", True, constantes.WHITE_COLOR)

   
    game_over_rect = game_over_text.get_rect(center=(constantes.WIDHT_SCREEN // 2, constantes.HEIGHT_SCREEN // 3))
    retry_rect = retry_text.get_rect(center=(constantes.WIDHT_SCREEN // 2, constantes.HEIGHT_SCREEN // 1.8))

    # Pantalla de fondo
    screen.fill(constantes.BLACK_COLOR)
    screen.blit(game_over_text, game_over_rect)
    screen.blit(retry_text, retry_rect)
    pygame.display.flip()



