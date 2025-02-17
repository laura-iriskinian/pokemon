import pygame
from pygame.locals import *

from models.fight import Fight
from models.trainer import Trainer
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
        self.trainer = Trainer()
        self.position = 1
        self.run = True
        self.current_state = "player_menu"


        # draw background
        self.fight.draw_background_fight()

        # draw pokemon
        self.trainer.pokemon_opponent[0].draw_pokemon_opponent_hp()
        self.trainer.pokemon_player.draw_pokemon_player()
        self.trainer.pokemon_opponent[0].draw_pokemon_opponent()
        self.trainer.pokemon_player.draw_pokemon_player_hp()

        # draw bottom panel
        self.fight.draw_panel()
        self.trainer.select_fight_button(self.position) 



    def game(self):



        while self.run:
            
            clock.tick(fps)

            if self.current_state == "player_menu":
                self.current_state = self.player_menu.start_player_menu()

            if self.current_state == "game_menu":
                self.current_state = self.game_menu.start_game_menu()

            if self.current_state == "game":
            

                # draw background
                self.fight.draw_background_fight()

                # draw pokemon
                self.trainer.pokemon_opponent[0].draw_pokemon_opponent_hp()
                self.trainer.pokemon_player.draw_pokemon_player()
                self.trainer.pokemon_opponent[0].draw_pokemon_opponent()
                self.trainer.pokemon_player.draw_pokemon_player_hp()

                # draw bottom panel
                self.fight.draw_panel()
                self.trainer.select_fight_button(self.position) 

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False

                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            if self.position >= 1:
                                self.position += 1
                                self.fight.draw_panel()
                                self.trainer.select_fight_button(self.position) 
                            if self.position == 4:
                                self.position -=3
                                self.fight.draw_panel()
                                self.trainer.select_fight_button(self.position) 
                        if event.key == K_UP:
                            if self.position >= 1:
                                self.position -= 1
                                self.fight.draw_panel()
                                self.trainer.select_fight_button(self.position) 
                            if self.position == 0:
                                self.position +=3
                                self.fight.draw_panel()
                                self.trainer.select_fight_button(self.position) 
                        if event.key == K_RETURN:
                            if self.trainer.rectangle_top.colliderect(self.trainer.rectangle_button):
                                self.trainer.trainer_attack()

                pygame.display.update()

        pygame.quit()
