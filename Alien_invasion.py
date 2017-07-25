import sys 
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien 

def run_game():
    #init and creat a screen object
    pygame.init()

    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #bg_color = (230,230,230) #set the background color
    
    ship = Ship(ai_settings,screen)#creat a ship 
    bullets = Group()
    #alien = Alien(ai_settings,screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen,ship, aliens)


    while True:
        # #watch the keyboad and mouse
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
       
        gf.update_bullets(bullets)

        # refill the screen everytimegit remote add origin git@github.com:qy19941014/PYLAlien.git        
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # alien.blitme()
        
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # #display the screen
        # pygame.display.flip()

run_game()
