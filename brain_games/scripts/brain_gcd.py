#!/usr/bin/env python3
# file <brain_gcd.py> brain_gcd game script

from brain_games.cli import welcome_user, summary
from brain_games.games.gcd_logic import game_drive


# intro
print('Welcome to the Brain Games!')
name = welcome_user()


def brain_gcd():
    t = game_drive()
    i = t[0]
    round_count = t[1]
    summary(i, round_count, name)  # Print game summary


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
