# general imports
from itertools import product

# file imports
from visuals import colours

def make_combinations():
    """
    makes a list containing all possible colour combinations in the form of tuples

    return: the list of tuples
    """
    combinations = list(product(colours, repeat=4)) # use itertools.product to get a list of all possible combinations of 4 characters long only containing the six colours
    return combinations