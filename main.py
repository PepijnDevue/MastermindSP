# general imports
import os

# file imports
import board
import strategies
import visuals
import interactions   

def player_guesses():
    os.system('CLS')
    playing_board = []
    guesses_left = 8
    playing = True
    secret_code = board.generate_secret_code()
    while playing:
        current_guess = interactions.player_take_guess()
        guesses_left -= 1
        current_check = board.check_player_guess(current_guess, secret_code)
        playing_board = board.save_board(current_guess, current_check, playing_board)
        board.display_board(playing_board)
        print('You have {} guesses left'.format(guesses_left))
        playing = board.check_end_game(current_check, guesses_left)
        print("current_guess = {}\n guesses_left = {}\n current_check = {}\n board = {}\n playing = {}\n secret_code = {}".format(current_guess, guesses_left, current_check, playing_board, playing, secret_code))
    choose_game_mode()

def computer_guesses_simple():
    print(strategies.make_combinations())
    print("not ready yet")

def computer_guesses_smart():
    print("not ready yet")

def choose_game_mode():
    board.start_game()
    visuals.set_white()
    game_mode = board.start_game()
    if game_mode == 1:
        player_guesses()
    elif game_mode == 2:
        computer_guesses_simple()
    else:
        computer_guesses_smart


if __name__ == "__main__":
    choose_game_mode()