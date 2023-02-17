# general imports
import os

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
    secret_code = board.generate_secret_code()          # generate random code
    while playing:                                      # keep playing untill there are no guesses left or the code is guessed correctly
        current_guess = interactions.player_take_guess()
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)             # get feedback for the player_guess
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game(current_check, guesses_left)
        # debug print("current_guess = {}\n guesses_left = {}\n current_check = {}\n board = {}\n playing = {}\n secret_code = {}".format(current_guess, guesses_left, current_check, playing_board, playing, secret_code))
    choose_game_mode()                                  # return to the option screen to play again when done

def computer_guesses_simple():
    """
    This function lets the computer guess a secret code the player thought of by using the simple alogirithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = interactions.player_make_code()
    combinations = strategies.make_combinations()
    while playing:
        current_guess = list(combinations[0])                                                       # guess the first combination that is possible
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    choose_game_mode()

def computer_guesses_smart():
    """
    This function lets the computer guess a secret code the player thought of by using the excpected-case alogirithm

    return: None
    """
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = interactions.player_make_code()
    combinations = strategies.make_combinations()
    while playing:
        current_guess = strategies.computer_guess(combinations)
        guesses_left -= 1
        current_check = interactions.check_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board, guesses_left)
        playing = board.check_end_game_computer(current_check, guesses_left)
        combinations = strategies.update_combinations(combinations, current_guess, current_check)
    

def choose_game_mode():
    """
    This function lets the player choose between one of three gamemodes
    """
    visuals.set_white()
    game_mode = board.start_game()
    if game_mode == 1:
        player_guesses()
    elif game_mode == 2:
        computer_guesses_simple()
    else:
        computer_guesses_smart()


if __name__ == "__main__":
    choose_game_mode()