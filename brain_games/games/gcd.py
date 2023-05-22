import random
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def get_question():
    # get random numbers
    num_1 = random.randint(0, 99)
    num_2 = random.randint(0, 99)
    return f'{num_1} {num_2}'


def get_correct_answer(question):
    # get greatest common divisor
    num_pair = question.split(' ')
    return str(gcd(int(num_pair[0]), int(num_pair[1])))
