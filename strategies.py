import itertools

from visuals import colours

def make_combinations():
    combinations = list(itertools.product(colours, repeat=4))
    return combinations