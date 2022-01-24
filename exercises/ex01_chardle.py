"""EX01 Chardle Project."""

__author__ = "730530687"


w: str = input("Enter a 5-character word: ")  # w = word
length_w: int = len(w)
if length_w != 5:
    print("Error: Word must contain 5 characters.")
    exit()
    
character: str = input("Enter a single chatacter: ")

length_character: int = len(character)
if length_character != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + w)
count: int = 0

if character == w[0]:
    print(character + " found at index 0")
    count = count + 1

if character == w[1]:
    print(character + " found at index 1")
    count = count + 1
    
if character == w[2]:
    print(character + " found at index 2")
    count = count + 1

if character == w[3]:
    print(character + " found at index 3")
    count = count + 1

if character == w[4]:
    print(character + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + character + " found in " + w)

if count == 1:
    print(str(count) + " instance of " + character + " found in " + w)

if count > 1:
    print(str(count) + " instances of " + character + " found in " + w)