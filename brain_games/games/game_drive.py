# file <game_drive.py> game-drive logic

from brain_games.cli import welcome_user, summary
from brain_games.games.calc_logic import logic_outputs as calc_logic
from brain_games.games.even_logic import logic_outputs as even_logic
from brain_games.games.gcd_logic import logic_outputs as gcd_logic
from brain_games.games.prime_logic import logic_outputs as prime_logic
from brain_games.games.progression_logic import logic_outputs as prog_logic


def print_task_text(task_text, raund_index):
    '''Print text of task'''
    print(task_text) if raund_index == 1 else None


def game_drive(game):
    '''Greet and led the user through the game'''
    # intro
    print('Welcome to the Brain Games!')
    name = welcome_user()
    MAX_RAUND = 3  # max raund
    for raund_index in range(1, MAX_RAUND + 1):  # round revolver
        logic_outputs_module = game + '()'  # build logic
        logic_outputs_list = eval(logic_outputs_module)  # get logic results
        quest = logic_outputs_list[0]
        correct_answer = logic_outputs_list[1]
        task_text = logic_outputs_list[2]
        print_task_text(task_text, raund_index)
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
    summary(raund_index, MAX_RAUND, name)  # Print game summary


def main():
    game_drive()


if __name__ == '__main__':
    main()
