#!/usr/bin/env python3
# file <brain_progression.py> brain_progression script

from brain_games.games.game_drive import game_drive


def brain_progression(game):
    game_drive(game)


def main():
    brain_progression('prog_logic')


if __name__ == '__main__':
    main()
