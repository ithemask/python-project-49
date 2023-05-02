import prompt
import random
from . import welcome


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def even_game():
    username = welcome.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 3
    while tries:
        number = random.randint(0, 99)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_even(number)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{correct_answer}'.\nLet's try again, {username}!")
            break
        print('Correct!')
        tries -= 1
    if tries == 0:
        print(f'Congratulations, {username}!')
