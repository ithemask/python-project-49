import prompt


def run(game):
    if game == 'even':
        from .games.even import task, get_question, get_correct_answer
    elif game == 'calc':
        from .games.calc import task, get_question, get_correct_answer
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(task)
    tries = 3
    while tries:
        question = get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(question)
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer "
                  f"was '{correct_answer}'.\nLet's try again, {username}!")
            break
        print('Correct!')
        tries -= 1
    if tries == 0:
        print(f'Congratulations, {username}!')
