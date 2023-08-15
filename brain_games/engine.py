import prompt


TRIES_TO_WIN = 3


def run(game):
    exec(f'from .games.{game} import TASK, get_question_and_answer', globals())
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n{TASK}')
    tries_left = TRIES_TO_WIN
    while tries_left:
        question_and_answer = get_question_and_answer()
        print(f'Question: {question_and_answer[0]}')
        answer = prompt.string('Your answer: ')
        if answer != question_and_answer[1]:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{question_and_answer[1]}'.\n"
                  f"Let's try again, {username}!")
            return
        print('Correct!')
        tries_left -= 1
    print(f'Congratulations, {username}!')
