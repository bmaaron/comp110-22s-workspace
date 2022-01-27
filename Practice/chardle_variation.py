"""EX01 Chardle Project."""

__author__ = "730530687"


number: str = input("Enter a number: ")  # w = word
length_number: int = len(number)
if length_number <= 5:
    print("Error: Word must contain at least 5 integers.")
    exit()
    
character: str = input("Enter a single number: ")

length_character: int = len(character)
if length_character != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character + " in " + number)
count: int = 0

if character == number[0]:
    print(character + " found at index 0")
    count = count + 1

if character == number[1]:
    print(character + " found at index 1")
    count = count + 1
    
if character == number[2]:
    print(character + " found at index 2")
    count = count + 1

if character == number[3]:
    print(character + " found at index 3")
    count = count + 1

if character == number[4]:
    print(character + " found at index 4")
    count = count + 1

if count == 0:
    print("No instances of " + character + " found in " + number)

if count == 1:
    print(str(count) + " instance of " + character + " found in " + number)

if count > 1:
    print(str(count) + " instances of " + character + " found in " + number)