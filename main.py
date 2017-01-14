#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from getchar import getchar
import logic #The Game logic
import pickword #Function wordpick()

def Quit():
    
    return 0

def GameOn():
    logic.word = pickword.wordpick()
    del logic.clueline
    logic.clueline = []

    logic.get_clue()

    logic.play_game()

    replay = ''
    print("Do you want to play again?"),
    while replay != "Y" or replay != "N":
        replay = getchar()
        if replay.upper() == "Y" : 
            GameOn()
        elif replay.upper() == "N":
            exit() 
        else :
            print("I'm expecting 'y' or 'n'")

GameOn()
