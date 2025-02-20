from models.window import Window
from models.pokemon import Pokemon

import pygame
import json
from pygame.locals import *


with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

class Starter_choice():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.current_state = "starter_choice"

        self.x = 80
        self.y = 120
        self.width = 180
        self.height = 300
        
        self.window_left = pygame.Rect(self.x,self.y,self.width,self.height)
        self.window_middle = pygame.Rect(self.x+(self.width+50),self.y,self.width,self.height)
        self.window_right = pygame.Rect(self.x+(self.width*2+100),self.y,self.width,self.height)

        #  buttons
        self.buttons_starter_choice = (self.window_left,self.window_middle,self.window_right)
        self.total_buttons_starter = len(self.buttons_starter_choice)
        self.selected_position = 1
        self.pokemon_sprite = self.get_pokemon_starter_list()

    def get_pokemon_starter_list(self):
        self.pokemon_starter_list = []
        for pokemon in data["pokemon"]:
            pokemon_sprite = pokemon["sprites"]["front"]
            pokemon_sprite_img = pygame.image.load(pokemon_sprite).convert_alpha()
            if pokemon["name"] == "Bulbasaur":
                self.pokemon_starter_list.append(pokemon_sprite_img)
            elif pokemon["name"] == "Charmander":
                self.pokemon_starter_list.append(pokemon_sprite_img)
            elif pokemon["name"] == "Squirtle":
                self.pokemon_starter_list.append(pokemon_sprite_img)
        return self.pokemon_starter_list
    

    def draw_background_starter_choice(self):

        self.window.screen.blit(self.background,(0,0))

        pygame.draw.rect(self.window.screen,self.window.BLUE,self.window_left)
        pygame.draw.rect(self.window.screen,self.window.GREY,self.window_left,4)

        pygame.draw.rect(self.window.screen,self.window.BLUE,self.window_middle)
        pygame.draw.rect(self.window.screen,self.window.GREY,self.window_middle,4)

        pygame.draw.rect(self.window.screen,self.window.BLUE,self.window_right)
        pygame.draw.rect(self.window.screen,self.window.GREY,self.window_right,4)

        self.window.draw_text("Choice your starter pokemon :",self.window.text_font_menu,self.window.BLACK,20,20)


    def draw_pokemons_starter_choice(self):
        
        position_x = 170
        for sprite in self.pokemon_starter_list:
                pokemon_sprite_img = pygame.transform.scale(sprite, (sprite.get_width()*3, sprite.get_height()*3))
                rect_pokemon_sprite = pokemon_sprite_img.get_rect()
                rect_pokemon_sprite.center = (position_x,200)
                
                self.window.screen.blit(pokemon_sprite_img,rect_pokemon_sprite)
                position_x += 235


    def select_starter_choice(self):

        for position,sprite in enumerate(self.buttons_starter_choice,1):
            if position == self.selected_position:
                pygame.draw.rect(self.window.screen, self.window.WHITE, sprite, 4)


    def handle_envent_starter_choice(self):


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # handle events based on the type of menu
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    if self.selected_position != 3:
                        self.selected_position += 1
                        print(f"right : {self.selected_position}")
                    else:
                        self.selected_position = 3
                elif event.key == K_LEFT:
                    if self.selected_position != 1:
                        self.selected_position -=1
                        print(f"left : {self.selected_position}")
                    else:
                        self.selected_position = 1
                if event.key == K_RETURN:

                    if self.selected_position == 1:
                        return "game_menu"
                    if self.selected_position == 2:
                        return "game_menu"
                    if self.selected_position == 3:
                        return "game_menu"

        return "starter_choice"



    def start_starter_choice(self):

        #set the scene
        self.draw_background_starter_choice()
        self.draw_pokemons_starter_choice()
        self.select_starter_choice()

        #handle events
        new_state = self.handle_envent_starter_choice()
        return new_state