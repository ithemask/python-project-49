import random


TASK = 'What is the result of the expression?'
RANGE_START = 0
RANGE_END = 20


def get_question_and_answer():
    # get random expression
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    operation = random.choice(['+', '-', '*'])
    question = f'{num_1} {operation} {num_2}'
    # get correct result
    if operation == '+':
        answer = num_1 + num_2
    elif operation == '-':
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2
    return (question, str(answer))
