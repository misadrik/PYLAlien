import sys 
import pygame

def run_game():
    #init and creat a screen object
    pygame.init() 
    screen = pygame.display.set_mode((720,640))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230,230,230) #set the background color
    
    while True:
        #watch the keyboad and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # refill the screen everytimegit remote add origin git@github.com:qy19941014/PYLAlien.git        
        screen.fill(bg_color)

        #display the screen
        pygame.display.flip()

run_game()
