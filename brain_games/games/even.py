import random


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    # get random number
    return random.randint(0, 99)


def get_correct_answer(question):
    # is even number
    if question % 2 == 0:
        return 'yes'
    return 'no'
