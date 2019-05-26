#!/usr/bin/python

import random


class krypto:

    deck = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    hand = []
    goal = 0

    def getNumsFromResponse(self, input):
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



    def usesFullHand(self, input):
        guessHand=[]
        temp_hand = self.hand[:]
        # Extract all digits from input string .... This part breaks with double digit numbers
        guessHand= self.getNumsFromResponse(input)

        # Sort lists to facilitate comparison
        temp_hand.sort()
        guessHand.sort()

        if guessHand == temp_hand:
            return True
        else:
            self.informWhyBad(guessHand, temp_hand)
            return False
        

    def informWhyBad(self, guess, hand):
        print('\nYou entered an invalid input')

        if not len(guess)==len(hand):
            print('Your input has %i numbers\n' %(len(guess)))
        else:
            print('Your input uses numbers not found in the hand\n')


    def displayInfo(self):
        print('Achieve:\t %i' %(self.goal))
        print('Using:\t ',self.hand)


    def requestSolution(self):
        response = raw_input('Please input your solution: ')
        return response
        


    def getInput(self):
        haveGoodInput = False
        while not haveGoodInput:
            self.displayInfo() # Print hand and goal
            response = self.requestSolution() # Obtain input from user
            haveGoodInput = self.usesFullHand(response) # Check if input is good
        return response


    def initiateRound(self):
        deck_copy = self.deck[:]
        random.shuffle(deck_copy)
        self.hand = deck_copy[0:5]
        self.goal = deck_copy[5]

    def turn(self):
        self.initiateRound()
        solved = False

        while (not solved):
            response = self.getInput()
            solved = (eval(response) == self.goal)
            if(not solved):
                print('\nThat is Incorrect. Try again!\n')

        print('\nThat is Correct! Congratulations!')



game = krypto()
game.turn()