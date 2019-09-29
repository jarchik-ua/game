from play.compandperson  import Comp
from play.compandperson import Person
from random import randint
from time import sleep
from os import name, system


# інформацію про вчинені дії
def print_info(info_about_step):
    type_of_step, points, name = info_about_step

    if type_of_step == 0 or type_of_step == 1:
        print('Гравець отримав  ураження'.format(name, points))
    else:
        print('Гравець оздоровився на '.format(name, points))

# очистка екрану
def clear_screen():
    if name == 'posix':
        system('clear')
    elif name == 'nt':
        system('cls')

# головна функція
def main():
    comp = Comp()
    person = Person()

# цикл гри
    while comp.is_alive() and person.is_alive():
        clear_screen()

        print("здоров'я комп'ютера: " + str(comp.get_health()))
        print("Ваше здоров'я: " + str(person.get_health()))

        step = randint(0, 1)

        if step == 0:
            print("\nхід комп'ютера")
            sleep(1)
            print_info(comp.attack(person))
        else:
            print('\nхід людини')
            input('\nНатисніть "enter" для атаки')
            print_info(person.attack(comp))

        sleep(2)

        if not comp.is_alive():
            print('Ви виграли!')
        else:
            print('Ви програли!')


if __name__ == '__main__':
    main()