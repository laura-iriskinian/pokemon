from window import Window
import pygame


class Pokemon():
    """class to init pokemon, caract and draw"""

    def __init__(self):
        # background image
        self.window = Window()
        # pokemon 
        pokemon_player = pygame.image.load("assets/pictures/Fire/charmander_back.png").convert_alpha()
        self.pokemon_player = pygame.transform.scale(pokemon_player, (pokemon_player.get_width()*3, pokemon_player.get_height()*3))
        self.rect_pokemon_player = self.pokemon_player.get_rect()
        self.rect_pokemon_player.center = (250,330)

        pokemon_opponent = pygame.image.load("assets/pictures/Fire/charmander_front.png").convert_alpha()
        self.pokemon_opponent = pygame.transform.scale(pokemon_opponent, (pokemon_opponent.get_width()*3, pokemon_opponent.get_height()*3))
        self.rect_pokemon_opponent = self.pokemon_opponent.get_rect()
        self.rect_pokemon_opponent.center = (650,160)


    def draw_pokemon(self):
        """function to drawing pokemon """
        self.window.screen.blit(self.pokemon_player,self.rect_pokemon_player)
        self.window.screen.blit(self.pokemon_opponent,self.rect_pokemon_opponent)