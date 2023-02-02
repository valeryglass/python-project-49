#!/usr/bin/env python3
# file <brain_prog.py> brain_progression game script

from brain_games.cli import welcome_user, summary
from brain_games.games.prog_logic import progression_calc

# intro
print('Welcome to the Brain Games!')

name = welcome_user('')


def brain_progression():
    user_ans = ''  # ответ пользователя
    corr_ans = ''  # правильный ответ
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'What number is missing in the progression?'  # текст задания
    t = []  # список для вывода функции

    print(task_text)
    while i < round_count:
        t = progression_calc()
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
    brain_progression()


if __name__ == '__main__':
    main()
