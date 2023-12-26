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
    
    def update_world(self, player, npc):
        # Clear the previous positions of player and obstacle
        for row in range(self.height):
            for col in range(self.width):
                if (row, col) != (self.player.row, self.player.col) and (row, col) != self.obstacle:
                    self.matrix[row][col] = ' '

        self.matrix[self.player.position_x][self.player.position_y] = player
        row, col = self.npc.position_x, self.npc.position_y
        self.matrix[row][col] = npc
            
    def print_world(self):
        for row in self.matrix:
            print(' '.join(row))

class Character():

    def __init__(self, name: str, health: int, x: int, y: int, world: World):
        self.name = name
        self.health = health
        self.strength = randint(1, 150)
        self.position_x = x # row
        self.position_y = y # column
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
        target.take_dammage(randint(0, self.strength))

    def take_dammage(self, damage):
        self.health -= damage
        print(f'{self.name} took {damage} damage. Health: {self.health}')

class Hero(Character):

    def __init__(self, name: str, health: int, x: int, y: int, world: World):
        super().__init__(name, health, x, y, world)
        self.luck = randint(1, 10)
        self.inventory = []
        self.armor = 0
        self.position = [x, y]

    # add characteristics for the hero
    # i.e. skin, eyes, hair, species etc. 

    def heal(self, points):
        print('You healed yourself')
        self.healths += points
        print(f'Your health is: {self.health}')

class Gameplay:
    @staticmethod
    def fight(enemy: Character, player: Hero):
        escaped = False
        while player.health > 0 and enemy.health > 0 and not escaped:
            print('\nWhat are you going to do?')
            print('1. Attack')
            print('2. Run away')

            choice = int(input('Choose what your action will be (1 or 2): '))

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

        '''
        Movement: 
        Check the new coordinates, if there is object from class Character
        initiate a fight, if hero wins, remove Character object from new coordinates, 
        write her object to new coordinates
        Also add check for size of the direction - move should not be out of bounds
 
        # Consider different approaches for this
        # i.e. check for creatures on the positions which you are passing over (not only where you land)
        # fight them and then continute to the final destination
        
        '''

    @staticmethod
    def move_hero(hero: Hero, wrld):
        # wrld should be a matrix
        hero_pos = hero.position
        while True:
            direction = input('Enter the direction (up, down, left, right): ')

            # Validate the direction input
            if direction not in ['up', 'down', 'left', 'right']:
                print('Invalid direction. Please enter one of: up, down, left, right.')
                continue

            try:
                moves = int(input('Enter how many squares to move: '))

                # Validate the number of moves input
                if moves <= 0:
                    print('Number of moves must be a positive integer.')
                    continue

                if direction == 'up':
                    new_hero_pos = hero_pos[0] - moves
                    if new_hero_pos >= 0 and new_hero_pos <= (len(wrld) - 1):
                        print(f'Values on the new row (x) are: {wrld[new_hero_pos]}')
                        new_coordinates = wrld[new_hero_pos]
                        if type(new_coordinates) == Character:
                            while hero.health > 0 and new_coordinates.health > 0:
                                Gameplay.fight(new_coordinates, hero)
                                if hero.health <= 0:
                                    print('YOU WERE DEFEATED!!!')
                                    exit(0)
                        hero_pos[0] = new_hero_pos
                    else:
                        print('You have reached the border of the realm!')
                elif direction == 'down':
                    new_hero_pos = hero_pos[0] + moves
                    if new_hero_pos < len(wrld):
                        print(f'Values on the new row (x) are: {wrld[new_hero_pos]}')
                        new_coordinates = wrld[new_hero_pos]
                        if type(new_coordinates) == Character:
                            while hero.health > 0 and new_coordinates.health > 0:
                                Gameplay.fight(new_coordinates, hero)
                                if hero.health <= 0:
                                    print('YOU WERE DEFEATED!!!')
                                    exit(0)
                        hero_pos[0] = new_hero_pos
                    else:
                        print('You have reached the border of the realm!')
                elif direction == 'left':
                    new_hero_pos = hero_pos[1] - moves
                    if 0 <= new_hero_pos <= (len(wrld[hero_pos[0]]) - 1):
                        print(f'Values on the new position (x) are: {wrld[hero_pos[0]][new_hero_pos]}')
                        new_coordinates = wrld[hero_pos[0]][new_hero_pos]
                        if type(new_coordinates) == Character:
                            while hero.health > 0 and new_coordinates.health > 0:
                                Gameplay.fight(new_coordinates, hero)
                                if hero.health <= 0:
                                    print('YOU WERE DEFEATED!!!')
                                    exit(0)
                        hero_pos[1] = new_hero_pos
                    else:
                        print('You have reached the border of the realm!')
                elif direction == 'right':
                    new_hero_pos = hero_pos[1] + moves
                    if 0 <= new_hero_pos <= (len(wrld[hero_pos[0]]) - 1):
                        print(f'Values on the new row (x) are: {wrld[hero_pos[0]][new_hero_pos]}')
                        new_coordinates = wrld[hero_pos[0]][new_hero_pos]
                        if type(new_coordinates) == Character:
                            while hero.health > 0 and new_coordinates.health > 0:
                                Gameplay.fight(new_coordinates, hero)
                                if hero.health <= 0:
                                    print('YOU WERE DEFEATED!!!')
                                    exit(0)
                        hero_pos[1] = new_hero_pos
                    else:
                        print('You have reached the border of the realm!')

                break  # Exit the loop when valid input is received

            except ValueError:
                print('Invalid input. Number of moves must be a positive integer.')

# Functions

def generate_world():
        name = str(input('Please enter the name of your new realm: '))
        size = int(input('Please enter an integer to define the size of your world: '))
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

if __name__ == '__main__':
    my_world = generate_world()
    hero = Hero(input('Please enter the name of your hero: '), 150, 0, 0, my_world)
    
    while hero.health > 0:
        Gameplay.move_hero(hero, my_world.matrix)