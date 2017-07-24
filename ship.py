import pygame

class Ship():
  
    def __init__(self,ai_settings,screen):
        self.screen = screen

        self.ai_settings = ai_settings

        #load the ship's img and get it's rectangle
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put the ship in the middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #store a float number in center
        self.center = float(self.rect.centerx)

        #flag for moving left and right continuously
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor

        # update object rect according to center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)


        
