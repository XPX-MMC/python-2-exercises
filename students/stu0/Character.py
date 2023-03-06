import random


class Character:

    def __init__(self, hit_points):
        self._hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 10)
        character.set_hit_points(character.get_hit_points() - random_number)

    def get_hit_points(self):
        return self._hit_points

    def set_hit_points(self, value):
        self._hit_points = value
