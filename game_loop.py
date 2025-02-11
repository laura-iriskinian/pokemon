import pygame


from fight import Fight
from pokemon import Pokemon

pygame.init()

clock = pygame.time.Clock()
fps = 60


fight = Fight()
pokemon = Pokemon()
run = True

while run:

    clock.tick(fps)

    # draw background
    fight.draw_background()

    # draw bottom panel
    fight.draw_panel()

    # draw pokemon
    pokemon.draw_pokemon()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()


pygame.quit()
