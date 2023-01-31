#!/usr/bin/env python3
# file <brain_even.py> brain_even game script

from brain_games.cli import welcome_user, summary
from brain_games.games.even_logic import even_calc

# intro
print('Welcome to Brain Games!')

# знакомство узнаем имя
name = welcome_user('')


def brain_even():
    user_ans = ''  # ответ пользователя
    corr_ans = ''  # правильный ответ
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    t = []
    print(task_text)
    while i < round_count:
        t = even_calc()
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

# # summary
    summary(i, round_count, name)


def main():
    brain_even()


if __name__ == '__main__':
    main()
