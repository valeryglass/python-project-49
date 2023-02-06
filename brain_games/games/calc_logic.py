# file <calc_logic.py> brain-calc logic

import random


def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    x = 0  # parameter for randomization
    y = 9  # parameter for randomization
    operator_list = ['+', '-', '*']  # list of operators
    first_number = random.randint(x, y)  # first element
    second_number = random.randint(x, y)  # second element
    operator = random.choice(operator_list)
    quest = str(first_number) + ' ' + operator + ' ' + str(second_number)  # format quest text
    corr_ans = str(eval(quest))  # calculate correct answer
    return quest, corr_ans


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
