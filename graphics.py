import pygame

pygame.init()

display_width = 800
display_height = 600
run_game = True

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pokemon")


def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
while True:
    event_handler()
    
    pygame.display.update()