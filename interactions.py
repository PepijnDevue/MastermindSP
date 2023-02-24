# general imports
import os
import time
import random

# file imports
from visuals import print_colours, colours
import board
import strategies

def player_take_guess():
    """
    let the player take a guess

    return: a list of 4 times one of the colours from the game
    """
    print("Take a guess between one of the following colours [{}B{}R{}G{}Y{}P{}W], an example guess would be 'BRGY'".format(print_colours['b'], print_colours['r'], print_colours['g'], print_colours['y'], print_colours['p'], print_colours['w']))
    while True:                                                 # let the player input a guess until it is a valid guess
        invalid_guess = False
        played_guess = input("Guess: ").lower()
        for i in played_guess:
            if i not in colours:
                invalid_guess = True
        if invalid_guess == False and len(played_guess) == 4:
            break
    return list(played_guess) 

def player_make_code():
    """
    let the player think of a code so the computer can guess it

    return: a list of 4 times one of the colours from the game
    """
    print("Think of a secret code containing only the following colours [{}B{}R{}G{}Y{}P{}W], an example code would be 'BRGY'\nIf you want to use a random code type 'x'".format(print_colours['b'], print_colours['r'], print_colours['g'], print_colours['y'], print_colours['p'], print_colours['w']))
    while True:                                                 # let the player input a code until it is a valid code
        invalid_code = False
        code = input("Secret code: ").lower()
        for i in code:
            if i not in colours:
                invalid_code = True
        if code == "x":
            code = board.generate_secret_code()
            break
        elif invalid_code == False and len(code) == 4:
            break
    return list(code)

def await_player_input():
    """
    let the script continue after the player has instructed to do so
    """
    input("Press enter to continue")            # the script will wait until the player has hit the enter key

def player_guesses():
    """
    This function lets the player play mastermind as the guesses

    return: None
    """
    os.system('CLS')                                    # clear the screen
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = board.generate_secret_code()          # generate random secret code
    start_time = time.time()
    while playing:                                      # keep playing until there are no guesses left or the code is guessed correctly
        current_guess = player_take_guess()
        guesses_left -= 1
        current_check = strategies.check_guess(current_guess, secret_code)            # get feedback for the player_guess
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game(current_check, guesses_left)
    print("It took {} seconds to play".format(round(time.time()-start_time, 2)))
    await_player_input()

def computer_guesses_simple():
    """
    This function lets the computer guess a secret code the player thought of by using the simple algorithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    while playing:
        current_guess = list(combinations[0])                                                       # guess the first combination that is possible
        guesses_left -= 1
        current_check = strategies.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    await_player_input()

def computer_guesses_expected_case():
    """
    This function lets the computer guess a secret code the player thought of by using the expected-case algorithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    while playing:
        if guesses_left == 8:
            current_guess = ['b', 'b', 'r', 'g']        # expected case has the standard starting guess of AABC, in this case its bbrg
        else:
            frequency_dict = strategies.generate_frequency_dict(combinations)
            current_guess = strategies.computer_guess(frequency_dict)
        guesses_left -= 1
        current_check = strategies.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    await_player_input()

def computer_guesses_new ():
    """
    This function adds the first guess of entropy to a variation of the simple strategy

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    random.shuffle(combinations)        # shuffling the list makes it so the player cannot play into the simple strategy its weakness
    while playing:
        if guesses_left == 8:
            current_guess = ['b', 'r', 'g', 'y']    # use the standard first guess of entropy to get the most information
        else:
            current_guess = list(combinations[0])
        guesses_left -= 1
        current_check = strategies.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    await_player_input()