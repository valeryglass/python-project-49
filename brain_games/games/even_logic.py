# file <even_logic.py> brain-even logic

import random

def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    x = 0  # parameter for randomization
    y = 99  # parameter for randomization
    quest = random.randint(x, y)  # format quest text
    if quest % 2 == 0:
        corr_ans = 'yes'
    else:
        corr_ans = 'no'
    return quest, corr_ans


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
