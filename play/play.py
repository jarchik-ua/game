
#
class Player:
    def __init__(self):
        self._health = 100
        self._max_health = 100
        self._status = True
#
class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Human'

    def attack(self, player):
        type_of_step = randint(0, 2)

        return self.make_step(player, type_of_step)
#
class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'