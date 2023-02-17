# imports
import os
import random
import time


print_colours = {                                                                                                                           # dict of pre-sets to print in different colours
    "b": "\033[1;36;1m",
    "r": "\033[1;31;1m",
    "g": "\033[1;32;1m",
    "y": "\033[1;33;1m",
    "p": "\033[1;35;1m",
    "w": "\033[1;37;1m"}

pin = "●"

welcome_message = "Welc●me t● Mastermind!"

colours = ["b", "r", "g", "y", "p", "w"]

def generate_secret_code():
    """
    generates a random combination of any of the colours in the list colours, multiples allowed
    :return: the secret code as a string
    """
    secret_code = random.choices(colours, k=4)
    return secret_code
    
def player_take_guess():
    print("Take a guess between one of the following colours [{}B{}R{}G{}Y{}P{}W], an example guess would be 'BRGY'".format(print_colours['b'], print_colours['r'], print_colours['g'], print_colours['y'], print_colours['p'], print_colours['w']))
    while True:
        invalid_guess = False
        played_guess = input("Guess: ").lower()
        for i in played_guess:
            if i not in colours:
                invalid_guess = True
        if invalid_guess == False and len(played_guess) == 4:
            break
    return list(played_guess)                                                                                                                # make a list of 4 times a random instance of the list

def check_player_guess(guess, secret_code):
    copy_guess = guess.copy()
    copy_code = secret_code.copy()
    check = [0, 0]
    for i in range(len(copy_guess)):
        if copy_guess[i] == copy_code[i]:
            copy_guess[i] = "X"
            copy_code[i] = 'x'
            check[0] += 1
    for i in range(len(copy_guess)):
        if copy_guess[i] in copy_code:
            print(copy_code, copy_guess, i)
            copy_code[copy_code.index(copy_guess[i])] = 'x'
            check[1] += 1
    return check

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

def player_guesses():
    os.system('CLS')
    board = []
    guesses_left = 8
    playing = True
    secret_code = generate_secret_code()
    while playing:
        current_guess = player_take_guess()
        guesses_left -= 1
        current_check = check_player_guess(current_guess, secret_code)
        board = save_board(current_guess, current_check, board)
        display_board(board)
        print('You have {} guesses left'.format(guesses_left))
        playing = check_end_game(current_check, guesses_left)
        print("current_guess = {}\n guesses_left = {}\n current_check = {}\n board = {}\n playing = {}\n secret_code = {}".format(current_guess, guesses_left, current_check, board, playing, secret_code))
    choose_game_mode()

def computer_guesses_simple():
    print("not ready yet")

def computer_guesses_smart():
    print("not ready yet")

def choose_game_mode():
    os.system('CLS')
    for i in range(len(welcome_message)):
        print("{}{}".format(list(print_colours.values())[i % 6], welcome_message[i]), end="")
    print(print_colours["w"])
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