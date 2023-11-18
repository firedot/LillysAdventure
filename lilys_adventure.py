import pygame 
import sounddevice as sd
import soundfile as sf
import time
from random import randint

# Variables
enemy_list = ['Evil Goat', 'Harpy', 'Horned woperfloff', 
              'Tree mongler', 'Aligator', 'Fluff Dragon', 'Biter', 
              'Giant rat', 'Poisonous sheep']
# Classes
class Character():

    def __init__(self, name: str, health: int, x: int, y: int):
        self.name = name
        self.health = health
        self.strength = randint(1, 150)
        self.position_x = x
        self.position_y = y

    def battle_cry(self):
        fname = f'battlecry_{self.name}.wav'
        pygame.init()
        pygame.mixer.music.load(fname)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock.tick(5)

    # add record_battlecry and battlecry methods
    
    def attack(self, target):
        print(f'{self.name} attacks {target.name}')
        target.take_damage(randint(0, self.strength))

    def take_dammage(self, damage):
        self.health -= damage
        print(f'{self.name} took {damage} damage. Health: {self.health}')

class Hero(Character):

    def __init__(self, name: str, health: int, x: int, y: int):
        super().__init__(name, health)
        self.luck = randint(1, 10)
    
    def move(self, direction, count):

        for i in range(count):
            if direction == 'up' and self.y > 0:
                self.world.matrix[self.y][self.x], self.world.matrix[self.y -1][self.x]
                self.y -= 1
            

class World():

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.matrix = [[' ' for _ in range(width)] for _ in range(height)]
    
    def print_world(self):
        for row in self.matrix:
            print(' '.join(row))
# Fucntions

def fight(enemy_name: str, enemy_health: int, player: Hero):
    enemy = Character(enemy_name, enemy_health)
    print(f'Oh, no! You have encounterd a {enemy.name}')
    escaped = False
    while player.health > 0 and enemy.health >0 or escaped:
        print(f'\nWhat are you going to do?')
        print('1. Attack')
        print('2. Run away')

        choice = int('Choose what are your action will be (1 or 2): ')

        if choice == 1:
            if randint(0, 10) > player.luck:
                enemy.attack(player)
                player.attack(enemy)
            else:
                player.attack(enemy)
                enemy.attack(player)
        elif choice == 2:
            if randint(0, 10) > player.luck:
                print("Darn! You failed to escape!")
                print("Prepare to FIGHT!")
                enemy.attack(player)
            else:
                print('You have successfully escaped!')
                escaped = True

def generate_world(name: str, size: int):
    width = size
    height = size
    number_of_creatures = randint(1, size//3)
    world = World(name, width, height)
    creatures = []
    for i in range(number_of_creatures):
        creature = Character(enemy_list[randint(0, len(enemy_list))], randint(10, 300), randint(1, size), randint(1, size))
        creatures.append(creature)

if __name__ == '__main__':
    pass