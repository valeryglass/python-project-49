# file <even_logic.py> brain-even logic

import random


def logic_outputs():
    '''Make 'quest' and 'correct answer' for specific task'''
    task_text = ('Answer "yes" if the number is even, '
                 'otherwise answer "no".')  # task text
    x = 0  # parameter for randomization
    y = 99  # parameter for randomization
    quest = random.randint(x, y)  # format quest text
    if quest % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return quest, correct_answer, task_text


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
