# general imports
from itertools import product

# file imports
from visuals import colours
from interactions import check_guess

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