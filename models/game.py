import pygame
from pygame.locals import *

from models.fight import Fight
from models.trainer import Trainer

pygame.init()
clock = pygame.time.Clock()
fps = 60

class Game():

    def __init__(self):
        

        self.fight = Fight()
        self.trainer = Trainer()
        self.position = 1
        self.run = True


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
