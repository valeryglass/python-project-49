# file <calc_logic.py> brain-calc logic

import random


def logic_outputs():
    '''Make 'quest' and 'correct answer' for specific task'''
    task_text = 'What is the result of the expression?'  # task text
    x = 0  # parameter for randomization
    y = 9  # parameter for randomization
    operator_list = ['+', '-', '*']  # list of operators
    first_number = random.randint(x, y)  # first element
    second_number = random.randint(x, y)  # second element
    operator = random.choice(operator_list)
    quest = str(first_number) + ' ' + operator + ' ' + str(second_number)
    correct_answer = str(eval(quest))  # calculate correct answer
    return quest, correct_answer, task_text


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
