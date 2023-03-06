from .Character import Character


class Dwarf(Character):

    def __repr__(self):
        return "Drawf: " + str(self.hit_points) + " hit points."

