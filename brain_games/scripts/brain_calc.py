#!/usr/bin/env python3
# file <brain_calc.py> brain_calc game script

from brain_games.cli import welcome_user, summary
from brain_games.games.calc_logic import logic_outputs


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_calc():
    # user_ans = ''  # ответ пользователя
    # corr_ans = ''  # правильный ответ
    # operator_list = ['+', '-', '*']  # список операторов
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'What is the result of the expression?'
    # logic_outputs_list = []
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
    brain_calc()


if __name__ == '__main__':
    main()
