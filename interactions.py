# file imports
from visuals import print_colours, colours
from board import generate_secret_code

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


def check_guess(guess, secret_code):
    """
    generate feedback to the guess with a given secret_code

    guess: a list of 4 times on of the colours form the game that needs to be checked
    secret_code: the code that the feedback is based on
    return: a list of two ints containing the feedback
    """
    copy_guess = guess.copy()
    copy_code = secret_code.copy()
    check = [0, 0]
    for i in range(len(copy_guess)):                            # first look for pins with right colours at the correct place
        if copy_guess[i] == copy_code[i]:
            copy_guess[i] = "X"                                 # replace those pins with marks to avoid confusion for the second part
            copy_code[i] = 'x'
            check[0] += 1
    for i in range(len(copy_guess)):                            # now look for right colours at incorrect places
        if copy_guess[i] in copy_code:
            copy_code[copy_code.index(copy_guess[i])] = 'x'     # replace the pin again with a mark
            check[1] += 1
    return check


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
            code = generate_secret_code()
            break
        elif invalid_code == False and len(code) == 4:
            break
    return list(code)

def await_player_input():
    """
    let the script continue after the player has instructed to do so
    """
    input("Press enter to continue")            # the script will wait until the player has hit the enter key