#!/usr/bin/ev python3
# file <brain_prog.py> brain_prog script

from brain_games.cli import welcome_user, summary
from brain_games.games.prog_logic import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_prog():
    i = 1  # round index
    round_count = 4  # max round
    t = game_drive()
    i = t[0]
    round_count = t[1]
    summary(i, round_count, name)  # Print game summary


def main():
    brain_prog()


if __name__ == '__main__':
    main()
    