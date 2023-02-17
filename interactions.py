from visuals import print_colours, colours

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
    return list(played_guess) 


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