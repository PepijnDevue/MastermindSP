import time
import random
import os

from visuals import print_colours, colours, pin

def generate_secret_code():
    """
    generates a random combination of any of the colours in the list colours, multiples allowed
    :return: the secret code as a string
    """
    secret_code = random.choices(colours, k=4)          # make a list of 4 times a random instance of the list
    return secret_code


def save_board(guess, check, board):
    board.append([guess, check])
    return board


def display_board(board):
    os.system('CLS')
    print("The answer to each guess is given as (x, y) \n x is the amount of pins that are the good colour on the correct place, y is the amount of good colours at incorrect places\n")
    for i in board:
        for j in i[0]:
            print("{}{}".format(print_colours[j], pin), end='')
        print("{}    {}\n".format(print_colours['w'], i[1]))


def check_end_game(check, guesses_left):
    if check[0] == 4:
        print("You won!")
        time.sleep(5)
        return False
    elif guesses_left == 0:
        print("You are out of guesses, try again!")
        time.sleep(5)
    return True
