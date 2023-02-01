# file <gcd_logic.py> brain-gcd logic

import random

# поиск всех четных делителей числа
def get_devisor_list(number):
    j = number
    i = 0
    devisors_list = []
    while j > 0:
        if number % (number - i) == 0:
            i += 1
            devisors_list.append(j)
            j -= 1
        else:
            i += 1
            j -= 1
            continue
    return devisors_list

# построение вопроса и поиск парвильного ответа
def gcd_calc(x=1, y=9):
    list_gcd_common = []
    first_number = random.randint(x, y)
    second_number = random.randint(x, y)
    gdl1 = get_devisor_list(first_number)
    gdl2 = get_devisor_list(second_number)
    list_gcd_common = list(set(gdl1) & set(gdl2))
    list_gcd_common.sort(reverse=True)
    quest = str(first_number) + ' ' + str(second_number)  # строит вопрос
    corr_ans = str(list_gcd_common[0])  # высчитывает правильный ответ
#    corr_ans = str(corr_ans)
    return quest, corr_ans


def main():
    gcd_calc('')


if __name__ == '__main__':
    main()
