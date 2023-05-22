import random


TASK = 'What number is missing in the progression?'
LEN_RANGE_START = 5
LEN_RANGE_END = 10
NUM_RANGE_START = 0
NUM_RANGE_END = 99


def get_question():
    # get random progression with missing number
    init_len = random.randint(LEN_RANGE_START, LEN_RANGE_END)
    start = random.randint(NUM_RANGE_START, NUM_RANGE_END - init_len)
    stop = random.randint(start + init_len, NUM_RANGE_END)
    step = int((stop - start) / init_len)
    progr = list()
    for num in range(start, stop, step):
        if len(progr) == 10:
            break
        progr.append(str(num))
    final_len = len(progr)
    progr[random.randint(0, final_len) - 1] = '..'
    return ' '.join(progr)


def get_correct_answer(question):
    # get missing number
    progr = question.split(' ')
    for i, elem in enumerate(progr):
        if elem == '..':
            if i > 1:
                miss_num = int(progr[i - 1]) * 2 - int(progr[i - 2])
            else:
                miss_num = int(progr[i + 1]) * 2 - int(progr[i + 2])
            return str(miss_num)
