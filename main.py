#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from getchar import getchar
import logic #The Game logic
import pickword #Function wordpick()

def GameOn():
    logic.word = pickword.wordpick()
    del logic.clueline
    logic.clueline = []

    logic.get_clue()

    logic.play_game()

    replay = ''
    print("Do you want to play again? Y/N")
    while replay != "Y" or replay != "N":
        replay = getchar()
        if replay.upper() == "Y" : 
            GameOn()
        elif replay.upper() == "N":
            print("Goodbye then!")
            break
        else :
            print("You've got a decision to take... Play again? Y/N")

GameOn()
