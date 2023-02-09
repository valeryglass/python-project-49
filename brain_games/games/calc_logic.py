# file <calc_logic.py> brain-calc logic

import random


def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    task_text = 'What is the result of the expression?'  # task text
    x = 0  # parameter for randomization
    y = 9  # parameter for randomization
    operator_list = ['+', '-', '*']  # list of operators
    first_number = random.randint(x, y)  # first element
    second_number = random.randint(x, y)  # second element
    operator = random.choice(operator_list)
    quest = str(first_number) + ' ' + operator + ' ' + str(second_number)  # format quest text
    corr_ans = str(eval(quest))  # calculate correct answer
    return quest, corr_ans, task_text


def game_drive():
    # round revolver
    i = 1  # round index
    round_count = 4  # max round
    while i < round_count:
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
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            break
    return i, round_count


def main():
    game_drive()


if __name__ == '__main__':
    main()
