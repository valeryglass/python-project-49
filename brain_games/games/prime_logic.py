# file <prime_logic.py> brain-prime logic

import random


def is_prime(number):
    '''Define weather given number is prime or not'''
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def logic_outputs():
    '''Make 'quest' and 'correct answer' for specific task'''
    task_text = ('Answer "yes" if given number is prime. '
                 'Otherwise answer "no".')  # task text
    x = 0  # parameter for randomization
    y = 99  # parameter for randomization
    quest = random.randint(x, y)  # format quest text
    if is_prime(quest):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return quest, correct_answer, task_text


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
