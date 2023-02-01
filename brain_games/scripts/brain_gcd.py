#!/usr/bin/env python3
# file <brain_gcd.py> brain_gcd game script

from brain_games.cli import welcome_user, summary
from brain_games.games.gcd_logic import gcd_calc


# intro
print('Welcome to the Brain Games!')

# знакомство узнаем имя
name = welcome_user('')


def brain_gcd():
    user_ans = ''  # ответ пользователя
    corr_ans = ''  # правильный ответ
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'Find the greatest common divisor of given numbers.'  # текст задания
    t = []  # кортеж для вывода функции

    print(task_text)
    while i < round_count:
        t = gcd_calc()
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
    brain_gcd()


if __name__ == '__main__':
    main()
