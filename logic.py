clueline = []
from getchar import getchar
def get_clue():
    for i in word: 
        clueline.append('_')

    print("\nLet's play Hangman!\n")

    print(' '.join(clueline))


def play_game():
    guesstring = ''
    guesscount = 0
    while '_' in clueline:
        if guesscount > 5:
            print("Hangmand is dead after your 6 mistakes!")
            print("The word was {}".format(word))
            break
        guess = getchar()
        while guess.isalpha() == False:
            print("You must type a LETTER")
            guess = getchar()

        if guess.upper() in guesstring:
            print("you already tried {}".format(guess.upper()))
            continue
        elif guess.upper() in word:
            for i in range(len(word)):
                if word[i] == guess.upper():
                    clueline[i] = guess.upper()
        else :
            guesscount += 1
            if guesscount == 1 : print("Hangman lost a leg! 5 mistakes left")
            elif guesscount == 2 : print("Hangman lost his other leg! 4 mistakes left")
            elif guesscount == 3 : print("Hangman lost an arm! 3 mistakes left")
            elif guesscount == 4 : print("Hangman lost his other arm! 2 mistakes left")
            elif guesscount == 5 : print("Hangman lost his body! 1 mistake left")
            elif guesscount == 6 : print("Hangman lost his head! GAME OVER") 
            
        guesstring += guess.upper() 
        print("\n") 
        print(' '.join(clueline))
        print("\n")
        print("{} guesses left".format(6-guesscount))
        print("\nLetters you tried: {}\n".format(guesstring)) 
    else : 
        print("You've found the word!")
