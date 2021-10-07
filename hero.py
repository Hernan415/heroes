import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health = 100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.max_block = max_block
        self.max_damage = max_damage
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

def take_damage(self, damage):
  new_health = self.current_health - damage
  return new_health

def is_alive(self):
    if current_health <=0
        print("You died")
    else:
        print(current_health)
  pass


def fight(self, opponent):
  ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
  # TODO: Fight each hero until a victor emerges.
  # Phases to implement:
  # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
  # 1) else, start the fighting loop until a hero has won
  # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
  # 3) After each attack, check if either the hero (self) or the opponent is alive
  # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
  pass

 def add_weapon(self, weapon):
        abilitiies.append(weapon)
        pass

def add_kill(self, num_kills):
    self.kills += num_kills

def add_death(self, num_deaths):
    self.deaths += num_deaths
    pass

def stats(self):
    '''Print team statistics'''
    for hero in self.heroes:
        kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))

def revive_heroes(self, health=100):
    ''' Reset all heroes health to starting_health'''
    current_health = starting_health
    pass

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())
