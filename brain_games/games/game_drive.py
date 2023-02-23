# file <game_drive.py> game-drive logic

from brain_games.games.calc_logic import logic_outputs as calc_logic
from brain_games.games.even_logic import logic_outputs as even_logic
from brain_games.games.gcd_logic import logic_outputs as gcd_logic
from brain_games.games.prime_logic import logic_outputs as prime_logic
from brain_games.games.progression_logic import logic_outputs as prog_logic


def game_drive(game):
    # raund revolver
    i = 1  # raund index
    raund_count = 3  # max raund
    while i <= raund_count:
        logic_outputs_module = game + '()'
        logic_outputs_list = eval(logic_outputs_module)
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
    game_drive(game)


if __name__ == '__main__':
    main()
