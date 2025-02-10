import pygame
import json


class Pokemon:
    def __init__(self, name: str, hp: int, level: int, attack: int, defense: int):
        self.name = name 
        self.hp = hp
        self.level = level
        self.attack = attack
        self.defense = defense

    
