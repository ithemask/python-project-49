import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 0
RANGE_END = 99


def get_question():
    # get random number
    return random.randint(RANGE_START, RANGE_END)


def get_correct_answer(question):
    # is even number
    if question % 2 == 0:
        return 'yes'
    return 'no'
