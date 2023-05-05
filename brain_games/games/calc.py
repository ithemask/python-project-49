import random


task = 'What is the result of the expression?'


def get_question():
    # get random expression
    num_1 = random.randint(0, 20)
    num_2 = random.randint(0, 20)
    sign = random.choice(['+', '-', '*'])
    return f'{num_1} {sign} {num_2}'


def get_correct_answer(question):
    # get correct result
    return str(eval(question))
