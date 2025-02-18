import pygame
from pygame.locals import *

from models.fight import Fight
from models.player_menu import Player_menu
from models.game_menu import Game_menu

pygame.init()
clock = pygame.time.Clock()
fps = 60

class Game():

    def __init__(self):
        
        self.player_menu = Player_menu()
        self.game_menu = Game_menu()
        self.fight = Fight()
        self.run = True
        self.current_state = "player_menu"


    def game(self):

        while self.run:
            
            clock.tick(fps)

            if self.current_state == "player_menu":
                self.current_state = self.player_menu.start_player_menu()

            if self.current_state == "game_menu":
                self.current_state = self.game_menu.start_game_menu()

            if self.current_state == "add_pokemon":
                self.current_state = self.game_menu.start_add_pokemon()
            
            if self.current_state == "fight":
                self.current_state = self.fight.start_fight()

            if self.current_state == "lose_game":
                self.current_state = self.fight.lose_fight()



                
            pygame.display.update()

        pygame.quit()
