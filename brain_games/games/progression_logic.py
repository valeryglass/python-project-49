# file <prog_logic.py> brain-progression logic

import random


def get_progression_list(d=1, a1=1, a0=10):
    # make progression list from given parameters
    progression_list = []
    i = 1
    while i < a0 + 1:
        ai = a1 + (i - 1) * d
        progression_list.append(ai)
        i += 1
    return progression_list


def logic_outputs():
    # make 'quest' and 'correct answer' for specific task
    task_text = 'What number is missing in the progression?'  # task text
    x = 1  # parameter for randomization
    x1 = 5  # parameter for randomization
    y = 10  # parameter for randomization
    d = random.randint(x, y)  # gap between elements
    a1 = random.randint(x, y)  # start element
    a0 = random.randint(x1, y)  # amout of elements
    progression_list = get_progression_list(d, a1, a0)
    p = random.randint(0, len(progression_list) - 1)  # index of hidden element
    quest_raw = list(progression_list)
    correct_answer = str(quest_raw[p])
    quest_raw[p] = '..'
    quest = ' '.join(map(str, quest_raw))  # format quest text
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
