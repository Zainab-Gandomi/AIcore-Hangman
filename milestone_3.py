'''
#Iteratively checkif the input is a valid guess
while True:
    guess = input("Please guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guessed:", guess)


#check whether the guess is in the word
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")   
'''


# create function to run the checks
def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

    
def ask_for_input():
    while True:
        guess = input("Please guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Testing the code

while True:
    guessed_letter = ask_for_input()
    check_guess(guessed_letter)