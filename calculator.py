import math


# This program only works if one deck of cards is used. Please do not use this in a professional setting.

bustchance = None
doubledown = None
doubledownfailchance = None
playercardace = None
dealercardace = None
dealerhandvalue = 0
playerhandvalue = 0
playercard1 = None
playercard2 = None

def playercardvalue(): # This function tests for the value of the player's cards.
    print("What is the value of your second card? If the card is an Ace, please write 'a' without the symbols.\n")
    playercard2 = input()
    if playercardace == True:
        if playercard2 == 'a':
            playercard2 = 1
            playerhandvalue = 12
        elif playercard2 == 10:
            bustchance = 100
            doubledownfailchance = 100
            doubledown = "Guaranteed to fail."
    elif str.isdigit(playercard2):
        playercard2 = int(playercard2)
        playerhandvalue = playercard2 + playercard1

        else:
            print("Invalid response. Please input the numerical value of your card.")
            playercardvalue()
    elif None:
        print("ee")
    else:
        print("Test")
        print(playercardace)



def playerace(): # This function tests to see if the player has an Ace.
    global playercard1
    global playercardace
    print("Are one of your two cards an Ace? [y/n]\n")
    playercardace = input()
    if playercardace == 'y':
        print("Ace") # To be removed
        playercardace = True
        playercard1 = 11
        playercardvalue()
    elif playercardace == 'n':
        print("No ace") # To be removed
        playercardace = False
        playercardvalue()
    else:
        print('Invalid response. Please input y or n.')
        playerace()

def dealerace(): # Tests to see if the dealer has an Ace.
    global dealercardace
    global dealerhandvalue

    print("Is the dealer's first card an Ace? [y/n]\n")
    dealercardace = input()
    if dealercardace == 'y':
        print("Dealer has an ace.") #To be removed.
        dealercardace = True
        dealerhandvalue = 11
    elif dealercardace == 'n':
        print("Dealer does not have an ace.") #To be removed.
        dealercardace = False
    else:
        print("Invalid response. Please input y or n.")
        dealerace()


def printchance():
    print("Your chance of going over 21 with your next card is: ",str(bustchance),"%\n""Doubling down is:", doubledown," (",str(doubledownfailchance),"% chance of failure)\n")

playerace()
dealerace()
# To Do:
# Calculate chance of bust considering remaining cards in deck.
# Calculate how likely you are to succeed on a double down.
# Remove clunky variables
