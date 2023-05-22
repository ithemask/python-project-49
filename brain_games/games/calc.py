import random


TASK = 'What is the result of the expression?'
RANGE_START = 0
RANGE_END = 20


def get_ques_and_answ():
    # get random expression
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    operation = random.choice(['+', '-', '*'])
    question = f'{num_1} {operation} {num_2}'
    # get correct result
    answer = str(eval(question))
    return (question, answer)
