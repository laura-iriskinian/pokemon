
from models.window import Window

import json
import pygame
from pygame.locals import *

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

class Pokedex():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "pokedex"

        #  button for add_pokemon
        self.buttons_add_pokemon = []
        self.pokemon_in_pokedex_list = self.get_pokemon_selected_sprite_list()
        self.total_buttons_add_pokemon = len(self.pokemon_selected_sprite_list)+1
        self.position_pokemon_sprite = self.get_position_pokemon_list()
        self.selected_position_add_pokemon = 0


    def get_pokemon_selected_sprite_list(self):

        with open("models/pokedex.json", "r", encoding = "utf-8") as file:
            data = json.load(file)

        self.pokemon_selected_sprite_list = []
        for player in data["players"]:
                if player["player_name"] == "player1":
                    for pokemon in player["pokedex"]:
                        pokemon_sprite = pokemon["sprite"]
                        pokemon_sprite_img = pygame.image.load(pokemon_sprite).convert_alpha()
                        if pokemon["selected"] == False:
                            pokemon_sprite_img.set_alpha(128)   
                        self.pokemon_selected_sprite_list.append(pokemon_sprite_img)

        return self.pokemon_selected_sprite_list

    def selected_pokemon(self,player_index,position_pokemon):

        with open("models/pokedex.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        player = data["players"][player_index]

        for pokemon in player["pokedex"]:
            pokemon["selected"] = False

        pokemon = player["pokedex"][position_pokemon]
        pokemon["selected"] = False

        pokemon["selected"] = not pokemon["selected"]

        with open("models/pokedex.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        self.pokemon_in_pokedex_list = self.get_pokemon_selected_sprite_list()

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))


    def draw_background_add_pokemon(self):

        background_add_pokemon = pygame.Rect(10,10,self.window.screen_width-20,self.window.screen_height-20)
        pygame.draw.rect(self.window.screen,self.window.BLUE,background_add_pokemon)
        pygame.draw.rect(self.window.screen,self.window.GREY,background_add_pokemon,4)
        self.window.draw_text("Pokemon in pokedex :",self.window.text_font_menu_battle,self.window.WHITE,20,20)

    def get_position_pokemon_list(self):
        self.position_pokemon_sprite = []
        for position,sprite in enumerate(self.pokemon_selected_sprite_list):
            self.position_pokemon_sprite.append(position)

        return self.position_pokemon_sprite

    def draw_pokemons_add_pokemon(self):
        
# line 1
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon_in_pokedex_list):
            if position_list <= 8:

                rect_pokemon_sprite = sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,100)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(sprite,rect_pokemon_sprite)
                position_x += 83
# # line 2
#         position_x = 60
#         for position_list, sprite in enumerate(self.pokemon_availability_sprite_list):
#             if position_list >= 9 and position_list <= 17:

#                 rect_pokemon_sprite = sprite.get_rect()
#                 rect_pokemon_sprite.center = (position_x,190)

#                 self.buttons_add_pokemon.append(rect_pokemon_sprite)
#                 self.window.screen.blit(sprite,rect_pokemon_sprite)
#                 position_x += 83
# # line 3
#         position_x = 60
#         for position_list, sprite in enumerate(self.pokemon_availability_sprite_list):
#             if position_list >= 18 and position_list <= 26:

#                 rect_pokemon_sprite = sprite.get_rect()
#                 rect_pokemon_sprite.center = (position_x,290)

#                 self.buttons_add_pokemon.append(rect_pokemon_sprite)
#                 self.window.screen.blit(sprite,rect_pokemon_sprite)
#                 position_x += 83
# # line 4
#         position_x = 60
#         for position_list, sprite in enumerate(self.pokemon_availability_sprite_list):
#             if position_list >= 27 and position_list <= 35:

#                 rect_pokemon_sprite = sprite.get_rect()
#                 rect_pokemon_sprite.center = (position_x,390)

#                 self.buttons_add_pokemon.append(rect_pokemon_sprite)
#                 self.window.screen.blit(sprite,rect_pokemon_sprite)
#                 position_x += 83
# # line 5
#         position_x = 60
#         for position_list, sprite in enumerate(self.pokemon_availability_sprite_list):
#             if position_list >= 35 and position_list <= 41:

#                 rect_pokemon_sprite = sprite.get_rect()
#                 rect_pokemon_sprite.center = (position_x,490)

#                 self.buttons_add_pokemon.append(rect_pokemon_sprite)
#                 self.window.screen.blit(sprite,rect_pokemon_sprite)
#                 position_x += 83

        return self.buttons_add_pokemon

    def select_add_pokemon(self):

        for position,sprite in enumerate(self.buttons_add_pokemon):
            if position == self.selected_position_add_pokemon:
                pygame.draw.rect(self.window.screen, self.window.GREY, sprite, 3)


    def handle_envent_pokedex(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #handle events based on the type of menu

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if self.selected_position_add_pokemon % 9 != 8 and self.selected_position_add_pokemon < self.total_buttons_add_pokemon - 1:
                        self.selected_position_add_pokemon += 1
                if event.key == K_LEFT:
                    if self.selected_position_add_pokemon % 9 != 0:
                        self.selected_position_add_pokemon -= 1
                if event.key == K_DOWN:
                    if self.selected_position_add_pokemon + 9 < self.total_buttons_add_pokemon:
                        self.selected_position_add_pokemon += 9
                if event.key == K_UP:
                    if self.selected_position_add_pokemon - 9 >= 0:
                        self.selected_position_add_pokemon -= 9

                if event.key == K_RETURN:
                    if  self.selected_position_add_pokemon in self.position_pokemon_sprite:
                        self.selected_pokemon(0, self.selected_position_add_pokemon)
                        return "pokedex"
                    
                
                if event.key == K_ESCAPE:
                    return "game_menu"
                
        return "pokedex"

    # def activate_pokemon(self,position):


    def start_pokedex_menu(self):

        self.draw_background()
        self.draw_background_add_pokemon()
        self.draw_pokemons_add_pokemon()
        self.select_add_pokemon()



        new_state = self.handle_envent_pokedex()
        return new_state

