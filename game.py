from user import User
import random


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
            print(comp.action(person))
        else:
            action = input('\nнатисни "А" щоб атакувати')

            if action == True:
                print(person.action(comp))

    if comp.live_status():
        print('Ви програли')
        
    else:
        print('Ви виграли')
        


if __name__ == '__main__':
    main()
