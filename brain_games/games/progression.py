import random


LEN_RANGE = {'start': 5, 'end': 10}
START_RANGE = {'start': 0, 'end': 100}
STEP_RANGE = {'start': 1, 'end': 10}


def get_task():
    return 'What number is missing in the progression?'


def get_progression(length, start, step):
    return list(map(str, range(start, start + step * length, step)))


def get_question_and_answer():
    length = random.randint(LEN_RANGE['start'], LEN_RANGE['end'])
    start = random.randint(START_RANGE['start'], START_RANGE['end'])
    step = random.randint(STEP_RANGE['start'], STEP_RANGE['end'])
    progression = get_progression(length, start, step)
    miss_num_i = random.randint(0, len(progression) - 1)
    miss_num = progression[miss_num_i]
    progression[miss_num_i] = '..'
    question = ' '.join(progression)
    answer = str(miss_num)
    return (question, answer)
