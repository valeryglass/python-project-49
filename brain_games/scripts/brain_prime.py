#!/usr/bin/env python3
# file <brain_prime.py> brain_prime game script

from brain_games.games.game_drive import game_drive


def brain_prime(game):
    game_drive(game)


def main():
    brain_prime('prime_logic')


if __name__ == '__main__':
    main()
