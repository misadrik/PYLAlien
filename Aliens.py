import sys 
import pygame
from settings import Settings

def run_game():
    #init and creat a screen object
    pygame.init() 
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #bg_color = (230,230,230) #set the background color
    
    while True:
        #watch the keyboad and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # refill the screen everytimegit remote add origin git@github.com:qy19941014/PYLAlien.git        
        screen.fill(ai_settings.bg_color)

        #display the screen
        pygame.display.flip()

run_game()