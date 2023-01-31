# file <calc_logic.py> brain-calc logic

import random

first_number = ''
second_number = ''
operator = ''
quest = ''
corr_ans = ''  # правильный ответ
operator_list = ['+', '-', '*']  # список операторов


def random_calc(x=0, y=9):
    first_number = random.randint(x, y)
    second_number = random.randint(x, y)
    operator = random.choice(operator_list)
    quest = str(first_number) + ' ' + operator + ' ' + str(second_number)  # строит вопрос
    corr_ans = str(eval(quest))  # высчитывает правильный ответ
    return quest, corr_ans


def main():
    random_calc('')


if __name__ == '__main__':
    main()
