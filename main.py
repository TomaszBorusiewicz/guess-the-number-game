# Guess the number game

from random import randint


def roll_rand_number() -> int:
    return randint(1, 10)


def take_number_from_user() -> int:
    number = input('Choose a number between 1 and 10: ')
    try:
        return int(number)
    except ValueError:
        print('Wrong value was given, please type a number from 1 to 10')
        take_number_from_user()


def main():
    computer_number = roll_rand_number()
    user_number = None
    guess_iter = 0
    while computer_number != user_number:
        user_number = take_number_from_user()
        if user_number == computer_number:
            print('Great you guessed the number')
        else:
            print("you didn't guess the number, try again")
            guess_iter += 1
    print(f'it took you {guess_iter} rounds to guess the number')

main()