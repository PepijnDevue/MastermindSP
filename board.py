# general imports
import time
import random
import os

# file imports
import visuals

def generate_secret_code():
    """
    generates a random combination of any of the colours in the list colours, multiples allowed
    :return: the secret code as a string
    """
    secret_code = random.choices(visuals.colours, k=4)          # make a list of 4 times a random instance of the list
    return secret_code


def save_board(guess, check, playing_board):
    """
    saves the move and check that have been mode together with previous moves

    guess: a list of four characters from the six colours that will be saved as guess
    check: a list of two ints representing feedback to the guess that will be saved as guess
    playing_board: a list of lists, every list represents one turn and contains a guess and a check
    return: the list of lists with the current turn (guess and check) added
    """
    playing_board.append([guess, check])
    return playing_board


def display_board(playing_board, guesses_left):
    """
    displays all previous turns and the amount of guesses left after clearing the terminal

    playing_board: a list of lists containing all the turns played
    guesses left: an int telling how many guesses the player has left
    return: None
    """
    os.system('CLS')                                                    # clear the screen
    print("The answer to each guess is given as (x, y) \n x is the amount of pins that are the good colour on the correct place, y is the amount of good colours at incorrect places\n")
    for turn in playing_board:                                          # loop through the turns and display the guess of that turn and the feedback given                                  
        for pin in turn[0]:
            print("{}{}".format(visuals.print_colours[pin], visuals.pin), end='')       # print a pin in the colour needed by using the colour-preset
        print("{}    {}\n".format(visuals.print_colours['w'], turn[1]))                 # print the feedback in white
    print('You have {} guesses left'.format(guesses_left))


def check_end_game(check, guesses_left):
    """
    checks whether the game has ended, if so, handle the ending of the game

    check: a list containing feedback given for the current guess
    guesses_left: an int telling how many guesses the player has left
    return: a boolean telling if the game has ended
    """
    if check[0] == 4:                                   # if 4 pins with placed with the correct colour on the correct positions, the player has won
        print("You won!")
        time.sleep(5)
        return False
    elif guesses_left == 0:
        print("You are out of guesses, try again!")
        time.sleep(5)
        return False
    return True

def start_game():
    """
    start the game by welcoming the player and letting the player choose a gamemode

    return: an int that corresponds to a gamemode
    """
    os.system('CLS')
    visuals.display_welcome_message()
    visuals.set_white()
    print("\nChoose your game mode!!\n1. Player guesses\n2. Computer guesses simple\n3. Computer guesses smart")
    chosen = False
    while not chosen:                               # let the player choose one of the gamemodes, keep repeating untill the choice is clear
        game_mode_choice = int(input('Type [1, 2 or 3] to play: '))
        if game_mode_choice < 4 or game_mode_choice > 0:
            chosen = True
            return game_mode_choice
        else:
            print("Not a valid choice, please choose 1 2 or 3")
