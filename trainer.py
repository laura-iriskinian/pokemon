import pygame
from pygame.locals import *
from window import Window
from pokemon import Pokemon
from fight import Fight

class Trainer(Pokemon):
    """class trainer : to select attack, menu, pokedex"""
    def __init__(self):
        super().__init__()
        self.window = Window()
        self.fight = Fight()

        # rectangle button to panel : (position x,position y,size x, size y)
        self.rectangle_top = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_top, self.window.sx_button, self.window.sy_button)
        self.rectangle_midle = pygame.Rect(self.window.px_pannel_left,self.window.py_rectangle_middle,self.window.sx_button,self.window.sy_button)
        self.rectangle_bottom = pygame.Rect(self.window.px_pannel_left, self.window.py_rectangle_bottom,self.window.sx_button,self.window.sy_button)

    def draw_panel_button(self,position):
        """def to draw panel button : search in dicto the position"""

        rectangle_button_position = {1 : self.rectangle_top, 
                                    2 : self.rectangle_midle, 
                                    3: self.rectangle_bottom, 
                                    4 :self.rectangle_bottom}

        self.rectangle_button = pygame.draw.rect(self.window.screen, 
                                                self.window.GREY, 
                                                rectangle_button_position[position],
                                                3)
        
        pygame.draw.rect(self.window.screen, self.window.GREY, self.rectangle_button, 3)

    def trainer_attack(self):
        self.attack()
        self.draw_hp_opponent_pokemon()