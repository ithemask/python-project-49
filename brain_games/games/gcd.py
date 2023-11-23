import random
from math import gcd


RANGE_START = 0
RANGE_END = 99


def get_task():
    return 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    question = f'{num_1} {num_2}'
    answer = str(gcd(num_1, num_2))
    return (question, answer)
