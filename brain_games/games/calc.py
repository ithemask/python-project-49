import random


RANGE_START = 0
RANGE_END = 20


def get_task():
    return 'What is the result of the expression?'


def get_question_and_answer():
    num_1 = random.randint(RANGE_START, RANGE_END)
    num_2 = random.randint(RANGE_START, RANGE_END)
    operation = random.choice(['+', '-', '*'])
    question = f'{num_1} {operation} {num_2}'
    if operation == '+':
        answer = num_1 + num_2
    elif operation == '-':
        answer = num_1 - num_2
    elif operation == '*':
        answer = num_1 * num_2
    return (question, str(answer))
