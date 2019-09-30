from user import User
import random

# інформацію про вчинені дії
def print_info(info_about_step):
    step, points, name =info_about_step

    if step == 0 or step == 1:
        print('Гравець отримав  ураження'.format(name, points))
    else:
        print('Гравець оздоровився на '.format(name, points))
# головна функція
def main():
    comp = User(True, 'Comp')
    person = User(False, 'Person')

# цикл гри
    while True:
        print("здоров'я комп'ютера: " + str(comp.hp))
        print("Ваше здоров'я: " + str(person.hp))

        next_step = random.randint(0, 1)

        if next_step == 0:
            print("\nхід комп'ютера")
            print_info(comp.action(person))
        else:
            print('\nхід людини')
            input('\nНатисніть "enter" для атаки')

            if action == True:
                print_info(person.action(comp))

    if comp.live_status():
        print('Ви програли')
        
    else:
        print('Ви виграли')
        


if __name__ == '__main__':
    main()
