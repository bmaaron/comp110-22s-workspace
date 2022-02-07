"""Less than 7 billion $ Wordle."""

__author__ = "730530687"

# secret: str = "codes"  
# secret_len: int = len(secret)
# guess: str = input(f"Enter a {secret_len} word: ")  


def contains_char(guess: str, char_in_guess: str) -> bool:
    """Searches for character in guess word."""
    exist: bool = False
    assert len(char_in_guess) == 1
    i: int = 0

    while not exist and i < len(guess):
        if guess[i] == char_in_guess:
            exist = True
        i = i + 1
    if exist:
        return True
    else: 
        return False


def emojified(guess: str, secret: str) -> str:
    """Purpose is to assign a colored box representing the chars location in guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    