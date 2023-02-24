#!/usr/bin/env python3
# file <brain_calc.py> brain_calc game script

from brain_games.cli import welcome_user, summary
from brain_games.games.game_drive import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_calc(game):
    t = game_drive(game)
    raund_index = t[0]
    MAX_RAUND = t[1]
    summary(raund_index, MAX_RAUND, name)  # Print game summary


def main():
    brain_calc('calc_logic')


if __name__ == '__main__':
    main()
