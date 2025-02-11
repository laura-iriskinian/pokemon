import pygame
import random
import json
from screen import Screen
# from sound import Sound

pygame.init()

clock = pygame.time.Clock()
fps = 60


class Pokemon(Screen):

        def __init__(self):
            super().__init__()
            # background image
            self.background = pygame.image.load("assets/pictures/background.png").convert_alpha()

            # pokemon 
            pokemon_player = pygame.image.load("assets/pictures/Fire/charmander_back.png").convert_alpha()
            self.pokemon_player = pygame.transform.scale(pokemon_player, (pokemon_player.get_width()*3, pokemon_player.get_height()*3))
            self.rect_pokemon_player = self.pokemon_player.get_rect()
            self.rect_pokemon_player.center = (250,330)

            pokemon_opponent = pygame.image.load("assets/pictures/Fire/charmander_front.png").convert_alpha()
            self.pokemon_opponent = pygame.transform.scale(pokemon_opponent, (pokemon_opponent.get_width()*3, pokemon_opponent.get_height()*3))
            self.rect_pokemon_opponent = self.pokemon_opponent.get_rect()
            self.rect_pokemon_opponent.center = (650,160)


        def draw_panel(self):
            """draw rectangle for bottom panel"""
            # full Rectangle 
            rectangle_left = pygame.Rect(0, self.screen_height - self.bottom_panel, self.screen_width / 2, self.bottom_panel)
            pygame.draw.rect(self.screen, self.BLUE, rectangle_left)
            rectangle_right = pygame.Rect(self.screen_width/2, self.screen_height - self.bottom_panel, self.screen_width / 2, self.bottom_panel)
            pygame.draw.rect(self.screen, self.BLUE, rectangle_right)

            # outline rectangle 
            pygame.draw.rect(self.screen, self.GREY, rectangle_left, 3)
            pygame.draw.rect(self.screen, self.GREY, rectangle_right, 3)

        def draw_background(self):
            """function to drawing background"""
            self.screen.blit(self.background,(0,0))

        def draw_pokemon(self):
            """function to drawing pokemon """
            self.screen.blit(self.pokemon_player,self.rect_pokemon_player)
            self.screen.blit(self.pokemon_opponent,self.rect_pokemon_opponent)

sprite = Pokemon()
run = True

while run:

    clock.tick(fps)

    # draw background
    sprite.draw_background()

    # draw bottom panel
    sprite.draw_panel()

    sprite.draw_pokemon()

    # sprite.draw_pokemon()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()
