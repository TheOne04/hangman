import random


def main():
    # Pick a random word from words
    with open("words.txt") as f:
        words = f.readlines()
    while True:
        word = random.choice(words).rstrip("\n")
        if word:
            break

    wrong_attempts = 0

    while True:
        # Initialize game
        print_hangman(wrong_attempts)
        print_blanks(word, attempts)
        print_wrong_attempts(word, attempts)
        letter = ask_letter(attempts)

        # Add to attempts and count wrong attempts
        if letter not in attempts:
            attempts.append(letter)
            if letter not in word:
                wrong_attempts += 1

        # Check if game over
        if wrong_attempts == 7:
            print_hangman(wrong_attempts)
            print_blanks(word, attempts)
            print_wrong_attempts(word, attempts)
            print("Game Over")
            break

        # Check for victory
        if guessed_word(word, attempts):
            print_hangman(wrong_attempts)
            print_blanks(word, attempts)
            print_wrong_attempts(word, attempts)
            print("You win!")
            break


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
        letter = input("Guess: ").lower()
        if letter.isalpha() and len(letter) == 1 and letter not in attempts:
            return letter


def guessed_word(word, attempts):
    for letter in set(word):
        if letter not in attempts:
            return False
    return True


def print_wrong_attempts(word, attempts):
    wrong_attempts = []
    for attempt in attempts:
        if attempt not in word:
            wrong_attempts.append(attempt)

    print("Wrong attempts: ", wrong_attempts)


main()
