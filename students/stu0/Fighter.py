from .Character import Character


class Fighter(Character):

    def __repr__(self):
        return "Fighter: " + str(self.get_hit_points()) + " hit points."


