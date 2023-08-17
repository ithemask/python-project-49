import random


LEN_RANGE_START = 5
LEN_RANGE_END = 10
NUM_RANGE_START = 0
NUM_RANGE_END = 99


def get_task():
    return 'What number is missing in the progression?'


def get_progression():
    length = random.randint(LEN_RANGE_START, LEN_RANGE_END)
    start = random.randint(NUM_RANGE_START, NUM_RANGE_END - length)
    stop = random.randint(start + length, NUM_RANGE_END)
    step = int((stop - start) / length)
    return list(map(str, range(start, stop, step)))[:length]


def get_question_and_answer():
    progression = get_progression()
    miss_num_i = random.randint(0, len(progression) - 1)
    miss_num = progression[miss_num_i]
    progression[miss_num_i] = '..'
    question = ' '.join(progression)
    answer = str(miss_num)
    return (question, answer)
