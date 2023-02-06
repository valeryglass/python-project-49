# file <cli.py> CLI logic

import prompt


def welcome_user():
    # greet user and get his name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def summary(i, round_count, name):
    # calculate game summary and print it
    if i >= round_count:
        summary_text = print(f'Congratulations, {name}!')
        return summary_text
    else:
        summary_text = print(f'Let\'s try again, {name}!')
        return summary_text


def main():
    welcome_user()


if __name__ == '__main__':
    main()
