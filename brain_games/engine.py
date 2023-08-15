import prompt


ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n{game.get_task()}')
    rounds_left = ROUNDS_COUNT
    while rounds_left:
        question_and_answer = game.get_question_and_answer()
        print(f'Question: {question_and_answer[0]}')
        answer = prompt.string('Your answer: ')
        if answer != question_and_answer[1]:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{question_and_answer[1]}'.\n"
                  f"Let's try again, {username}!")
            return
        print('Correct!')
        rounds_left -= 1
    print(f'Congratulations, {username}!')
