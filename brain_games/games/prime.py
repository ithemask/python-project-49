import random


RANGE_START = 0
RANGE_END = 99


def get_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def get_question_and_answer():
    # get random number
    question = random.randint(RANGE_START, RANGE_END)
    # is prime number
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
