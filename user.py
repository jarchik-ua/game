import random


class User:
    def __init__(self, isBot, type):
        self.hp = 100
        self.isBot = isBot
        self.type = type

    # Робить випадкове дію
    def action(self, user):
        if self.isBot:
            if self.hp <= 35:
                step = random.randint(0, 3)
            else:
                step = random.randint(0, 2)
        else:
            step = random.randint(0, 2)

        # message это переменная куда ты напиши что произошло
        if step == 0:
            user.hp -= random.randint(18, 25)
            message ="урон"
        elif step == 1:
            user.hp -= random.randint(10, 35)
            message ="урон"
        elif step == 2:
            user.hp += random.randint(18, 25)
            message ="урон"
        else:
            self.hp += random.randint(18, 25)
            message ="урон"

        return message

    # Перевіряє, чи живий гравець
    def live_status(self):
        if self.hp <= 0:
            return False
        else:
            return True
