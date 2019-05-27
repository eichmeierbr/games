## Pirates Dice

### Introduction and Rules
This is a simple betting game I first saw in Pirate's of the Carribean 2: Dead Man's Chest.  The game begins with each player secretly rolling 5 dice. A round consists of players sequentially predicting and betting on the number of dice of a particular value on the table. When a player believes the previous bet is incorrect, they 'call' the bet and everybody reveals their dice. Whichever of the two players incorrectly predicted the bet loses a dice. Rounds are repeated until only a single play has remaining dice. A more thorough ruleset can be found here: [Game Rules](https://en.wikipedia.org/wiki/Liar%27s_dice)

### Implementation
My program currently aids the user by calculating the probability of each bet being succesful. It begins by asking the number of players in the game and the number of beginning dice given to each player. Then, the user may select whether or not to include their own dice in the probability calculations. Including the known dice values increases accuracy, but can be tedious during play. Then the program conducts a round by inputting known dice values and calculating bet success probability.

  1) Initialize Game:
      1) Request number of players and number of starting dice
      2) Determine calculation method
  2) Conduct Round:
      1) If smart calculation is enabled, request the user's dice values
      2) Request bet count and value
      3) Calculate and display the probability of bet success using the binomial function
      4) If the user bets agrees with the bet, return to step 2.ii
      5) Otherwise, reduce the number of dice by one and return to step 2.i

### Future Work

  1) Error Handling
      1) Currently, there is no error handling on user input. Any improper input causes the program to crash. Implementing basic error handling will improve stability.
  2) AI Player
      1) This program is close to having a computer player. AI opponents will increase bets when the liklihood of the previous bet is above 50%. Then, the AI must have logic to select the next bet. 
  3) Implement Self-Playing Game
      1) The final improvement is establishing a framework for the user to play an entire game against computer opponents. In addition to the previous steps, a computerized game would create multiple opponents, and better facilitate playing rounds.
