import pygame

class Sound:
    def __init__(self):
        self.music = pygame.mixer_music.load("assets/sound/Opening.mp3")
        self.music_play = pygame.mixer.music.play(loops = -1) #-1 makes the music loop indefinitely
        self.music_volume = pygame.mixer.music.set_volume(0.25)
        # self.battle_sound = pygame.mixer.Sound("asset/sound/Battle.mp3")

    def sound_volume(self):
        self.battle_sound.set_volume(0.3)