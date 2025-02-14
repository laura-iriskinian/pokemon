from models.game import Game

from models.menu import *
from models.second_menu import Second_menu
from models.pokedex_menu import Pokedex_menu


pygame.init()
run = True
menu = Menu()
second_menu=Second_menu()
pokedex_menu = Pokedex_menu()
current_menu = menu
while run:
    #set the scene
    current_menu.draw_background()
    current_menu.draw_buttons()
    current_menu.select_menu_button()

    #handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #handle events based on the type of menu
        current_menu.handle_events(event)

        if event.type == KEYDOWN and event.key == K_RETURN:
            if current_menu == menu:
                current_menu = second_menu
            else:
                current_menu = menu
            
            # elif event.key == K_RETURN:
                # if menu.selected_position == 1:
                #     sign_in()
                # if menu.selected_button == 2:
                #     game()
                    

    pygame.display.update()


pygame.quit()


if __name__ == "__main__":

    g = Menu()
    g.menu_loop()

