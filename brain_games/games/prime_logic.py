# file <prime_logic.py> brain-prime logic

import random


def is_prime(number):
    # define weather given number is prime or not
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def logic_outputs():
    # make 'quest' and 'correct answer'
    x = 0
    y = 99
    quest = random.randint(x, y)
    if is_prime(quest):
        corr_ans = 'yes'
    else:
        corr_ans = 'no'
    return quest, corr_ans


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
