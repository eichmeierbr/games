#!/usr/bin/python

import random


# class krypto:

deck = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    

def getNumsFromResponse(input):
    input+=' '
    guessHand = []
    digitList = []
    for char in input:
        if(char.isdigit()):
            digitList.append(char)
        elif(digitList):
            num = int(''.join(digitList),10)
            guessHand.append(num)
            digitList = []

    return guessHand



def usesFullHand(input, hand_true):
    guessHand=[]
    hand = hand_true[:]
    # Extract all digits from input string .... This part breaks with double digit numbers
    guessHand= getNumsFromResponse(input)

    # Sort lists to facilitate comparison
    hand.sort()
    guessHand.sort()

    if guessHand == hand:
        return True
    else:
        informWhyBad(guessHand, hand)
        return False
    

def informWhyBad(guess, hand):
    print '\nYou entered an invalid input'

    if not len(guess)==len(hand):
        print 'Your input has %i numbers\n' %(len(guess))
    else:
        print 'Your input uses numbers not found in the hand\n'


def displayInfo(hand, goal):
    print 'Achieve:\t %i' %(goal)
    print 'Using:\t ',hand


def requestSolution(hand):
    response = raw_input('Please input your solution: ')
    return response
    


def getInput(hand, goal):
    haveGoodInput = False
    while not haveGoodInput:
        displayInfo(hand, goal) # Print hand and goal
        response = requestSolution(hand) # Obtain input from user
        haveGoodInput = usesFullHand(response, hand) # Check if input is good
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
        solved = (eval(response) == goal)
        if(not solved):
            print '\nThat is Incorrect. Try again!\n'

    print '\nThat is Correct! Congratulations!'



turn()
