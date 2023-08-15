import random


def get_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    # is prime number (using 'Sieve of Eratosthenes' algorithm)
    if number < 2:
        return False
    sequence = list(range(2, number + 1))
    prime_div_i = 0
    prime_div = sequence[prime_div_i]
    while prime_div ** 2 <= number:
        for i, elem in enumerate(sequence):
            if elem != prime_div and elem % prime_div == 0:
                sequence.pop(i)
        prime_div_i += 1
        prime_div = sequence[prime_div_i]
    if number in sequence:
        return True
    else:
        return False


RANGE_START = 0
RANGE_END = 99


def get_question_and_answer():
    # get random number
    question = random.randint(RANGE_START, RANGE_END)
    # is prime number
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
