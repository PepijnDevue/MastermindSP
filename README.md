# Mastermind

This program allows users to play Mastermind, a classic code-breaking game, and also provides three different computer strategies for guessing the code.

## Getting Started

To run the program, you will need to have Python 3 installed on your computer. Run the `main.py` file to

## How to Play

When you run the program, you will be prompted to choose whether you want to be the code breaker or let the computer break the code. There are three different strategies to choose between for the latter.

After you have chosen your role, the game will begin. You will have a 8 turns to guess the code. On each turn, you will enter your guess and the computer will give you feedback on how close you are to the correct code.

Feedback will look like this (1,2). The first number tells how many colours you guessed in the correct position, the second numbers tells how many other colours are correct but in the wrong position.

## Computer Strategies

This program includes three different strategies that the computer can use to guess the code:

- Simple Strategy: The computer only listens to the feedback given to reduce the remaining possibilities but does not use logic to choose which of the those will be guessed.
- Expected Case Strategy: The computer listens to the feedback given to reduce the remaining possibilities and chooses its next guess based on which feedback is expected.
- Custom Strategy: This strategy is a mix of an adapted version of the simple strategy. It starts with the guess that would give the most information according to entropy and then proceeds using the simple strategy randomized.

To use a specific strategy, simply follow the prompts when starting the game.

## Authors

- [Pepijn](https://github.com/PepijnDevue)

## Acknowledgments

- [Mastermind on Wikipedia](https://en.wikipedia.org/wiki/Mastermind_(board_game))
- [Yet Another Mastermind Strategy](https://pure.rug.nl/ws/files/9871441/icgamaster.pdf)
- [Add Colour to Text in Python](https://ozzmaker.com/add-colour-to-text-in-python/)
- [Circle Symbols](https://www.alt-codes.net/circle-symbols)
