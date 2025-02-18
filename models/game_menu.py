import pygame
import pygame.draw_py
from pygame.locals import *
from models.button import Button
from models.pokemon import Pokemon
from models.window import Window

class Game_menu():
    def __init__(self):
        self.window = Window()
        self.background = pygame.image.load("assets/pictures/menu.jpg")
        self.selected_position = 1
        self.current_state = "game_menu"
        self.pokemon = Pokemon()


        self.buttons_add_pokemon = []
        self.total_buttons_add_pokemon = len(self.pokemon.pokemon_sprites_list)+1
        self.position_pokemon_sprite = self.get_position_pokemon_list()
        self.selected_position_add_pokemon = 0

        #Load button images:
        self.resume_game_img = self.window.create_text_image("Resume game", self.window.text_font_menu, self.window.BLACK)
        self.pokedex_img = self.window.create_text_image("Pokedex", self.window.text_font_menu, self.window.BLACK)
        self.add_pokemon_img = self.window.create_text_image("Add pokemon", self.window.text_font_menu, self.window.BLACK)
        self.new_game_img = self.window.create_text_image("New game", self.window.text_font_menu, self.window.BLACK)

        #Create Button objects
        self.resume_game_button = Button(100,100,self.resume_game_img, self.window)
        self.pokedex_button = Button(100,150,self.pokedex_img, self.window)
        self.add_pokemon_button = Button(100,200,self.add_pokemon_img, self.window)
        self.new_game_button = Button(100,250,self.new_game_img, self.window)

        self.buttons = (self.resume_game_button, self.pokedex_button, self.add_pokemon_button, self.new_game_button)
        self.total_buttons = len(self.buttons)

    def draw_background(self):
        """method to draw background"""
        self.window.screen.blit(self.background,(0,0))


    def draw_buttons(self):
        self.resume_game_button.draw_button()
        self.pokedex_button.draw_button()
        self.add_pokemon_button.draw_button()
        self.new_game_button.draw_button()

    #Draw a rectangle around the selected button
    def select_menu_button(self):
        for position, button in enumerate(self.buttons, 1):
            #check if button is selected
            if position == self.selected_position:  
                #draw the rectangle around it
                pygame.draw.rect(self.window.screen, self.window.GREY, button.rect, 3)


    def handle_events_game_menu(self):   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #handle events based on the type of menu

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.selected_position = (self.selected_position % self.total_buttons) +1  
                if event.key == K_UP:
                    self.selected_position = (self.selected_position - 2) % self.total_buttons + 1


                if event.key == K_RETURN:
                    if self.selected_position == 1 :
                        return "fight"  
                    if self.selected_position == 3:
                        return "add_pokemon"
                    else:
                        return "game_menu"


        return "game_menu"


    def start_game_menu(self):

        #set the scene
        self.draw_background()
        self.draw_buttons()
        self.select_menu_button()

        #handle events

        new_state = self.handle_events_game_menu()
        return new_state


    def draw_background_add_pokemon(self):

        background_add_pokemon = pygame.Rect(10,10,self.window.screen_width-20,self.window.screen_height-20)
        pygame.draw.rect(self.window.screen,self.window.BLUE,background_add_pokemon)
        pygame.draw.rect(self.window.screen,self.window.GREY,background_add_pokemon,4)
        self.window.draw_text("Pokemon in the world :",self.window.text_font_menu_battle,self.window.WHITE,20,20)

    def get_position_pokemon_list(self):
        self.position_pokemon_sprite = []
        for position,sprite in enumerate(self.pokemon.pokemon_sprites_list):
            self.position_pokemon_sprite.append(position)

        return self.position_pokemon_sprite

    def draw_pokemons_add_pokemon(self):
        
# line 1
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon.pokemon_sprites_list):
            if position_list <= 8:
                pokemon_sprite = pygame.image.load(sprite).convert_alpha()

                rect_pokemon_sprite = pokemon_sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,100)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite,rect_pokemon_sprite)
                position_x += 83
# line 2
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon.pokemon_sprites_list):
            if position_list >= 9 and position_list <= 17:
                pokemon_sprite = pygame.image.load(sprite).convert_alpha()

                rect_pokemon_sprite = pokemon_sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,190)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite,rect_pokemon_sprite)
                position_x += 83
# line 3
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon.pokemon_sprites_list):
            if position_list >= 18 and position_list <= 26:
                pokemon_sprite = pygame.image.load(sprite).convert_alpha()

                rect_pokemon_sprite = pokemon_sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,290)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite,rect_pokemon_sprite)
                position_x += 83
# line 4
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon.pokemon_sprites_list):
            if position_list >= 27 and position_list <= 35:
                pokemon_sprite = pygame.image.load(sprite).convert_alpha()

                rect_pokemon_sprite = pokemon_sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,390)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite,rect_pokemon_sprite)
                position_x += 83
# line 5
        position_x = 60
        for position_list, sprite in enumerate(self.pokemon.pokemon_sprites_list):
            if position_list >= 35 and position_list <= 41:
                pokemon_sprite = pygame.image.load(sprite).convert_alpha()

                rect_pokemon_sprite = pokemon_sprite.get_rect()
                rect_pokemon_sprite.center = (position_x,490)

                self.buttons_add_pokemon.append(rect_pokemon_sprite)
                self.window.screen.blit(pokemon_sprite,rect_pokemon_sprite)
                position_x += 83

        return self.buttons_add_pokemon

    def select_add_pokemon(self):

        for position,sprite in enumerate(self.buttons_add_pokemon):
            if position == self.selected_position_add_pokemon:
                pygame.draw.rect(self.window.screen, self.window.GREY, sprite, 3)


    def handle_envent_add_pokemon(self):

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

                        return "add_pokemon" 
                    if self.selected_position_add_pokemon == 3:
                        return "add_pokemon"
                    else:
                        return "game_menu"
        return "add_pokemon"

    # def activate_pokemon(self,position):


    def start_add_pokemon(self):

        self.draw_background()
        self.draw_background_add_pokemon()
        self.draw_pokemons_add_pokemon()
        self.select_add_pokemon()



        new_state = self.handle_envent_add_pokemon()
        return new_state

