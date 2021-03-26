import math
from collections import Counter

# This program only works if one deck of cards is used. Please do not use this in a professional setting.

bustChance = 0.0
doubleDown = " "
doubleDownFailChance = 0.0
cardValueList = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
playerHandList = []
dealerHandList = []

cardvalue = 0
dealerstand = False
dealercardvalue = 0

def calculate():
    print("Placeholder")
    #playertotal = 0
    #valuetil21 = 0
    pace = True in (num == 1 for num in playerHandList)
    dace = True in (num == 1 for num in dealerHandList)
    print(str(pace), str(dace))
    # Player Total Calculation
    playertotal = sum(playerHandList)
    print(playertotal)



def testDealer(): # Prints a certain text depending on the number of the dealer's turn.
    global dealercardvalue
    global dealerstand
    if len(dealerHandList) == 0:
        dealercardvalue = input("What is the numerical value of the dealer's upcard? ")
    else:
        if not dealerstand:
            dealercardvalue = input("What is the numerical value of the card the dealer just pulled? Write "
                                        "'n' if the dealer is standing. ")
            if dealercardvalue == "n":
                    dealerstand = True


def testPlayer(): #Prints a certain text depending on the number of your turn.
    global cardvalue
    global dealerstand
    global dealercardvalue
    if len(playerHandList) == 0:
        cardvalue = input("What is the numerical value of the first card you were dealt? ")
    elif len(playerHandList) == 1:
        cardvalue = input("What is the numerical value of the second card you were dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")
    else:
        cardvalue = input("What is the numerical value of the card you were just dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")
        print(dealerstand)

def askPlayervalue():
    testPlayer()
    if not str.isdigit(cardvalue):
        if cardvalue == 'exit':
            exit()
        elif cardvalue == 'c':
            calculate()
        else:
            print("Invalid response. Please input the numerical value of your card.")
            askPlayervalue()
    elif int(cardvalue) > 10:
        print("Your card value cannot be higher than 10.")
        askPlayervalue()
    else:
        playerHandList.append(int(cardvalue))
        cardValueList.remove(int(cardvalue))
        print(playerHandList)
        askDealervalue()

def askDealervalue(): # Checks the value of the dealer's card.
    global CallDealer
    global dealerstand
    testDealer()
    if not str.isdigit(dealercardvalue):
        if dealercardvalue == 'exit':
            exit()
        elif dealercardvalue == 'c':
            calculate()
        elif dealercardvalue == 'n' and len(dealerHandList) > 0:
            dealerstand = True
            askPlayervalue()
        else:
            print("Invalid response. Please input the numerical value of your card.")
            askDealervalue()
    elif int(dealercardvalue) > 10:
        print("Your card value cannot be higher than 10.")
        askDealervalue()
    else:
        dealerHandList.append(int(dealercardvalue))
        cardValueList.remove(int(dealercardvalue))
        print(dealerHandList)
        askPlayervalue()

#askPlayervalue()
calculate()
