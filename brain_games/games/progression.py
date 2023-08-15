import random


def get_task():
    TASK = 'What number is missing in the progression?'


LEN_RANGE_START = 5
LEN_RANGE_END = 10
NUM_RANGE_START = 0
NUM_RANGE_END = 99


def get_question_and_answer():
    # get random progression with missing number
    init_len = random.randint(LEN_RANGE_START, LEN_RANGE_END)
    start = random.randint(NUM_RANGE_START, NUM_RANGE_END - init_len)
    stop = random.randint(start + init_len, NUM_RANGE_END)
    step = int((stop - start) / init_len)
    progr = list()
    for num in range(start, stop, step):
        if len(progr) == LEN_RANGE_END:
            break
        progr.append(str(num))
    final_len = len(progr)
    miss_num_i = random.randint(0, final_len - 1)
    miss_num = progr[miss_num_i]
    progr[miss_num_i] = '..'
    question = ' '.join(progr)
    answer = str(miss_num)
    return (question, answer)
