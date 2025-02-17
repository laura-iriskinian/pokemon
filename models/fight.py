from models.window import Window
from models.pokemon import Pokemon


import pygame
from pygame.locals import *


class Fight():
    """class to print combat"""
    def __init__(self):

        # background image
        self.window = Window() 
        self.background = pygame.image.load("assets/pictures/background.png").convert_alpha()
        self.position = 1

        self.pokemon_player = Pokemon()
        self.pokemon_opponent = [Pokemon()]



    def draw_panel(self):
        """draw rectangle for bottom panel"""
        # full Rectangle 
        rectangle_left = pygame.Rect(0, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_left)
        rectangle_right = pygame.Rect(self.window.screen_width/2, self.window.screen_height - self.window.bottom_panel, self.window.screen_width / 2, self.window.bottom_panel)
        pygame.draw.rect(self.window.screen, self.window.BLUE, rectangle_right)

        # outline rectangle 
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_left, 3)
        pygame.draw.rect(self.window.screen, self.window.GREY, rectangle_right, 3)

        self.window.draw_text("Attack !",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - self.window.bottom_panel)+6)
        self.window.draw_text("Run ",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - (self.window.bottom_panel - (self.window.bottom_panel/3))))
        self.window.draw_text("Change pokemon",self.window.text_font_menu_battle,self.window.WHITE,50, (self.window.screen_height - (self.window.bottom_panel/3)))

    def select_fight_button(self,position):
        """def to draw panel button : search in dicto the position"""

        rectangle_button_position = {0 : self.rectangle_bottom,
                                    1 : self.rectangle_top, 
                                    2 : self.rectangle_midle, 
                                    3: self.rectangle_bottom, 
                                    4 :self.rectangle_bottom}

        self.rectangle_button = pygame.draw.rect(self.window.screen, 
                                                self.window.GREY, 
                                                rectangle_button_position[position],
                                                3)
        
        pygame.draw.rect(self.window.screen, self.window.GREY, self.rectangle_button, 3)

    def draw_background_fight(self):
        """function to drawing background"""
        self.window.screen.blit(self.background,(0,0))

        # rectangle button to panel : (position x,position y,size x, size y)
        self.rectangle_top = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_top, self.window.sx_button, self.window.sy_button)
        self.rectangle_midle = pygame.Rect(self.window.px_pannel_left,self.window.py_rectangle_middle,self.window.sx_button,self.window.sy_button)
        self.rectangle_bottom = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_bottom,self.window.sx_button,self.window.sy_button)


    def trainer_attack(self):
    # attack
        self.pokemon_opponent[0].player_attack()

        if self.pokemon_opponent[0].pokemon_opponent_life <=0:
            self.pokemon_opponent.append(Pokemon())
            del self.pokemon_opponent[0]

        self.pokemon_player.opponent_attack()

        # reset 
        self.draw_background_fight()
        self.pokemon_player.draw_pokemon_player()
        self.pokemon_opponent[0].draw_pokemon_opponent()
        self.draw_panel()
        self.select_fight_button(1)
        self.pokemon_opponent[0].draw_pokemon_opponent_hp()

        self.pokemon_player.draw_pokemon_player_hp()


    def start_fight(self):

        # draw background
        self.draw_background_fight()

        # draw pokemon
        self.pokemon_opponent[0].draw_pokemon_opponent_hp()
        self.pokemon_player.draw_pokemon_player()
        self.pokemon_opponent[0].draw_pokemon_opponent()
        self.pokemon_player.draw_pokemon_player_hp()

        # draw bottom panel
        self.draw_panel()
        self.select_fight_button(self.position) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if self.position >= 1:
                        self.position += 1
                        self.draw_panel()
                        self.select_fight_button(self.position) 
                    if self.position == 4:
                        self.position -=3
                        self.draw_panel()
                        self.select_fight_button(self.position) 
                if event.key == K_UP:
                    if self.position >= 1:
                        self.position -= 1
                        self.draw_panel()
                        self.select_fight_button(self.position) 
                    if self.position == 0:
                        self.position +=3
                        self.draw_panel()
                        self.select_fight_button(self.position) 
                if event.key == K_RETURN:
                    if self.rectangle_top.colliderect(self.rectangle_button):
                        self.trainer_attack()

