# import random

class Character:
    def __init__(self, health, attack_power):
        self.health = health
        self.attack_power = attack_power

    def fight(self, character):
        # random_number = random.randint(1, 20)
        character.health -= self.attack_power

        # prevent health from being a negative number
        if character.health < 0:
            character.health = 0

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.health} health left. \n Does {self.attack_power} damage!"

class Fighter(Character):
    pass
    def __repr__(self):
        return f"Special class: Fighter! \n {self.health} health left. \n Does {self.attack_power} damage!"


class Dwarf(Character):
    pass
    def __repr__(self):
        return f"Special class: Dwarf! \n {self.health} health left. \n Does {self.attack_power} damage!"
