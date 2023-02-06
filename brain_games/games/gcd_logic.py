# file <gcd_logic.py> brain-gcd logic

import random


def get_devisor_list(number):
    # make list of devisors for given parameter
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


def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    x = 0  # parameter for randomization
    y = 9  # parameter for randomization  
    list_gcd_common = []  # list of common gcd
    first_number = random.randint(x, y)  # first element
    second_number = random.randint(x, y)  # second element
    gdl1 = get_devisor_list(first_number)  # list of first element devisors
    gdl2 = get_devisor_list(second_number)  # list of secondelement devisors
    list_gcd_common = list(set(gdl1) & set(gdl2)) 
    list_gcd_common.sort(reverse=True)
    quest = str(first_number) + ' ' + str(second_number)  # format quest text
    corr_ans = str(list_gcd_common[0])  # calculate correct answer
    return quest, corr_ans


def main():
    logic_outputs()


if __name__ == '__main__':
    main()
