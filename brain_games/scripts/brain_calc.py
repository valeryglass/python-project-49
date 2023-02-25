#!/usr/bin/env python3
# file <brain_calc.py> brain_calc game script

from brain_games.games.game_drive import game_drive


def brain_calc(game):
    game_drive(game)


def main():
    brain_calc('calc_logic')


if __name__ == '__main__':
    main()
