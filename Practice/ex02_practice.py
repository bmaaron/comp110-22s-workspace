"""EX_02: One Shot Wordle."""

__author__ = "730530687"


SECRET_WORD: str = "python"
guess: str = input("What is your 6-letter guess? ")
guessing: bool = True

while guessing:
    guess_length: int = len(guess)
    SECRET_LENGTH: int = len(SECRET_WORD)

    if guess == SECRET_WORD:
        print("Woo! You got it!")
        guessing = False
        exit()

    elif guess_length == SECRET_LENGTH and guess != SECRET_WORD:
        print("Not quite. Play again soon!")
        guessing = False
        
    else:
        guess: str = input(f"That was not {SECRET_LENGTH} letters! Try again: ")
        if guess_length == SECRET_LENGTH:
            print("Not quite. Play again soon!")
            guessing = False
            