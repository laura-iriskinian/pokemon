from models.window import Window
from models.pokemon import Pokemon

import pygame
from pygame.locals import *


class Starter_choice():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "starter_choice"
        self.pokemon = Pokemon()

        #  button for add_pokemon
        self.buttons_strater_choice = []
        self.total_buttons_starter = 3
        self.position_pokemon_sprite = self.get_position_pokemon_list()
        self.selected_position_add_pokemon = 0

    def draw_background_starter_choice(self):
        x = 80
        y = 120
        width = 180
        height = 300
        
        window_left = pygame.Rect(x,y,width,height)
        window_middle = pygame.Rect(x+(width+50),y,width,height)
        window_right = pygame.Rect(x+(width*2+100),y,width,height)

        self.window.screen.blit(self.background,(0,0))

        pygame.draw.rect(self.window.screen,self.window.BLUE,window_left)
        pygame.draw.rect(self.window.screen,self.window.GREY,window_left,4)

        pygame.draw.rect(self.window.screen,self.window.BLUE,window_middle)
        pygame.draw.rect(self.window.screen,self.window.GREY,window_middle,4)

        pygame.draw.rect(self.window.screen,self.window.BLUE,window_right)
        pygame.draw.rect(self.window.screen,self.window.GREY,window_right,4)

        self.window.draw_text("Choice your starter pokemon :",self.window.text_font_menu,self.window.BLACK,20,20)


    def get_position_pokemon_list(self):
        self.position_pokemon_sprite = []
        for position,sprite in enumerate(self.pokemon.pokemon_starter_list):
            self.position_pokemon_sprite.append(position)

        return self.position_pokemon_sprite

    def draw_pokemons_starter_choice(self):
        
        position_x = 170
        for sprite in self.pokemon.pokemon_starter_list:
                pokemon_sprite_img = pygame.transform.scale(sprite, (sprite.get_width()*3, sprite.get_height()*3))
                rect_pokemon_sprite = pokemon_sprite_img.get_rect()
                rect_pokemon_sprite.center = (position_x,200)
                
                self.buttons_strater_choice.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite_img,rect_pokemon_sprite)
                position_x += 235

        return self.buttons_strater_choice


    def select_add_pokemon(self):

        for position,sprite in enumerate(self.buttons_strater_choice):
            if position == self.selected_position_add_pokemon:
                pygame.draw.rect(self.window.screen, self.window.GREY, sprite, 3)


    def handle_envent_add_pokemon(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #handle events based on the type of menu

            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.selected_position = (self.selected_position % 2) +1 
                
                elif event.key == K_LEFT:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1 

                if event.key == K_RETURN:
                    # if  self.selected_position_add_pokemon in self.position_pokemon_sprite:
                    #     self.pokemon.availability_pokemon(self.selected_position_add_pokemon)

                    #     return "add_pokemon"
                    if self.selected_position_add_pokemon == 3:
                        return "add_pokemon"
                    # else:
                    #     return "game_menu"
                
                if event.key == K_ESCAPE:
                    return "game_menu"
                
        return "add_pokemon"




    def start_starter_choice(self):

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()

        #set the scene
        self.draw_background_starter_choice()
        self.draw_pokemons_starter_choice()
        #handle events

        new_state = "starter_choice"
        return new_state