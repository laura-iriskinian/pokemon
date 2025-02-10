import pygame
import random
import json
from sound import Sound

#load image files and sound
music = Sound()

pygame.display.set_caption("Pokemon") 
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("pictures/background.png")




pygame.init()

run = True

while run:


    pygame.display.update()


pygame.quit()
