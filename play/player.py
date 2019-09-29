from random import randint


class Player:
    def __init__(self):
        self._health = 100
        self._max_health = 100
        self._status = True

    # Перевіряє, чи живий гравець
    def is_alive(self):
        return self._status

    # Повертає здоров'я
    def get_health(self):
        return self._health

    # лікує гравця
    def heal(self, hp):
        if self._health + hp > self._max_health:
            self._health = self._max_health
        else:
            self._health += hp

    # приймає урон
    def get_damage(self, damage):
        self._health -= damage

        if self._health <= 0:
            self._status = False

    # Робить випадкове дію
    def make_step(self, player, type_of_step):
        if type_of_step == 0:
            points = randint(18, 25)
            player.get_damage(points)
        elif type_of_step == 1:
            points = randint(10, 35)
            player.get_damage(points)
        elif type_of_step == 2:
            points = randint(18, 25)
            player.heal(points)
        else:
            points = randint(18, 25)
            player = self
            player.heal(points)

        return type_of_step, points, player.name