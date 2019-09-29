from play.player import Player
from random import randint


class Person(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Person'

    def attack(self, player):
        type_of_step = randint(0, 2)

        return self.make_step(player, type_of_step)
class Comp(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Comp'

    def attack(self, player):
        if self._health <= 35:
            type_of_step = randint(0, 4)
        else:
            type_of_step = randint(0, 2)

        return self.make_step(player, type_of_step)