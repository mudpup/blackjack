import math

# This program only works if one deck of cards is used. Please do not use this in a professional setting.

bustChance = 0.0
doubleDown = " "
doubleDownFailChance = 0.0
playerHasAce = False
dealerHasAce = False
dealerHandValue = 0
playerHandValue = 0
cardValueList = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
playerHandList = []
dealerHandList = []

cardvalue = " "
dealerstand = False
dealercardvalue = ""

def calculate():
    print("Placeholder")


def askvalprint():
    global cardvalue
    global dealerstand
    global dealercardvalue
    if len(playerHandList) == 0:
        cardvalue = input("What is the numerical value of the first card you were dealt? ")
    elif len(playerHandList) == 1:
        cardvalue = input("What is the numerical value of the second card you were dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")
        dealercardvalue = input("What is the numerical value of the dealer's upcard? ")
    else:
        cardvalue = input("What is the numerical value of the card you were just dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")
        print(dealerstand)
        if not dealerstand:
            dealercardvalue = input("What is the numerical value of the card the dealer just pulled? Write 'N/A' if the dealer is standing. ")
            if dealercardvalue == "N/A":
                dealerstand = True

def askvalue():
    global cardvalue
    askvalprint()
    if not str.isdigit(cardvalue) or not int(cardvalue) <= 10:
        if cardvalue == 'exit' or cardvalue == 'c':
            if cardvalue == 'exit':
                exit()
            else:
                calculate()
        elif not str.isdigit(cardvalue):
            print("Invalid response. Please input the numerical value of your card.")
            askvalue()
        else:
            print("Your card value cannot be higher than 10.")
            askvalue()
    elif not int(dealercardvalue)<= 10 or not dealercardvalue == "N/A":
        print("Invalid response. Please input the numerical value of the dealer's card.")
        askvalue()
    else:
        playerHandList.append(int(cardvalue))
        cardValueList.remove(int(cardvalue))
        print(playerHandList)
        if not dealerstand:
            dealerHandList.append(int(dealercardvalue))
            cardValueList.remove(int(dealercardvalue))
        print(dealerHandList)
        askvalue()


askvalue()
