# general imports
import os

# file imports
import board
import strategies
import visuals
import interactions   

def player_guesses():
    os.system('CLS')
    board = []
    guesses_left = 8
    playing = True
    secret_code = board.generate_secret_code()
    while playing:
        current_guess = interactions.player_take_guess()
        guesses_left -= 1
        current_check = board.check_player_guess(current_guess, secret_code)
        board = board.save_board(current_guess, current_check, board)
        board.display_board(board)
        print('You have {} guesses left'.format(guesses_left))
        playing = board.check_end_game(current_check, guesses_left)
        print("current_guess = {}\n guesses_left = {}\n current_check = {}\n board = {}\n playing = {}\n secret_code = {}".format(current_guess, guesses_left, current_check, board, playing, secret_code))
    choose_game_mode()

def computer_guesses_simple():
    print(strategies.make_combinations())
    print("not ready yet")

def computer_guesses_smart():
    print("not ready yet")

def choose_game_mode():
    os.system('CLS')
    for i in range(len(visuals.welcome_message)):
        print("{}{}".format(list(visuals.print_colours.values())[i % 6], visuals.welcome_message[i]), end="")
    print(visuals.print_colours["w"])
    print("\nChoose your game mode!!\n1. Player guesses\n2. Computer guesses simple\n3. Computer guesses smart")
    chosen = False
    while not chosen:
        game_mode_choice = int(input('Type [1, 2 or 3] to play: '))
        if game_mode_choice == 1:
            chosen = True
            player_guesses()
        elif game_mode_choice == 2:
            chosen = True
            computer_guesses_simple()
        elif game_mode_choice == 3:
            chosen = True
            computer_guesses_smart()
        else:
            print("Not a valid choice, please choose 1 2 or 3")


if __name__ == "__main__":
    choose_game_mode()