import random
from words import words
import string


def is_valid(word):
    """Check if chosen word is valid, otherwise choose another one"""
    while "-" in word or " " in word:
        random.choice(words)
    return word


# have computer choose valid random word from list
word = is_valid(random.choice(words)).upper()
word_set = set(word)

# define guessed letters 
letters_guessed = set()

# display word with dashes
def word_dashed(word):
    """Show only letters guessed in word, otherwise show dash"""
    dashed = [letter if letter in letters_guessed else '-' for letter in word]
    return ' '.join(dashed)

print(f"Hi ! Let's play hangman.\nHere's a peak: {word_dashed(word)}")

def guess():
    lives = 6
    while len(word_set) > 0 and lives > 0:
        try:
            letter = input("Guess a letter: ")[0].upper()
            if letter.isalpha():
                if letter in letters_guessed:
                    print(f"You guessed {letter} before! Try again")
                    print("Word: " + word_dashed(word))
                elif letter in word:
                    word_set.remove(letter)
                    letters_guessed.add(letter)
                    print("Letters used: " + ' '.join(letters_guessed))
                    print("Word: " + word_dashed(word))
                else:
                    lives -= 1
                    print(f"Too bad! {letter} is not in it. You have {lives} lives left", end=". ")
                    letters_guessed.add(letter)
                    print("Letters used: " + ' '.join(letters_guessed))
                    print("Word: " + word_dashed(word))                
            else:
                print("Wrong input! Try again")
        except IndexError:
            print("You need to input a letter!")
    if lives == 0:
        print(f"You lose! The word was {word}")
    else:
        print(f"Yay, you guessed the word {word}")

guess()