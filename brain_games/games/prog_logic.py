# file <prog_logic.py> brain-progression logic

import random

# построение прогрессии


def get_progression_list(d=1, a1=1, a0=10):
    progression = []
    n = 1
    while n < a0 + 1:
        an = a1 + (n - 1) * d
        progression.append(an)
        n += 1
    return progression

# построение вопроса и поиск парвильного ответа


def progression_calc():
    x = 1
    x1 = 5
    y = 10
    d = random.randint(x, y)  # сколько между
    a1 = random.randint(x, y)  # с какого начать
    a0 = random.randint(x1, y)  # сколько сделать
    progression = get_progression_list(d, a1, a0)
    p = random.randint(0, len(progression)-1)
    quest_raw = list(progression)
    corr_ans = str(quest_raw[p])
    quest_raw[p] = '..'
    quest = ' '.join(map(str, quest_raw))
    return quest, corr_ans


def main():
    progression_calc('')


if __name__ == '__main__':
    main()
