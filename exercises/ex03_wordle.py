"""Less than 7 billion $ Wordle."""

__author__ = "730530687"

  
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
    answer: str = ""
    i: int = 0  
    secret_len: int = len(secret)

    while i < secret_len:
        if secret[i] == guess[i]:
            answer = answer + GREEN_BOX 
            
        else: 
            exist: bool = False
            if contains_char(secret, guess[i]):
                exist = True
            if exist:
                answer = answer + YELLOW_BOX
            else:
                answer = answer + WHITE_BOX
        i = i + 1

    return answer 


def input_guess(expected_length: int) -> str:
    """Give integer an expected length of a guess as a parameter."""
    guess: str = input(f"Enter a {expected_length} character word: ")  
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
        
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    x: int = 1
    secret: str = "codes"
    secret_len: int = len(secret)
    guess: str = "" 
    while x <= 6 and guess != secret: 
        print(f"=== Turn {x}/6 ===")
        guess = input_guess(secret_len)
        print(emojified(guess, secret))
        x = x + 1

    if guess == secret:
        print(f"You won in {x - 1}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")
        

if __name__ == "__main__":
    main()