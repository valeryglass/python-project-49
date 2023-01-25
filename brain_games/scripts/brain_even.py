#!/usr/bin/env python3
# file <brain_even.py> brain_even game script

import prompt


num = 'rand'
corr_ans = ''
i = 1

print('Answer "yes" if the number is even, otherwise answer "no".')
print(f'Question: {num}')
ans = prompt.string('Your answer: ')

# получаем корректный результат
if (num % 2) == 0:
    corr_ans = 'yes'
else:
    corr_ans = 'no'

# счетчик правильных игр
while i < 4:
# сравниваем с ответом пользователя
    if ans = corr_ans:
        i = i + 1
        print('Correct!')
    else
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{corr_ans}'. Lets`s try again, {name}!")
        break
print('Congratulations, {name}!')
