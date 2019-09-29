from random import randint
from play.play import Computer
from play.play import Human



# Перевіряє, чи живий гравець
    def is_alive(self):
        return self._status

# Повертає поточну кількість здоров'я
    def get_health(self):
        return self._health

# лікує гравця
    def heal(self, hp):
        if self._health + hp > self._max_health:
            self._health = self._max_health
        else:
            self._health += hp

# приймає пошкодження
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


    def attack(self, player):
        if self._health <= 35:
            type_of_step = randint(0, 4)
        else:
            type_of_step = randint(0, 2)

        return self.make_step(player, type_of_step)
# інформацію про вчинені дії
    def print_info(info_about_step):
        type_of_step, points, name = info_about_step

        if type_of_step == 0 or type_of_step == 1:
            print('Player {} took {} points of damage'.format(name, points))
        else:
            print('Player {} healed by {} units'.format(name, points))



# Головна функція
    def main():
        computer = Computer()
        human = Human()

# Головний цикл гри
        while computer.is_alive() and human.is_alive():
            clear_screen()

            print("здоров'я комп'ютера: " + str(computer.get_health()))
            print("Ваше здоров'я: " + str(human.get_health()))

            step = randint(0, 1)

            if step == 0:
                print("\nхід комп'ютера")
                sleep(1)
                print_info(computer.attack(human))
            else:
                print("\nхід людини")
                input("\nНатисніть 'enter' для атаки")
                print_info(human.attack(computer))

            sleep(2)

            if not computer.is_alive():
                print("Ви виграли!")
            else:
                print("Ви програли!")

 		

    if __name__ == '__main__':
        main()

        