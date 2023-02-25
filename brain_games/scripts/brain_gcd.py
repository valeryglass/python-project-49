#!/usr/bin/env python3
# file <brain_gcd.py> brain_gcd game script

from brain_games.games.game_drive import game_drive


def brain_gcd(game):
    game_drive(game)


def main():
    brain_gcd('gcd_logic')


if __name__ == '__main__':
    main()
