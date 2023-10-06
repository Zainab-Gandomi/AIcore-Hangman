
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
            self.word = random.choice(word_list)
            self.word_guessed = ['_'] * len(self.word)
            self.num_letters = len(set(self.word))
            self.num_lives = num_lives
            self.list_letters = []

            print(f"The mystery word has {self.num_letters} characters")
            print(' '.join(self.word_guessed))


    def check_letter(self, guess) -> None:
        guess = guess.lower()
        if guess in self.word:
            print(f"good guess! {guess} is in the word")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")


    def ask_letter(self):
        while True:
            letter = input("Please enter a letter: ").lower()
            if len(letter) != 1:
                print("Please, enter just one character")
            elif letter in self.list_letters:
                print(f"{letter} was already tried")
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)
                break

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game.ask_letter()

    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")



if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list) 
