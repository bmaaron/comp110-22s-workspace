"""Classic ordered searching algorithm."""

low: float = 1
high: float = 100

print("Think of a number between 1-100")
input("Press enter to continue...")
playing: bool = True

while playing and low <= high:
    guess: float = (high + low) // 2
    print(str(guess) + "?")
    result: str = input("Reply yes, higher, lower: ")
    if result == "yes": 
        print("Woo!")
        playing = False
    elif result == "higher":
        low = guess + 1
    else:
        high = guess - 1