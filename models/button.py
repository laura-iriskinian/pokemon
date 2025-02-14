from models.window import Window

class Button:
    def __init__(self, x, y, image, window):
        
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.window = window
    
    #draw button on the screen
    def draw_button(self):
        self.window.screen_menu.blit(self.image, (self.rect.x, self.rect.y))