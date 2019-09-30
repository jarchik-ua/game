import random


class User:
    def __init__(self, isBot, type):
        self.hp = 100
        self.isBot = isBot
        self.type = type

    # Повертає здоров'я
    def get_health(self):
        return self._health

    
    def action(self, user):
        if self.isBot:
            if self.hp <= 35:
                step = random.randint(0, 3)
            else:
                step = random.randint(0, 2)
        else:
            step = random.randint(0, 2)

# Робить випадкове дію
    def message(self, user, step):
        if step == 0:
            points = randint(18, 25)
            user.get_damage(points)
        elif step == 1:
            points = randint(10, 35)
            user.get_damage(points)
        elif step == 2:
            points = randint(18, 25)
            user.heal(points)
        else:
            points = randint(18, 25)
            user = self
            user.heal(points)

        return step, points, user.name

    # Перевіряє, чи живий гравець
    def live_status(self):
        if self.hp <= 0:
            return False
        else:
            return True
