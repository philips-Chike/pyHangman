import random

def wordpick():
    with open('sowpods.txt','r') as sowpod:
        words = sowpod.readlines()

    return random.choice(words).strip()    
