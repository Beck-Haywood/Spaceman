import random

letters_guessed = []
#display = ''   DOESNT NEED TO BE GLOBAL VARIABLE?

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return True
    return False

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def get_guessed_word(secret_word, letters_guessed):
    display = ""
    for i in secret_word:
        if i in letters_guessed:
            display +=i
        else:
            display+="_"

    return display

def is_guess_in_word(guess, secret_word):
    return guess in secret_word

def spaceman(secret_word):
    incorrect_guesses = len(secret_word)
    Game = True

    print(
        f"Welcome to Space Man user! In this guessing game you have {incorrect_guesses} chances to guess the secret word!")

    while incorrect_guesses > 0 and incorrect_guesses <= len(secret_word) and is_word_guessed(secret_word, letters_guessed) and Game == True:
        print(get_guessed_word(secret_word, letters_guessed))

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            Game = False
            break

        guess = user_input("Guess a letter! ").lower()
        print ('---------------------------------')

        if guess in secret_word:
            #This is so you can only guess one character!
                if len(guess) > 1:
                    print ("You may only guess 1 character!")
                    print ('---------------------------------')
                elif guess in letters_guessed:
                    print ("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                    print ('---------------------------------')
                else:
                    letters_guessed.append(guess)
                    print ('Good guess: ' + get_guessed_word(secret_word, letters_guessed))
                    print ('---------------------------------')
        else:
            if len(guess) > 1:
                    print ("You may only guess 1 character!")
                    print ('---------------------------------')
            elif guess in letters_guessed:
                print ("Oops! You've already guessed that letter: " + get_guessed_word(secret_word, letters_guessed))
                print ('---------------------------------')
            else:
                letters_guessed.append(guess)
                incorrect_guesses-= 1
                print ('Oops! That letter is not in the word: ' + get_guessed_word(secret_word, letters_guessed))
                #This line tells you how many guesses you have left after each incorrect guess.
                print("You have " + (str(incorrect_guesses)) + " guesses left!")
                print ('---------------------------------')

    if not is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
    else: #incorrect_guesses == 0:
        print('Sorry, you ran out of guesses. The word was ' + secret_word)
    
# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

print("""   
      .-     -.      _
     /    .----\\   _/ \\
   .-|   /:.   |  |   |
   |  \\  |:.   /.-'-./
   | .- -;:__.     =/
   .-=  *=|     _.=-
  /   _.  |    ;
 ;-.--|    \\   |
/   | \\    _\\  _\\
\\__/-._;.  ==- ==\\
         \\    \\   |
         /    /   /
         /-._/-._/
         \\    \\  \\
          `-._/._/  """)

print("""  .   ,- To the Moon Space Man!
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )

               ____
          .-'""p 8o""`-.
       .-'8888P'Y.`Y[ ' `-.
     ,']88888b.J8oo_      '`.
   ,' ,88888888888["        Y`.
  /   8888888888P            Y8\\
 /    Y8888888P'             ]88\\
:     `Y88'   P              `888:
:       Y8.oP '- >            Y88:
|          `Yb  __             `'|
:            `'d8888bo.          :
:             d88888888ooo.      ;
 \\            Y88888888888P     /
  \\            `Y88888888P     /
   `.            d88888P'    ,'
     `.          888PP'    ,'
       `-.      d8P'    ,-'   
          `-.,,_'__,,.-'
 """)
#All art came from this website I did not create this. https://www.asciiart.eu/space/spaceships




#Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
#Prompt the user to play again after a game ends. If they say yes, then start a new game.
#User guesses “c”, which results in an incorrect guess.
