import sys

import pygame

#watch the keyboad and mouse
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#update the screen
def update_screen(ai_settings,screen,ship):
    
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #display the screen
    pygame.display.flip()