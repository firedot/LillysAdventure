import pygame 
import sounddevice as sd
import soundfile as sf
import time
from random import randint

class Character():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.strength = randint(0, 150)

    def battle_cry(self):
        fname = f'battlecry_{self.name}.wav'
        pygame.init()
        pygame.mixer.music.load(fname)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock.tick(5)
    
    def attack(self, target):
        pass

    def take_dammage(self, damage):
        pass

class Hero(Character):

    def __init__(self, name, health):
        super().__init__(name, health)


if __name__ == '__main__':
    pass