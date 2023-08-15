import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 0
RANGE_END = 99


def get_question_and_answer():
    # get random number
    question = random.randint(RANGE_START, RANGE_END)
    # is even number
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
