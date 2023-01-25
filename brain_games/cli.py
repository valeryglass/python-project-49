# file <cli.py> CLI logic

import prompt


def welcome_user(name):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def main():
    welcome_user('')


if __name__ == '__main__':
    main()
