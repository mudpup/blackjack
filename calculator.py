# This program only works if one deck of cards is used. Please do not use this in a professional setting.
cardValueList = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
playerHandList = []
dealerHandList = []

cardvalue = 0
dealerstand = False
dealercardvalue = 0

def askLeave():
    leave = input(("Type 'exit' to exit, or 'c' to keep playing. "))
    if leave == 'exit' or 'c':
        if leave == 'exit':
            exit()
        else:
            askPlayervalue()
    if not leave == 'exit' or 'c':
        print("Invalid answer. Please write 'exit' or 'c'. ")
        askLeave()

def calculate():
    pnumace = [num for num in playerHandList if num == 11]
    dnumace = [num for num in dealerHandList if num == 11]

    # Player Total Calculation
    while len(pnumace) > 0 and sum(playerHandList) > 21: #Changes aces to 1 if bust
        playerHandList.remove(11)
        playerHandList.append(1)
        pnumace.remove(11)
        print(playerHandList)
        print(sum(playerHandList))
    if sum(playerHandList) > 21 and len(pnumace) == 0:
        print("Bust. You lose.")
        print(playerHandList)
        print(sum(playerHandList))
        exit()
    print("Your point total is: ",sum(playerHandList))
    print("Your chance of busting on your next card is: ", 100*(float(len([num for num in cardValueList if num > (21-sum(playerHandList))]))/float(len(cardValueList))), "%")
    print("The chance of succeeding on a double down is: ", 100*((float(len([num for num in cardValueList if num == (21-sum(playerHandList))])))/float(len(cardValueList))),"%")
    if len([num for num in playerHandList if num == 11]) > 0:
        print("Because you have an ace worth 11 points, you will not lose if your next card puts you over 21.")
    print("There is a ", 100*(float(len([num for num in cardValueList if num == (21-sum(dealerHandList))]))/float(len(cardValueList))),"% chance of the dealer's next card giving them 21.")
    askLeave()



def testDealer():  # Prints a certain text depending on the number of the dealer's turn.
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


def testPlayer():  # Prints a certain text depending on the number of your turn.
    global cardvalue
    if len(playerHandList) == 0:
        cardvalue = input("What is the numerical value of the first card you were dealt? ")
    elif len(playerHandList) == 1:
        cardvalue = input("What is the numerical value of the second card you were dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")
    else:
        cardvalue = input("What is the numerical value of the card you were just dealt? (Say 'exit' to exit, "
                          "and 'c' to calculate) ")


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
    elif int(cardvalue) > 10 or int(cardvalue) < 1:
        print("Your card value cannot be higher than 10 or less than 1.")
        askPlayervalue()
    elif int(cardvalue) == 1:
        playerHandList.append(11)
        cardValueList.remove(int(cardvalue))
        askDealervalue()
    else:
        playerHandList.append(int(cardvalue))
        cardValueList.remove(int(cardvalue))
        askDealervalue()


def askDealervalue():  # Checks the value of the dealer's card.
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
    elif int(dealercardvalue) > 10 or int(dealercardvalue) < 1:
        print("Your card value cannot be higher than 10 or less than 1.")
        askDealervalue()
    elif int(dealercardvalue) == 1:
        dealerHandList.append(11)
        cardValueList.remove(int(dealercardvalue))
    else:
        dealerHandList.append(int(dealercardvalue))
        cardValueList.remove(int(dealercardvalue))
        askPlayervalue()


askPlayervalue()
