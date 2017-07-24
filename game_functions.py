import sys

import pygame

#watch the keyboad and mouse
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type ==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

#update the screen
def update_screen(ai_settings,screen,ship):
    
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #display the screen
    pygame.display.flip()

