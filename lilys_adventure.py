import pygame 
import sounddevice as sd
import soundfile as sf
import time
from random import randint

class Character():

    def __init__(self, name):
        self.name = name
        self.lifepoints = 100
        self.strength = randint(0, 150)

    def record_battle_cry(self):
        '''
        Recording battle cry to wav file
        used only for hero characters
        '''
        fname = f'battlecry_{self.name}.wav'
        fs = 44100 # 44.khz
        duration = 3 # seconds

        # Record audio
        recording = sd.rec(int(fs * duration), samplerate=fs, channels=2, dtype='int16')
        sd.wait()

        # Save the recording to a file
        sf.write(fname, recording, fs)

    def battle_cry(self):
        fname = f'battlecry_{self.name}.wav'
        pygame.init()
        pygame.mixer.music.load(fname)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock.tick(5)


if __name__ == '__main__':
    pass