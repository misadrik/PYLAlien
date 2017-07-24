import sys

import pygame

def key_down_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



#watch the keyboad and mouse
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            key_down_events(event,ship)

        elif event.type ==pygame.KEYUP:
            key_up_events(event,ship)

#update the screen
def update_screen(ai_settings,screen,ship):
    
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #display the screen
    pygame.display.flip()

