# file <even_logic.py> brain-even logic

import random


def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    task_text = 'Answer "yes" if the number is even, otherwise answer "no".'  # task text
    x = 0  # parameter for randomization
    y = 99  # parameter for randomization
    quest = random.randint(x, y)  # format quest text
    if quest % 2 == 0:
        corr_ans = 'yes'
    else:
        corr_ans = 'no'
    return quest, corr_ans, task_text


def game_drive():
    # round revolver
    i = 1  # round index
    round_count = 3  # max round
    while i <= round_count:
        logic_outputs_list = logic_outputs()
        quest = logic_outputs_list[0]
        corr_ans = logic_outputs_list[1]
        task_text = logic_outputs_list[2]
        if i == 1:
            print(f'{task_text}')
        i += 1
        print(f'Question: {quest}')
        user_ans = input('Your answer: ')
        if user_ans == corr_ans:
            print('Correct!')
            print(i)
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            i = 0
            break
    return i, round_count

def main():
    game_drive()


if __name__ == '__main__':
    main()
