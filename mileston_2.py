import random

# Task 1: Create a list of words
list_of_words = ['apple', 'banana', 'orange', 'strawberry', 'watermelon']

print(list_of_words)

# Task 2: Choose a random word from the list
def get_random_word(word_list):
    return random.choice(word_list)

word = get_random_word(list_of_words)

print(word)

# Task 3: Create input for a letter
user_input_letter = input("Please enter a single letter: ")

# Task 4: Check the guessing letter length and is alphabetical
if len(user_input_letter) == 1 and user_input_letter.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")