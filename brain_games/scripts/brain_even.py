#!/usr/bin/env python3
# file <brain_even.py> brain_even game script

import random
# from brain_games.cli import welcome_user

# welcome_user('')

print('Welcome to Brain Games!')
name = input('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    i = 1
    corr_ans = ''
    num = ''
    round_count = 4

    # счетчик правильных игр
    while i < round_count:
        # генерация и определения правильного результата
        num = random.randint(1, 9)
        if (num % 2) == 0:
            corr_ans = 'yes'
        else:
            corr_ans = 'no'
        print(f'Question: {num}')
        ans = input('Your answer: ')
        if ans != 'yes' and ans != 'no':
            print(f"'{ans}' is not a answer ;(. Lets`s try again, {name}!")
            break

    # сравниваем с ответом пользователя
        if ans == corr_ans:
            i = i + 1
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{corr_ans}'. Lets`s try again, {name}!")
            break

    # поздравляем если победитель
    if i >= round_count:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
