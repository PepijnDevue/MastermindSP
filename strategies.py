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
    index_combination = 0
    while index_combination < len(combinations):
        combination_check = check_guess(guess, list(combinations[index_combination]))
        if combination_check != check:
            del combinations[index_combination]
        else:
            index_combination += 1
    return combinations