#!/usr/bin/env python3
# file <brain_even.py> brain_even game script

from brain_games.cli import welcome_user, summary
from brain_games.games.game_drive import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_even(game):
    t = game_drive(game)
    i = t[0]
    raund_count = t[1]
    summary(i, raund_count, name)  # Print game summary


def main():
    brain_even('brain_even')


if __name__ == '__main__':
    main()
