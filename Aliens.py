import sys 
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #init and creat a screen object
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #bg_color = (230,230,230) #set the background color
    
    ship = Ship(screen)#creat a ship 

    while True:
        # #watch the keyboad and mouse
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events()

        # refill the screen everytimegit remote add origin git@github.com:qy19941014/PYLAlien.git        
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        gf.update_screen(ai_settings,screen,ship)

        # #display the screen
        # pygame.display.flip()

run_game()
