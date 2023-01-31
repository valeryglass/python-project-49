# file <even_logic.py> brain-even logic

import random

first_number = ''
second_number = ''
operator = ''
quest = ''
corr_ans = ''  # правильный ответ
operator_list = ['+', '-', '*']  # список операторов


def even_calc(x=0, y=9):
    quest = random.randint(x, y)  # строит вопрос
    if quest % 2 == 0:  # высчитывает правильный ответ
        corr_ans = 'yes'
    else:
        corr_ans = 'no'
    return quest, corr_ans


def main():
    even_calc('')


if __name__ == '__main__':
    main()
