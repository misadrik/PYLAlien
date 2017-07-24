import sys

import pygame

from bullet import Bullet
from alien import Alien

def key_down_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


#watch the keyboad and mouse
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            key_down_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            key_up_events(event,ship)

#update the screen
def update_screen(ai_settings,screen,ship,aliens,bullets):
    
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #display the screen
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width 
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    for alien_number in range(0, number_alien_x):
        alien = Alien(ai_settings,screen)

        alien.x = alien.rect.x + alien_number * alien_width * 2
        alien.rect.x = alien.x

        aliens.add(alien)

