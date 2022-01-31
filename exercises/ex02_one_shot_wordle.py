"""EX_02: One Shot Wordle."""

__author__ = "730530687"


secret: str = "python"  
secret_len: int = len(secret)
guess: str = input(f"What is your {secret_len}-letter guess? ")  
i = 0
answer = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != secret_len:
    guess = input(f"That was not {secret_len} letters! Try again: ")

while i < secret_len:
    if secret[i] == guess[i]:
        answer = answer + GREEN_BOX 
        
    else: 
        exist: bool = False
        i_2: int = 0
        while not exist and i_2 < secret_len: 
            if secret[i_2] == guess[i]:
                exist = True
            i_2 = i_2 + 1
        if exist:
            answer = answer + YELLOW_BOX
        else:
            answer = answer + WHITE_BOX
    i = i + 1
if guess == secret:
    print(f"{answer} \n Woo! You got it!")
else: 
    print(f"{answer} \n Not quite. Play again soon!")