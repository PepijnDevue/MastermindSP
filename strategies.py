# general imports
from itertools import product

# file imports
from visuals import colours
from interactions import check_guess, await_player_input

possible_feedback_dict = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0, (0, 4): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0, (2, 0): 0, (2, 1): 0, (2, 2): 0, (3, 0): 0, (4, 0): 0}


def make_combinations():
    """
    makes a list containing all possible colour combinations in the form of tuples

    return: the list of tuples
    """
    combinations = list(product(colours, repeat=4)) # use itertools.product to get a list of all possible combinations of 4 characters long only containing the six colours
    return combinations


def update_combinations(combinations, guess, check):
    """
    remove all combinations that don't add up with the given feedback

    combinations: a list of all combinations that are still possible, every combination is a tuple
    guess: a list containing the guess that was made
    check: a list containing the feedback that was given
    return: the updated list of possible combinations
    """
    index_combination = 0   # use whileloop and a counter to be able to change the counter based on whether or not a combination has been deleted
    while index_combination < len(combinations):
        combination_check = check_guess(guess, list(combinations[index_combination]))
        if combination_check != check:      # if the current combination would have gotten the same feedback, it could still be the secret_code
            del combinations[index_combination]
        else:
            index_combination += 1  # move to the next combination, otherwise all other combinations would have moved to the left
    return combinations

def computer_guess(combinations):
    """
    let the computer take the next guess out of the list using the expected_case strategy
    """
    frequency_dict = {}
    for guess_combination in combinations:
        frequency_dict[guess_combination] = possible_feedback_dict.copy()
        for code_combination in combinations:
            would_be_check = check_guess(list(guess_combination), list(code_combination))
            frequency_dict[guess_combination][(would_be_check[0], would_be_check[1])] += 1

    max_average = 1000
    max_average_guess = []
    for i in frequency_dict:
        frequency_list = []
        for j in frequency_dict[i]:
            if frequency_dict[i][j] != 0:
                frequency_list.append(frequency_dict[i][j])
        if sum(frequency_list)/len(frequency_list) < max_average:
            max_average = sum(frequency_list)/len(frequency_list)
            max_average_guess = i

    return list(max_average_guess)