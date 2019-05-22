#!/usr/bin/python

import random

deck = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]

def checkSolution(input, goal):
    pass

def displayInfo(hand, goal):
    print 'Achieve:\t %i' %(goal)
    print 'Using:\t ',hand

def requestInput(hand):
    response = raw_input('Please input your solution: ')
    return response
    


def getInput(hand, goal):
    displayInfo(hand, goal)
    response = requestInput(hand)
    # Add Error Handling on Response
    return response

def initiateRound():
    deck_copy = random.shuffle(deck)
    hand = deck[0:5]
    goal = deck[5]
    return hand, goal



def turn():
    hand, goal = initiateRound()
    solved = False

    while (not solved):
        response = getInput(hand, goal)
        response
        solved = (eval(response) == goal)
        if(not solved):
            print 'That is incorrect. Try again!'

    print 'That is Correct! Congratulations!'



turn()
