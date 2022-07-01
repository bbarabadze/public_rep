from rich import print as r_print
from words import utf_list_big
from words import utf_list
from random import choice
import os


def is_valid(user_input):
    return user_input.strip() in utf_list or user_input.strip() in utf_list_big


def compare(user_w, the_w):
    flags = [0] * 5
    for index in range(5):
        if user_w[index] == the_w[index]:
            flags[index] = 1
    for index in range(5):
        if flags[index]:
            the_w[index] = None
    for index in range(5):
        if not flags[index] and (user_w[index] in the_w):
            flags[index] = 2
    return flags


def print_lines(lin):
    for line in lin:
        r_print(line)


def formatting(comp_res, user_w, st, lin):
    for index in range(5):
        if comp_res[index] == 1:
            user_w[index] = f"[bold green]{user_w[index]}[/bold green]"
        elif comp_res[index] == 2:
            user_w[index] = f"[bold yellow]{user_w[index]}[/bold yellow]"
        else:
            user_w[index] = f"[grey]{user_w[index]}[/grey]"
    lin[st] += ' '.join(user_w)
    return lin


def main():
    the_word = choice(utf_list)
    win = lose = False
    lines = ["ცდა N1: ", "ცდა N2: ", "ცდა N3: ", "ცდა N4: ", "ცდა N5: ", "ცდა N6: "]
    stage = 1
    os.system('cls')
    print_lines(lines)

    while not lose and not win:
        user_word = input("შეიყვანეთ თქვენი ვერსია:").strip()
        os.system('cls')
        if is_valid(user_word):
            comparison_result = compare(list(user_word), list(the_word))
            lines = formatting(comparison_result, list(user_word), stage - 1, lines)
            print_lines(lines)
            stage += 1
            win = comparison_result.count(1) == 5
            lose = stage == 7
        else:
            print_lines(lines)
            r_print("[bold red]შეუსაბამო სიტყვაა, სცადეთ თავიდან[/bold red]")

    if win:
        r_print(f"[bold green]თქვენ მოიგეთ {stage - 1} ცდაში[/bold green]")
    else:
        r_print(f"[bold red]წააგეთ, სიტყვა იყო [/bold red][bold green]{the_word}[/bold green]")

    return input("გნებავთ თავიდან? (y/n)").strip().lower() in ['y', 'ყ']


if __name__ == '__main__':
    while main():
        pass
