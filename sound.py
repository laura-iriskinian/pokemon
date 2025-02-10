import pygame

class Sound:
    def __init__(self):
        self.music = pygame.mixer_music.load("asset/sound/Opening.mp3")
        self.music_volume = pygame.mixer.music.set_volume(0.25)
        self.battle_sound = pygame.mixer.Sound("asset/sound/Battle.mp3")

    def sound_volume(self):
        self.battle_sound.set_volume(0.25)
 