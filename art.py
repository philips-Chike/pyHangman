def drawhangman(graphic):
    """This function receives the filename as a param. prints it"""
    with open(graphic,'r') as hangman:
        drawit = hangman.readlines()
    for i in drawit:
        print(i.strip('\n'))
