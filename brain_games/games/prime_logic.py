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
    # make 'quest' and 'correct answer' for specific task
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


def game_drive():
    # raund revolver
    i = 1  # raund index
    raund_count = 3  # max raund
    while i <= raund_count:
        logic_outputs_list = logic_outputs()
        quest = logic_outputs_list[0]
        correct_answer = logic_outputs_list[1]
        task_text = logic_outputs_list[2]
        if i == 1:
            print(f'{task_text}')
        i += 1
        print(f'Question: {quest}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            i = 0
            break
    return i, raund_count


def main():
    game_drive()


if __name__ == '__main__':
    main()
