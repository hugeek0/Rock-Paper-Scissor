from config import CHOICES, rules, score_board
from random import choice
from decorator import log_time


def system_choice():
    return choice(CHOICES)


def user_choice():
    answer = input("enter your choice (p, r, s):")
    if answer not in CHOICES:
        print("wrong answer")
        return user_choice()
    return answer


def find_winner(user, system):
    result = {user, system}
    if len(result) == 1:
        return None

    return rules[tuple(sorted(result))]


def update_scoreboard(result):
    if result["user"] == 3:
        score_board["user"] += 1
        msg = "you win"
    else:
        score_board["system"] += 1
        msg = "system wins"

    print("#" * 20)
    print(
        f'{msg.upper():^20}\n##  user_score:{score_board["user"]}  ##\n'
        f'## system_score:{score_board["system"]} ##')
    print("#" * 20)


def play():
    result = {"user": 0, "system": 0}

    while result["user"] < 3 and result["system"] < 3:
        user_ch = user_choice()
        system_ch = system_choice()
        winner = find_winner(user_ch, system_ch)
        if winner is None:
            print(f'equal\nuser:{result["user"]}\tsystem:{result["system"]}')

        elif winner == user_ch:
            result["user"] += 1
            print(
                f'you are winner :)\nuser:{result["user"]}\tsystem:{result["system"]}')
        else:
            result["system"] += 1
            print(
                f'system is winner\nuser:{result["user"]}\tsystem:{result["system"]}')

    update_scoreboard(result)
    play_again = input("do you wanna play again(y, n):")
    if play_again == "y":
        play()


@log_time
def game():
    play()


game()
