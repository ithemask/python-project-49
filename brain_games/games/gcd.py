import random
from math import gcd


def get_task():
    return 'Find the greatest common divisor of given numbers.'


RANGE_START = 0
RANGE_END = 99


def get_question_and_answer():
    # get random numbers
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    question = f'{num_1} {num_2}'
    # get greatest common divisor
    answer = str(gcd(num_1, num_2))
    return (question, answer)
