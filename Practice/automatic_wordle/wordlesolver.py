guess = ""
feedback = ""
guess_list = []

try:
    with open('wordle_words.txt') as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("file not found")
  
print("Good starter words are: slice, tried, crane")

for guesses in range(6):
    guess = input("\nword:").lower()
    print("g - green, y - yellow, w - wrong / grey")
    feedback = input("Feedback").lower()
    if feedback == "ggggg":
        print("Well Done! Guess",guesses+1)
        break
      
    temp_tuple = tuple(guess_list)
    for word in temp_tuple: # You can't iterate over a list you want to change, so using a tuple.
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "g" and guess[i] != word[i]:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] not in word:
                guess_list.remove(word)
                break
            elif feedback[i] == "y" and guess[i] == word[i]:
                guess_list.remove(word)
                break
      
    counter = 0
    for word in guess_list:
        print(word,end=", ")
        counter+=1
        if counter == 8:
            print("")
            counter = 0