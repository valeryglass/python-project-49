#!/usr/bin/env python3
# file <brain_even.py> brain_even game script

from brain_games.games.game_drive import game_drive


def brain_even(game):
    game_drive(game)


def main():
    brain_even('even_logic')


if __name__ == '__main__':
    main()
