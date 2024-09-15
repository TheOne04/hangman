import random


def main():
    # Loop until hangman complete or word guessed
    # Choose random word
    # Show hangman
    # Show blank
    # Show attempts
    # Ask for input
    # Parse and play
    pass


def print_hangman(wrong_attempts):
    hangman = [
        """
        +----
        |   |
        |
        |
        |
        |
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |
        |
        |
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |   |
        |
        |
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |   |
        |   |
        |
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |  /|
        |   |
        |
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |  /|
        |   |
        |  /
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |  /|
        |   |
        |  / \\
      __|____
      |     |__
      |_______|
    """,
        """
        +----
        |   |
        |   O
        |  /|\\
        |   |
        |  / \\
      __|____
      |     |__
      |_______|
    """,
    ]

    print(hangman[wrong_attempts])


def print_blanks(word, attempts):
    blank_string = ""

    for letter in word:
        if letter in attempts:
            blank_string += letter
        else:
            blank_string += "-"

    print(blank_string)
