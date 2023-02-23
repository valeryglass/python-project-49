#!/usr/bin/env python3
# file <brain_calc.py> brain_calc game script

from brain_games.cli import welcome_user, summary
from brain_games.games.game_drive import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_calc(game):
    t = game_drive(game)
    i = t[0]
    raund_count = t[1]
    summary(i, raund_count, name)  # Print game summary


def main():
    brain_calc('brain_calc')


if __name__ == '__main__':
    main()
