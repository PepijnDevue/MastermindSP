# file imports
import board
import visuals
import interactions

def choose_game_mode():
    """
    This function lets the player choose between one of three game modes
    """
    visuals.set_white()
    game_mode = board.start_game()
    if game_mode == 1:
        interactions.player_guesses()
        choose_game_mode()          # play again after the game has finished
    elif game_mode == 2:
        interactions.computer_guesses_simple()
        choose_game_mode()
    elif game_mode == 3:
        interactions.computer_guesses_expected_case()
        choose_game_mode()
    else:
        interactions.computer_guesses_new()
        choose_game_mode()

if __name__ == "__main__":
    choose_game_mode()