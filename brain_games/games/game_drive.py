# file <game_drive.py> game-drive logic

from brain_games.games.calc_logic import logic_outputs as calc_logic
from brain_games.games.even_logic import logic_outputs as even_logic
from brain_games.games.gcd_logic import logic_outputs as gcd_logic
from brain_games.games.prime_logic import logic_outputs as prime_logic
from brain_games.games.progression_logic import logic_outputs as prog_logic


def game_drive(game):
    # raund revolver
    MAX_RAUND = 3  # max raund
    for raund_index in range(1, MAX_RAUND + 1):
        logic_outputs_module = game + '()'
        logic_outputs_list = eval(logic_outputs_module)
        quest = logic_outputs_list[0]
        correct_answer = logic_outputs_list[1]
        task_text = logic_outputs_list[2]
        if raund_index == 1:
            print(f'{task_text}')
        raund_index += 1
        print(f'Question: {quest}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            raund_index = 0
            break
    return raund_index, MAX_RAUND


def main():
    game_drive(game)


if __name__ == '__main__':
    main()
