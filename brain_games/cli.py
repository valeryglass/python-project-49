# file <cli.py> CLI logic

import prompt

# welcoming and KYC


def welcome_user(name):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


# calculating game summary


def summary(i, round_count, name):
    if i >= round_count:
        summary_text = print(f'Congratulations, {name}!')
        return summary_text    
    else:
        summary_text = print(f"Let's try again, {name}!")
        return summary_text


def main():
    welcome_user('')


if __name__ == '__main__':
    main()
