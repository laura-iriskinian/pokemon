from models.fight import Fight
from models.player_menu import Player_menu
from models.game_menu import Game_menu
from models.create_player_menu import Create_player_menu
from models.connect_player import Connect_player
from models.add_pokemon import Add_pokemon
from models.starter_choice import Starter_choice
from models.pokedex import Pokedex
from models.sound import Sound
import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

class Game_manager():

    def __init__(self):
        self.music = Sound()
        self.player_menu = Player_menu()
        self.create_player_menu = Create_player_menu()
        self.connect_player = Connect_player()
        # self.starter_choice = Starter_choice()
        self.game_menu = Game_menu()
        self.add_pokemon = Add_pokemon()
        # self.pokedex = Pokedex()
        # self.fight = Fight()

        self.run = True
        self.current_state = "player_menu"
        self.reset_fight = True
        # self.player_selected = None
        # self.fight = Fight(self.player_selected) 
    def game(self):

        while self.run:
            clock.tick(fps)

            if self.current_state == "player_menu":
                self.current_state = self.player_menu.start_player_menu()

            if self.current_state == "connect_player":
                self.current_state,self.player_selected = self.connect_player.connect_player()
                if self.current_state == "game_menu" and self.player_selected:
                    self.fight = Fight(self.player_selected) 
                    self.pokedex = Pokedex(self.player_selected)
                else:
                    self.current_state = "connect_player"



            if self.current_state == "create_player":
                self.current_state,self.player_created = self.create_player_menu.start_create_player()
                if self.current_state == "starter_choice" and self.player_created:
                    self.starter_choice = Starter_choice(self.player_created)
                else:
                    self.current_state = "create_player"

            if self.current_state == "starter_choice":

                self.current_state,self.player_created = self.starter_choice.start_starter_choice()

                if self.current_state == "game_menu" and self.player_created:
                    self.fight = Fight(self.player_created)
                    self.pokedex = Pokedex(self.player_created) 
                else : 
                    self.current_state = "starter_choice"

            if self.current_state == "game_menu":
                self.current_state = self.game_menu.start_game_menu()

            if self.current_state == "pokedex":
                self.current_state = self.pokedex.start_pokedex_menu()

            if self.current_state == "add_pokemon":
                self.current_state = self.add_pokemon.start_add_pokemon()

            if self.current_state == "fight":
                if self.reset_fight == True:
                    self.fight.initialize_opponent()
                    self.reset_fight = False
                
                self.current_state = self.fight.start_fight()

                if self.current_state != "fight":
                    self.reset_fight = True

            if self.current_state == "lose_game":
                self.current_state = self.fight.lose_fight()


            pygame.display.update()

        pygame.quit()