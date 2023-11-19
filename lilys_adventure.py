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

# consider class for items
# i.e. healing potions, weapons, etc. 
# items should also have coordinates
#

class World():

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        self.matrix = [[' ' for _ in range(width)] for _ in range(height)]

    def get_element_at(self, x, y):
        if 0 <= x < self.width and 0 <= y <self.height:
            return self.matrix[y][x]
        else:
            return None

    def print_world(self):
        for row in self.matrix:
            print(' '.join(row))

class Character():

    def __init__(self, name: str, health: int, x: int, y: int, world: World):
        self.name = name
        self.health = health
        self.strength = randint(1, 150)
        self.position_x = x
        self.position_y = y
        self.world = world
        #self.world.matrix[x][y] = self.name

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

    def __init__(self, name: str, health: int, x: int, y: int, world: World):
        super().__init__(name, health, x, y, world)
        self.luck = randint(1, 10)
        self.inventory = []
        self.armor = 0 

    # add characteristics for the hero
    # i.e. skin, eyes, hair, species etc. 
    
    # Consider different approaches for this
    # i.e. check for creatures on the positions which you are passing over (not only where you land)
    # fight them and then continute to the final destination

    # Also add check for size of the direction - move should not be out of bounds
    def move(self, direction, count: int):
        for i in range(count):
            #OOPS
            if direction == 'up' and self.position_x > 0:
                self.world.matrix[self.position_x][self.position_y], self.world.matrix[self.position_x][self.position_y - 1] = self.world.matrix[self.position_x][self.position_y - 1], self.world.matrix[self.position_x][self.position_y]
                self.position_y -= 1
            elif direction == 'down' and self.position_x < self.world.width - 1:
                self.world.matrix[self.position_x][self.position_y], self.world.matrix[self.position_x][self.position_y + 1] = self.world.matrix[self.position_x][self.position_y + 1], self.world.matrix[self.position_x][self.position_y]
                self.position_y += 1
            elif direction == 'left' and self.position_y > 0:
                self.world.matrix[self.position_x][self.position_y], self.world.matrix[self.position_x - 1][self.position_y] = self.world.matrix[self.position_x - 1][self.position_y], self.world.matrix[self.position_x][self.position_y]
                self.position_x -= 1
            elif direction == 'right' and self.position_y < self.world.height - 1:
                self.world.matrix[self.position_x][self.position_y], self.world.matrix[self.position_x + 1][self.position_y] = self.world.matrix[self.position_x + 1][self.position_y], self.world.matrix[self.position_x][self.position_y]
                self.position_x += 1
           
    
    def heal(self, points):
        print('You healed yourself')
        self.healths += points
        print(f'Your health is: {self.health}')

# Functions

def fight(enemy: Character, player: Hero):
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
    # 
    #number_of_creatures = randint(1, size//3)
    number_of_creatures = randint(1, size)
    world = World(name, width, height)
    for i in range(number_of_creatures):
        creature = Character(enemy_list[randint(0, len(enemy_list) - 1)], randint(10, 300), randint(0, size - 1), randint(0, size - 1), world)
        world.matrix[creature.position_x][creature.position_y] = creature



    return world

def move_player(player: Hero, world: World):
    correct = False
    
    while not correct:
        moves = int(input('Enter how many moves you make: '))
        direction = str(input('Enter in which direction you want to travel: '))
        if (type(moves) is int and moves > 0) and (world.height >= moves <= world.width):
            msg = 'OK'
        else:
            msg = 'NOK'
            print("Moves should be a number greater than 0 and no bigger than the world size!")
        
        if type(direction) is str and direction.lower() in ['up', 'down', 'left', 'right'] and msg == 'OK':
            player.move(direction, moves)
            msg = f'You moved {moves} squares {direction}'
            correct = True
        else: 
            print('Direction should be one of the following text entries: up, down, left, right')

   # return msg

        
        
    

def gameplay(player: Hero, world: World):
      print(f'Welcome {player.name} to the world of {world.name}!')
      print('We need your help to cleanse the realm for the awful monsters which invaded us!')
      print('Please, mighty warrior, help us !!!')
      play = True
      while play:
        while player.health > 0:
            move_player(player, world)
            current_position = world.get_element_at(player.position_x, player.position_y)
            print(current_position)
            print(player.position_x, player.position_y)
            if isinstance(current_position, Character):
                print(f'Oh, no! There is a ferotios {current_position.name} here!')
                print('Prepare to fight!')
                print(current_position.name)


              
      
      

      
      pass

if __name__ == '__main__':
    my_world = generate_world('Nightshade', 5)
    hero = Hero(input('Please enter the name of your hero: '), 150, 1, 1, my_world)
    gameplay(hero, my_world)