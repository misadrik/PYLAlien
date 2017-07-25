class Settings():
    'define all the related class'
    def __init__(self):
        #init all the settings
        self.screen_width = 720
        self.screen_height = 640
        self.bg_color = (230,230,230)

        # the speed of ship's move
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
