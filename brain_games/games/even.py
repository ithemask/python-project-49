import random


RANGE_START = 0
RANGE_END = 99


def get_task():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def get_question_and_answer():
    question = random.randint(RANGE_START, RANGE_END)
    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
