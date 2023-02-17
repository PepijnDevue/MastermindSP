print_colours = {                                       # dict of pre-sets to print in different colours
    "b": "\033[1;36;1m",
    "r": "\033[1;31;1m",
    "g": "\033[1;32;1m",
    "y": "\033[1;33;1m",
    "p": "\033[1;35;1m",
    "w": "\033[1;37;1m"}

pin = "●"                                               # the character used to display a pin 

welcome_message = "Welc●me t● Mastermind!"              # a fun welcome message

colours = ["b", "r", "g", "y", "p", "w"]                # a list of colours used in the game
    
def display_welcome_message():
    for i in range(len(welcome_message)):
        print("{}{}".format(list(print_colours.values())[i % 6], welcome_message[i]), end="")

def set_white():
    print(print_colours["w"])

