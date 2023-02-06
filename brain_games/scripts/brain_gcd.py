#!/usr/bin/env python3
# file <brain_gcd.py> brain_gcd game script

from brain_games.cli import welcome_user, summary
from brain_games.games.gcd_logic import logic_outputs


# intro
print('Welcome to the Brain Games!')
name = welcome_user('')


def brain_gcd():
    # user_ans = ''  # ответ пользователя
    # corr_ans = ''  # правильный ответ
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'Find the greatest common divisor of given numbers.'  # текст задания
    # logic_outputs_list = []  # кортеж для вывода функции
    print(task_text)
    while i < round_count:
        logic_outputs_list = logic_outputs()
        quest = logic_outputs_list[0]
        corr_ans = logic_outputs_list[1]
        i += 1
        print(f'Question: {quest}')
        user_ans = input('Your answer: ')
        if user_ans == corr_ans:
            print('Correct!')
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            break


    summary(i, round_count, name)  # Print game summary


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
