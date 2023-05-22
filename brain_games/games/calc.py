import random


TASK = 'What is the result of the expression?'
RANGE_START = 0
RANGE_END = 20


def get_question():
    # get random expression
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    sign = random.choice(['+', '-', '*'])
    return f'{num_1} {sign} {num_2}'


def get_correct_answer(question):
    # get correct result
    return str(eval(question))
