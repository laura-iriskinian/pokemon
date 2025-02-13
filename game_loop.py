import pygame
from pygame.locals import *

from fight import Fight
from pokemon import Pokemon
from trainer import Trainer

pygame.init()

clock = pygame.time.Clock()
fps = 60


fight = Fight()
pokemon = Pokemon()
trainer = Trainer()
position = 1
run = True
# draw background
fight.draw_background_fight()

# draw pokemon
trainer.draw_pokemon_opponent_hp()
trainer.draw_pokemons()

# draw bottom panel
fight.draw_panel()
trainer.draw_panel_button(position) 


while run:

    clock.tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if position >= 1:
                    position += 1
                    fight.draw_panel()
                    trainer.draw_panel_button(position) 
                if position == 4:
                    position -=3
                    fight.draw_panel()
                    trainer.draw_panel_button(position) 
            if event.key == K_RETURN:
                if trainer.rectangle_top.colliderect(trainer.rectangle_button):
                    trainer.trainer_attack()

    pygame.display.update()


pygame.quit()
