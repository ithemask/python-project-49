import prompt


TRIES_TO_WIN = 3


def run(game):
    exec(f'from .games.{game} import TASK, get_ques_and_answ', globals())
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n{TASK}')
    tries_left = TRIES_TO_WIN
    while tries_left:
        ques_and_answ = get_ques_and_answ()
        print(f'Question: {ques_and_answ[0]}')
        answer = prompt.string('Your answer: ')
        if answer != ques_and_answ[1]:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{ques_and_answ[1]}'.\nLet's try again, {username}!")
            return
        print('Correct!')
        tries_left -= 1
    print(f'Congratulations, {username}!')
