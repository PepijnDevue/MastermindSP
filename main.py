# general imports
import os
import time
import random

# file imports
import board
import strategies
import visuals
import interactions   

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
        current_guess = interactions.player_take_guess()
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)            # get feedback for the player_guess
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game(current_check, guesses_left)
    print("It took {} seconds to play".format(round(time.time()-start_time, 2)))
    interactions.await_player_input()
    choose_game_mode()                                  # return to the option screen to play again when done

def computer_guesses_simple():
    """
    This function lets the computer guess a secret code the player thought of by using the simple algorithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = interactions.player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    while playing:
        current_guess = list(combinations[0])                                                       # guess the first combination that is possible
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    interactions.await_player_input()
    choose_game_mode()

def computer_guesses_expected_case():
    """
    This function lets the computer guess a secret code the player thought of by using the expected-case algorithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = interactions.player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    while playing:
        if guesses_left == 8:
            current_guess = ['b', 'b', 'r', 'g']
        else:
            current_guess = strategies.computer_guess(combinations)
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    interactions.await_player_input()
    choose_game_mode()

def computer_guesses_pepijn():
    """
    
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = interactions.player_make_code()
    start_time = time.time()
    combinations = strategies.make_combinations()
    random.shuffle(combinations)
    while playing:
        if guesses_left == 8:
            current_guess = ['b', 'r', 'g', 'y']
        else:
            current_guess = list(combinations[0])
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    print("It took {} seconds to run".format(round(time.time()-start_time, 2)))
    interactions.await_player_input()
    choose_game_mode()

def choose_game_mode():
    """
    This function lets the player choose between one of three game modes
    """
    visuals.set_white()
    game_mode = board.start_game()
    if game_mode == 1:
        player_guesses()
    elif game_mode == 2:
        computer_guesses_simple()
    elif game_mode == 3:
        computer_guesses_expected_case()
    else:
        computer_guesses_pepijn()


if __name__ == "__main__":
    choose_game_mode()