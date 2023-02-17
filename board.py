import time
import random
import os

import visuals

def generate_secret_code():
    """
    generates a random combination of any of the colours in the list colours, multiples allowed
    :return: the secret code as a string
    """
    secret_code = random.choices(visuals.colours, k=4)          # make a list of 4 times a random instance of the list
    return secret_code


def save_board(guess, check, playing_board):
    playing_board.append([guess, check])
    return playing_board


def display_board(playing_board):
    os.system('CLS')
    print("The answer to each guess is given as (x, y) \n x is the amount of pins that are the good colour on the correct place, y is the amount of good colours at incorrect places\n")
    for i in playing_board:
        for j in i[0]:
            print("{}{}".format(visuals.print_colours[j], visuals.pin), end='')
        print("{}    {}\n".format(visuals.print_colours['w'], i[1]))


def check_end_game(check, guesses_left):
    if check[0] == 4:
        print("You won!")
        time.sleep(5)
        return False
    elif guesses_left == 0:
        print("You are out of guesses, try again!")
        time.sleep(5)
    return True

def start_game():
    os.system('CLS')
    visuals.display_welcome_message()
    visuals.set_white()
    print("\nChoose your game mode!!\n1. Player guesses\n2. Computer guesses simple\n3. Computer guesses smart")
    chosen = False
    while not chosen:
        game_mode_choice = int(input('Type [1, 2 or 3] to play: '))
        if game_mode_choice < 4 or game_mode_choice > 0:
            chosen = True
            return game_mode_choice
        else:
            print("Not a valid choice, please choose 1 2 or 3")
