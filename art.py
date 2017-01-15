def drawhangman(err=0):
    """This function prints the hangman corresponding to the error amount"""
    if err == 0 :  hman = ("  |       ","  |       ","  |       ")
    elif err == 1: hman = ("  |    O  ","  |       ","  |       ")
    elif err == 2: hman = ("  |    O  ","  |    |  ","  |       ")
    elif err == 3: hman = ("  |    O  ","  |   /|  ","  |       ")
    elif err == 4: hman = ("  |    O  ","  |   /|\\","  |       ")
    elif err == 5: hman = ("  |    O  ","  |   /|\\","  |   /   ")
    elif err == 6: hman = ("  |    O  ","  |   /|\\","  |   / \\")
    top =   ("  ______  ","  |    |  ")
    bottom =("  |       ","__|____   ","|      |___","|_________|")
    
    for i in top:
        print(i)
    for i in hman:
        print(i)
    for i in bottom:
        print(i)
