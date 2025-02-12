import pygame
from window import Window

class Button:
    def __init__(self, x, y, image):
        
        self.font = self.window.text_font_menu
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.sign_in_img = self.window.draw_text("Sign in", self.window.text_font_menu, self.window.BLACK, 100, 100)

    def create_img(self,text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        self.screen.blit(img,(x,y))

    def draw_button(self):
        self.window.screen_menu.blit(self.image, (self.rect.x, self.rect.y))


new_player_button = Button(100, 100, self.menu.sign_in_button_img)

#sign in button
sign_in_img = font.render("SIGN IN", True, BLACK)
sign_in_button = Button(100, 100, sign_in_img)
#new player button
new_player_img = font.render("NEW PLAYER", True, BLACK)
new_player_button = Button(530, 100, new_player_img)