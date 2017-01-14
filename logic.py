clueline = []
from getchar import getchar
import art

def get_clue():
    for i in word: 
        clueline.append('_')

def play_game():
    graphic = 'hangman'
    drawhangman = art.drawhangman(graphic)
    print("Word: "),
    print(' '.join(clueline))

    guesstring = ''
    guesscount = 0
    while '_' in clueline:
        if guesscount > 5:
            print("Sorry, The word was {}".format(word))
            break
        print("Guess: "),
        guess = getchar()
        while guess.isalpha() == False:
            print("{} is not a valid guess.".format(guess))
            print("Guess: "),
            guess = getchar()
        else : print(guess)

        if guess.upper() in guesstring:
            print("you already tried {}".format(guess.upper()))
            continue
        elif guess.upper() in word:
            for i in range(len(word)):
                if word[i] == guess.upper():
                    clueline[i] = guess.upper()
        else :
            guesscount += 1
            graphic = 'hangman' + str(guesscount)
            
        guesstring += guess.upper() 
        drawhangman = art.drawhangman(graphic)
        print("\nWord: "),
        print(' '.join(clueline))
        #print("{} guesses left".format(6-guesscount))
        print("Guesses: {}".format(guesstring)) 
    else : 
        print("You've found the word!")
