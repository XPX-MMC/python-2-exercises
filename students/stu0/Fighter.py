from .Character import Character


class Fighter(Character):

    def __repr__(self):
        return "Fighter: " + str(self.hit_points) + " hit points."
