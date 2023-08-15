import prompt


ROUNDS_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!\n{game.get_task()}')
    for _ in range(ROUNDS_COUNT):
        question, answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer "
                  f"was '{answer}'.\n"
                  f"Let's try again, {username}!")
            return
        print('Correct!')
    print(f'Congratulations, {username}!')
