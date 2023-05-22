import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_START = 0
RANGE_END = 99


def get_question():
    # get random number
    return random.randint(RANGE_START, RANGE_END)


def get_correct_answer(question):
    # is prime number (using 'Sieve of Eratosthenes' algorithm)
    if question < 2:
        return 'no'
    sequence = list(range(2, question + 1))
    prime_div_i = 0
    prime_div = sequence[prime_div_i]
    while prime_div ** 2 <= question:
        for i, elem in enumerate(sequence):
            if elem != prime_div and elem % prime_div == 0:
                sequence.pop(i)
        prime_div_i += 1
        prime_div = sequence[prime_div_i]
    if question in sequence:
        return 'yes'
    return 'no'
