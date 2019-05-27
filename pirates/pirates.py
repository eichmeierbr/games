import math


def getGameStats():
    numPlayers=input('How many people are playing? ')
    numDice=input('How many dice do you start with? ')
    totalDice=numPlayers*numDice
    return numPlayers,numDice,totalDice


# x: Number of successes
# n: Number of trials
# p: Probability of a single trial
def binomialFunc(n,p,x):
        percent=math.factorial(n)/math.factorial(x)/math.factorial(n-x)*math.pow(p,x)*math.pow(1-p,n-x)
        return percent


# diceRemaining: The total number of dice on the table
# betNumber: The number on the dice being guessed
# betCount: The number of dice rolling the betNumber
def getProbability(diceRemaining,betNumber,betCount):
        probability=0
        currentCount=betCount

        if betNumber==1:
                while currentCount <=diceRemaining:
                        probability+=binomialFunc(diceRemaining,0.1667,currentCount)
                        currentCount+=1
        else:
                while currentCount <=diceRemaining:
                        probability+=binomialFunc(diceRemaining,0.3333,currentCount)
                        currentCount+=1

        return probability
        

def getBetInfo():
    betCount=input('What is the number of dice? ')
    betNumber=input('What is the dice value? ')
    return betNumber, betCount

def yourDice():
        numberOfDice=input('How many dice do you have? ')
        dice = []
        count=1
        while count<=numberOfDice:
                dice.append(input('Enter your die # %i: ' %(count))) 
                count+=1
        print ''
        return numberOfDice, dice


def reduceBet(betNumber,betCount,myDice):
        for die in myDice:
                if die == betNumber or die ==1:
                        betCount-=1
        return betCount



def printIncludeYourDiceStats(remainingDice):
    print 'Consider Your Dice Statistics:\nDice Remaining: %i\n' %(remainingDice)
    yourDiceNumber, yourDiceValues=yourDice()
    otherRemain=remainingDice-yourDiceNumber
    
    print 'Number of Non-Ones : %f\nNumber of Ones: %f\n' %(otherRemain/3, otherRemain/6)

    betCalled=False
    while not betCalled:
            betNumber, betCount = getBetInfo()
            otherBetCount=reduceBet(betNumber,betCount,yourDiceValues)
            print 'The probability of this bet is: %f percent\n' %(100*getProbability(otherRemain,betNumber,otherBetCount))
            betCalled=input('Was the bet called?\nEnter 1 for Yes\nEnter 0 for No: ')
            print '\n'





def printSimpleStatistics(remainingDice):
    print 'Simple Statistics:\nDice Remaining: %i\n' %(remainingDice)
    print 'Number of Non-Ones : %f\nNumber of Ones: %f\n' %(remainingDice/3, remainingDice/6)

    betCalled = False
    while not betCalled:
        betNumber, betCount = getBetInfo()
        print 'The probability of this bet is: %f percent\n' %(100*getProbability(remainingDice,betNumber,betCount))
        betCalled=input('Was the bet called?\nEnter 1 for Yes\nEnter 0 for No: ')
        print '\n'



def playRound(numPlayers, remainingDice, considerMyDice):
        if considerMyDice:
                printIncludeYourDiceStats(remainingDice)
        else:
                printSimpleStatistics(remainingDice)



def startGame():
    print '\nWelcome to Pirates Dice! Good luck!\n'

    numPlayers, startingDice, remainingDice= getGameStats()
    considerMyDice=input('\nDo you want to consider your dice values in the calculations?\nEnter 1 for Yes\nEnter 0 for No: ')
    roundNum=1
    
    while remainingDice>1:
        print '\nThis is round: %i' %(roundNum)
        playRound(float(numPlayers), float(remainingDice),considerMyDice)
        roundNum+=1
        remainingDice -=1
    
    print 'Thank you for playing! Play again soon!'


startGame()