import string
import random
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
           return False      
    return True

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    alphabet_remaining = list(string.ascii_lowercase)
    for letter in letters_guessed:
        alphabet_remaining.remove(letter)
    return "".join(alphabet_remaining)


def display_hangman(remaining_lives):
    return(IMAGES[8-remaining_lives])


def if_valid(ch):
    if (len(ch) == 1 and ch in string.ascii_lowercase) or ch == 'hint':
        return True   
    return False

count = 0
def show_letter_hint(secret_word, letters_guessed):
    global count
    while True:
        if count < 1:
            l=list(secret_word)
            for i in letters_guessed:
                if i in l:
                    for j in range(l.count(i)):
                        l.remove(i)
            count += 1
            return random.choice(l)
        else:
            return ("You are not allowed for more hints. ")


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8
    guessed = False

    while remaining_lives > 0 and remaining_lives <= 8 and not guessed:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            guessed = True
            break
        
        print("You have {} remaining lives. ".format(remaining_lives))
        print("Available letters: {} ".format(get_available_letters(letters_guessed)))
        
        guess = input("Please guess a letter: ")
        letter = if_valid(guess)
        if letter == True:

            if guess in secret_word:
                if guess in letters_guessed:
                    print("Oops! You have already guessed the letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
                else:
                    letters_guessed.append(guess)
                    print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
                    
            elif guess == "hint":
                print("Possible word matches are: {}".format(show_letter_hint(secret_word,letters_guessed)))
                
            else:
                if guess in letters_guessed:
                    print("Oops! You have already guessed the letter: {}".format(get_guessed_word(secret_word, letters_guessed)))
                else:
                    letters_guessed.append(guess)
                    remaining_lives -= 1
                    print("Oops! That letter is not in my word: {} ".format(get_guessed_word(secret_word, letters_guessed)))
                print(display_hangman(remaining_lives))

        else:
            print("Oops! Invalid Input. Please try again with right one.")

    if is_word_guessed(secret_word, letters_guessed) == True:
        print(" * * Congratulations, you won! * * ")
    else:
        if remaining_lives == 0:
            print("Sorry, you ran out of lives. The word was {}.".format(secret_word))


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program

secret_word = choose_word()
hangman(secret_word)
