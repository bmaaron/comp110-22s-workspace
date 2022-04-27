"""Solves wordle by eliminating the letters that are not present - using NO probabilities."""


guess = ""
feedback = ""
wordle_words = []

try: 
    with open('wordle_words.txt') as f:
        for line in f:
            wordle_words.append(line.strip())
except FileNotFoundError:
    print("file not found.")


for guesses in range(6):
    guess = input("\nword:").lower()
    print("g - green, y - yellow, w - wrong")
    feedback = input("Feedback").lower()
    if feedback == "gggggg":
        print("Well done! Guess", guesses + 1)

temp_tuple = tuple(wordle_words)

    for word in temp_tuple:
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                wordle_words.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                wordle_words.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                wordle_words.remove(word)
                break
                word
            elif feedback[i] == "y" and guess[i] == word[i]:
                wordle_words.remove(word)
                break
    

counter = 0 
for word in wordle_words:
    print(word, end=", ")
    counter += 1
    if counter == 8:
        print("")
        counter = 0