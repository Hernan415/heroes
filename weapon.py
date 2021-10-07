class Weapon(Ability):
    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value
        pass
