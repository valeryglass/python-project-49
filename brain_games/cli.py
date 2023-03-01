# file <cli.py> CLI logic

import prompt


def welcome_user():
    '''Greet user and get his name'''
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def summary(i, raund_count, name):
    '''Calculate game summary and print it'''
    if i == raund_count + 1:
        return print(f'Congratulations, {name}!')
    else:
        return print(f'Let\'s try again, {name}!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
