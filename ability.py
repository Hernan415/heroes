class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value


def add_ability(self, ability):
    ability.append("Fireball")
    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)

def attack(self):
      damage = sum(ability)

      # start our total out at 0
      total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage
