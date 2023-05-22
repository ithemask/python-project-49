import prompt


TRIES_TO_WIN = 3


def run(game):
    if game == 'even':
        from .games.even import TASK, get_question, get_correct_answer
    elif game == 'calc':
        from .games.calc import TASK, get_question, get_correct_answer
    elif game == 'gcd':
        from .games.gcd import TASK, get_question, get_correct_answer
    elif game == 'progression':
        from .games.progression import TASK, get_question, get_correct_answer
    elif game == 'prime':
        from .games.prime import TASK, get_question, get_correct_answer
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(TASK)
    tries_left = TRIES_TO_WIN
    while tries_left:
        question = get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(question)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{correct_answer}'.\nLet's try again, {username}!")
            break
        print('Correct!')
        tries_left -= 1
    if tries_left == 0:
        print(f'Congratulations, {username}!')
