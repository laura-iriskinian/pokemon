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

        # create button objects
        self.attack_button = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_top, self.window.sx_button, self.window.sy_button)
        self.run_button = pygame.Rect(self.window.px_pannel_left,self.window.py_rectangle_middle,self.window.sx_button,self.window.sy_button)
        self.change_pokemon_button = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_bottom,self.window.sx_button,self.window.sy_button)
        
        self.buttons = (self.attack_button,self.run_button,self.change_pokemon_button)
        self.total_buttons = len(self.buttons)

        self.selected_position = 1

        # pokemon object
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

    def draw_background_fight(self):
        """function to drawing background"""
        self.window.screen.blit(self.background,(0,0))

    def select_menu_button(self):
        """method to show which button is selected"""

        for position, button in enumerate(self.buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button, 3)

    def draw_xp_bar(self):
        bar_rect = pygame.Rect(160, 160, 200, 10)
        pygame.draw.rect(self.window.screen, self.window.BLACK, bar_rect, 2)

        xp_ratio = self.pokemon_player.xp / self.pokemon_player.xp_to_next_level
        fill_width = int(200*xp_ratio)
        if fill_width > 0:
            fill_rect = pygame.Rect(161, 161, fill_width, 7)
            pygame.draw.rect(self.window.screen, self.window.BLUE, fill_rect)

    def draw_stats(self):
        xp_text = self.window.text_font_hp_opponent.render(f"XP: {self.pokemon_player.xp}/{self.pokemon_player.xp_to_next_level} Level : {self.pokemon_player.level}", True, self.window.WHITE)
        self.window.screen.blit(xp_text, (160, 180))
        

    def handle_events(self):   
        """method to handle menu events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.selected_position = (self.selected_position % self.total_buttons) +1  
                if event.key == K_UP:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1

                if event.key == K_RETURN:
                    if self.selected_position == 1 :
                        self.trainer_attack()
                    else:
                        return "fight"
        return "fight"

    def trainer_attack(self):
        """link with handle_events = player attack and opponent attack"""
        # player attack 
        self.pokemon_opponent[0].player_attack()

        # if pokemon life opponnent = 0 -> replace a pokemon oponant
        if self.pokemon_opponent[0].pokemon_opponent_life <=0:
            self.pokemon_player.win_battle()
            self.pokemon_opponent.append(Pokemon())
            del self.pokemon_opponent[0]

        # opponent attack
        self.pokemon_player.opponent_attack()

        # reset background
        self.draw_background_fight()

        # # draw pokemons 
        self.pokemon_player.draw_pokemon_player()
        self.pokemon_opponent[0].draw_pokemon_opponent()
        
        # panel 
        self.draw_panel()

        # text lifes
        self.pokemon_opponent[0].draw_pokemon_opponent_hp()
        self.pokemon_player.draw_pokemon_player_hp()


    def start_fight(self):

        # draw background
        self.draw_background_fight()

        # draw pokemons
        self.pokemon_opponent[0].draw_pokemon_opponent_hp()
        self.pokemon_player.draw_pokemon_player()
        self.pokemon_opponent[0].draw_pokemon_opponent()
        self.pokemon_player.draw_pokemon_player_hp()
        self.draw_stats()
        self.draw_xp_bar()

        # draw bottom panel 
        self.draw_panel()
        self.select_menu_button()

        # select action
        new_state = self.handle_events()
        return new_state