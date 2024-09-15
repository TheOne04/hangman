import random


def main():
    word = "apple"
    attempts = []
    wrong_attempts = 0

    while True:
        print_hangman(wrong_attempts)
        print_blanks(word, attempts)
        letter = ask_letter(attempts)

        # Add to attempts and count wrong attempts
        if letter not in attempts:
            attempts.append(letter)
            if letter not in word:
                wrong_attempts += 1

        # Check if game over
        if wrong_attempts == 7:
            print_hangman(wrong_attempts)
            print("Game Over")
            break

        # Check for victory
        if guessed_word(word, attempts):
            print_hangman(wrong_attempts)
            print_blanks(word, attempts)
            print("You win!")
            break

    # Loop until hangman complete or word guessed
    # Choose random word
    # Show hangman
    # Show blank
    # Show attempts
    # Ask for input
    # Parse and play


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


def ask_letter(attempts):
    while True:
        letter = input("Guess: ")
        if letter.isalpha() and len(letter) == 1 and letter not in attempts:
            return letter


def guessed_word(word, attempts):
    for letter in set(word):
        if letter not in attempts:
            return False
    return True


main()
