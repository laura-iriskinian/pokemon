from models.window import Window
import pygame
from pygame.locals import *
import json

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    pokedex = json.load(file)

class Connect_player():
    def __init__(self):
        #background
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.current_state = "connect_player"

        #button to select player
        self.button_select_player = []
        self.player_list = self.get_player_list()
        self.total_buttons_select_player = len(self.player_list)
        self.position_player = self.get_position_player()
        self.selected_position_select_player = 1

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))
        self.window.draw_text("Select player:",self.window.text_font_menu,self.window.BLACK,300,20) 

    def get_player_list(self):

        with open("models/pokedex.json", "r", encoding = "utf-8") as file:
            pokedex = json.load(file)

        self.player_list = []
        for self.player_name in pokedex["players"]:
            self.player_list.append(self.player_name["player_name"])
        

        self.total_buttons_select_player = len(self.player_list)

        return self.player_list
    
    def get_position_player(self):

        self.position_player = []
        for position, player in enumerate(self.player_list,1):
            self.position_player.append(position)
        return self.position_player

    def draw_player_list(self):

        self.button_select_player.clear()

        #column1
        position_x = 60
        position_y = 90
        self.player_list = self.get_player_list()
        for self.player_name in self.player_list:
            
            self.player_name_img = self.window.create_text_image(self.player_name, self.window.text_font_battle, self.window.BLACK)
            rect_player_sprite = self.player_name_img.get_rect()
            rect_player_sprite.topleft = (position_x,position_y)

            self.button_select_player.append(rect_player_sprite)
            self.window.screen.blit(self.player_name_img, rect_player_sprite)
            position_y += 40

        return self.button_select_player    

    def select_player_name(self):

        self.button_select_player = self.draw_player_list()
        for position, self.player_name_button in enumerate(self.button_select_player,1):
            if position == self.selected_position_select_player:
                pygame.draw.rect(self.window.screen, self.window.GREY, self.player_name_button, 2)

    def handle_events_connect_player(self):
        """method to handle events on the connect player screen"""

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "player_menu"  
                
                if event.key == K_DOWN:
                    if self.selected_position_select_player != self.total_buttons_select_player:
                        self.selected_position_select_player += 1
                    else:
                        self.selected_position_select_player = self.total_buttons_select_player
                elif event.key == K_UP:
                    if self.selected_position_select_player != 1:
                        self.selected_position_select_player -=1
                    else:
                        self.selected_position_select_player = 1

                if event.key == K_RETURN:

                        return "game_menu"

        return "connect_player"      

    def connect_player(self):

        self.get_player_list()  

        #set the scene
        self.draw_background() 
        self.draw_player_list() 
        self.select_player_name()  
        #handle events 
        new_state = self.handle_events_connect_player()
        return new_state