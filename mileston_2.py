import random

#task 1:  creat list of word
word_list  = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']

print(word_list)

#task 2: choose a random word from word_list
word = random.choice(word_list)

print(word)

#task 3: create input for letter
guess = input("pleaase enter a single letter: ")

# task 4: check the guessing letter length and is alphabetical
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")