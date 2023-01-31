#!/usr/bin/env python3
# file <brain_calc.py> brain_calc game script

from brain_games.cli import welcome_user, summary
from brain_games.games.calc_logic import random_calc


# intro
print('Welcome to the Brain Games!')

# знакомство узнаем имя
name = welcome_user('')


def brain_calc():
    user_ans = ''  # ответ пользователя
    corr_ans = ''  # правильный ответ
#    operator_list = ['+', '-', '*']  # список операторов
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'What is the result of the expression?'
    t = []

    print(task_text)
    while i < round_count:
        t = random_calc()
        quest = t[0]
        corr_ans = t[1]
        i += 1
        print(f'Question: {quest}')
        user_ans = input('Your answer: ')
        if user_ans == corr_ans:
            print('Correct!')
        else:
            print(f"'{user_ans}' is wrong answer ;(. Correct answer was '{corr_ans}'.")
            break

# summary
    summary(i, round_count, name)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
