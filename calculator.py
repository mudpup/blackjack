import math


# This program only works if one deck of cards is used. Please do not use this in a professional setting.

bustChance = 0.0
doubleDown = " "
doubleDownFailChance = 0.0
playerHasAce = False
dealerHasAce = False
dealerHandValue = 0
playerHandValue = 0
cardValueList = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
playerHandList = []
dealerHandList = []
idealmove = " "

def playerCardvalue(): # This function tests for the value of the player's cards.
    #global playerHandValue
    #global bustChance
    #global doubleDownFailChance
    #global doubleDown

    print("What is the value of your second card? If the card is an Ace, please write 'a' without the symbols.\n")
    cardvalue = input()

    if playerHasAce:
        if cardvalue == 'a': #Testfor ace
            playerHandValue = 12
            playerHandList.append(1)
            cardValueList.remove(1)

        elif cardvalue == '10': #Testfor face
            playerHandValue = 21
            playerHandList.append(10)
            cardValueList.remove(10)
            printChance()
        else:
            cardvalue = int(cardvalue)
            cardValueList.remove(cardvalue)
            playerHandList.append(cardvalue)
            playerHandValue = playerHandValue + cardvalue

        elif str.isdigit(cardvalue) and int(cardvalue) <= 10:
          cardvalue = int(cardvalue)
          playerHandValue = cardvalue + playerCard1
          playerHandList.append(playerCard2)
          cardValueList.remove(playerCard2)

        else:
            print("Invalid response. Please input the numerical value of your card.")
            playerCardvalue()


def playerAce(): # This function tests to see if the player has an Ace.
    #global playerHasAce
    #global cardValueList
    #global playerHandValue

    print("Are one (or both) of your two cards an Ace? [y/n]\n")
    playerHasAce = input()

    if playerHasAce == 'y':
        playerHasAce = True
        cardValueList.remove(1)
        playerHandList.append(1)
        playerHandValue = 11
        playerCardvalue()

    elif playerHasAce == 'n':
        playerHasAce = False
        playerCardvalue()

    else:
        print('Invalid response. Please input y or n.')
        playerAce()


def dealerAce(): # Tests to see if the dealer has an Ace.
    #global dealerHasAce
    #global dealerHandValue

    print("Is the dealer's upcard an Ace? [y/n]\n")
    dealerHasAce = input()

    if dealerHasAce == 'y':
        dealerHasAce = True
        dealerHandValue = 11
        cardValueList.remove(1)
        dealerHandList.append(1)

    elif dealerHasAce == 'n':
        dealerHasAce = False
        print("What is the value of the dealer's card?")


    else:
        print("Invalid response. Please input y or n.")
        dealerAce()

def bust():
 print("pee")

def printChance():
    if playerHandValue < 21:
        print("Your chance of going over 21 with your next card is: ",str(bustChance))
        print("Doubling down is:", doubleDown," (",str(doubleDownFailChance),"% chance of failure)\n")
        print("The ideal move in this situation is to ",idealmove)
    elif playerHandValue == 21:
        print("You win! Your hand is a 21.")
    else:
        print("Bust. Better luck next time.")


#playerAce()
#dealerAce()
print("Dealer: ",dealerHandList)
print("Player: ",playerHandList)
print("Deck: ",cardValueList)
def game():
    playerAce()
    dealerAce()
game()
