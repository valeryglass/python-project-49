#!/usr/bin/env python3
# file <brain_progression.py> brain_progression script

from brain_games.cli import welcome_user, summary
from brain_games.games.progression_logic import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_progression():
    t = game_drive()
    i = t[0]
    raund_count = t[1]
    summary(i, raund_count, name)  # Print game summary


def main():
    brain_progression()


if __name__ == '__main__':
    main()
