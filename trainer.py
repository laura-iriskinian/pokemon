import pygame
from pygame.locals import *
from window import Window
from pokemon import Pokemon
from fight import Fight

class Trainer():
    """class trainer : to select attack, menu, pokedex"""
    def __init__(self):
        self.window = Window()
        self.fight = Fight()
        self.pokemon_player = Pokemon()
        self.pokemon_opponent = [Pokemon()]

        # rectangle button to panel : (position x,position y,size x, size y)
        self.rectangle_top = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_top, self.window.sx_button, self.window.sy_button)
        self.rectangle_midle = pygame.Rect(self.window.px_pannel_left,self.window.py_rectangle_middle,self.window.sx_button,self.window.sy_button)
        self.rectangle_bottom = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_bottom,self.window.sx_button,self.window.sy_button)

    def select_fight_button(self,position):
        """def to draw panel button : search in dicto the position"""

        rectangle_button_position = {0 : self.rectangle_bottom,
                                    1 : self.rectangle_top, 
                                    2 : self.rectangle_midle, 
                                    3: self.rectangle_bottom, 
                                    4 :self.rectangle_bottom}

        self.rectangle_button = pygame.draw.rect(self.window.screen, 
                                                self.window.GREY, 
                                                rectangle_button_position[position],
                                                3)
        
        pygame.draw.rect(self.window.screen, self.window.GREY, self.rectangle_button, 3)

    def trainer_attack(self):
    # attack
        self.pokemon_opponent[0].player_attack()

        if self.pokemon_opponent[0].pokemon_opponent_life <=0:
            self.pokemon_opponent.append(Pokemon())
            del self.pokemon_opponent[0]

        self.pokemon_player.opponent_attack()

        # reset 
        self.fight.draw_background_fight()
        self.pokemon_player.draw_pokemon_player()
        self.pokemon_opponent[0].draw_pokemon_opponent()
        self.fight.draw_panel()
        self.select_fight_button(1)
        self.pokemon_opponent[0].draw_pokemon_opponent_hp()

        self.pokemon_player.draw_pokemon_player_hp()