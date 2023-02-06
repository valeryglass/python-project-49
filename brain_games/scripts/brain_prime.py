#!/usr/bin/env python3
# file <brain_prime.py> brain_prime game script

from brain_games.cli import welcome_user, summary
from brain_games.games.prime_logic import logic_outputs

# intro
print('Welcome to the Brain Games!')
name = welcome_user('')


def brain_prime():
#    user_ans = ''  # ответ пользователя
#    corr_ans = ''  # правильный ответ
    i = 1  # счетчик раундов
    round_count = 4  # количество раундов
    task_text = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # текст задания
#    logic_outputs_list = []  # список для вывода функции
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

# summary
    summary(i, round_count, name)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
