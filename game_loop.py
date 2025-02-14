import pygame
from pygame.locals import *
from fight import Fight
from pokemon import Pokemon
from trainer import Trainer
from menu import Menu


pygame.init()

clock = pygame.time.Clock()
fps = 60

fight = Fight()
pokemon = Pokemon()
trainer = Trainer()
menu = Menu()

game_state = "state"
position = 1

run = True


def main_loop():
    while run:

        # #different states of the program
        # if game_state == "menu":
        #     menu()
        # elif game_state == "second_menu":
        #     second_menu()
        # elif game_state == "new player":
        #     new_player()
        # elif game_state == "sign in":
        #     sign_in()
        # elif game_state == "resume game":
        #     play()
        # elif game_state == "add pokemon":
        #     add_pokemon()
        # elif game_state == "pokedex":
        #     display_pokedex()
        # elif game_state == "new game":
        #     play_new_game()

        #handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        # draw background
        fight.draw_background_fight()

        # draw pokemon
        trainer.draw_pokemon_opponent_hp()
        trainer.draw_pokemons()

        # draw bottom panel
        fight.draw_panel()
        trainer.draw_panel_button(position) 

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
        clock.tick(fps)

    pygame.quit()
