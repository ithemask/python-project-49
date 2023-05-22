import random
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'
RANGE_START = 0
RANGE_END = 99


def get_question():
    # get random numbers
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    return f'{num_1} {num_2}'


def get_correct_answer(question):
    # get greatest common divisor
    num_pair = question.split(' ')
    return str(gcd(int(num_pair[0]), int(num_pair[1])))
