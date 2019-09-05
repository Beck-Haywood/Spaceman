import random

# guess = ""
letters_guessed = []
display = ''
# Game = "onGoing"


def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    if "_" in display:
        return False
    else:
        return True


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def get_guessed_word(secret_word, letters_guessed):
    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    # display = ''

    # for character in secret_word:
    #     if character in letters_guessed:
    #         display += character
    #     else:
    #         display += "_ "
    # return display
    counter = 0
    display = ['_ ']*len(secret_word)
    for letter, guess in enumerate(secret_word):
        if guess in letters_guessed:
            counter += 1
            display.insert(letter-1, guess)
            display.pop(counter)
            if counter == len(secret_word):
                return ''.join(str(guess) for guess in display)
        else:
            counter += 1
            display.insert(counter-1, '_ ')
            display.pop(counter)
            if counter == len(secret_word):
                return ''.join(str(guess) for guess in display)

    return display