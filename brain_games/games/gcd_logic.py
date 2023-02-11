# file <gcd_logic.py> brain-gcd logic

import random


def get_devisor_list(number):
    # make list of devisors for given number
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
    task_text = ('Find the greatest common divisor of '
                 'given numbers.')  # task text
    x = 1  # parameter for randomization
    y = 9  # parameter for randomization
    list_gcd_common = []  # list of common gcd
    first_number = random.randint(x, y)  # first element
    second_number = random.randint(x, y)  # second element
    gdl1 = get_devisor_list(first_number)  # list of first element devisors
    gdl2 = get_devisor_list(second_number)  # list of secondelement devisors
    list_gcd_common = list(set(gdl1) & set(gdl2))
    list_gcd_common.sort(reverse=True)
    quest = str(first_number) + ' ' + str(second_number)  # format quest text
    correct_answer = str(list_gcd_common[0])  # calculate correct answer
    print(list_gcd_common[0])
    print(list_gcd_common)
    print(correct_answer)
    return quest, correct_answer, task_text


def game_drive():
    # raund revolver
    i = 1  # raund index
    raund_count = 3  # max raund
    while i <= raund_count:
        logic_outputs_list = logic_outputs()
        quest = logic_outputs_list[0]
        correct_answer = logic_outputs_list[1]
        task_text = logic_outputs_list[2]
        if i == 1:
            print(f'{task_text}')
        i += 1
        print(f'Question: {quest}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            i = 0
            break
    return i, raund_count


def main():
    game_drive()


if __name__ == '__main__':
    main()
