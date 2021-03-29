# This program only works if one deck of cards is used. Please do not use this in a professional setting.
cardValueList = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9,
                 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
playerHandList = []
dealerHandList = []

cardvalue = 0
dealercardvalue = 0

#def options():
    #deckamt = input("Input the number of decks you're playing with: ")
    #players = input("Input number of players: ")
    #shuffle = input("If used cards will NOT be put back into the deck, type 'y'. If the dealer shuffles each round, "
                    #"type 'n'.")

def changenumto(list,fromx,toy):
    decknumace = [num for num in list if num == fromx]
    while len(decknumace) > 0:
        list.remove(fromx)
        list.append(toy)
        decknumace.remove(fromx)


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

def ElevToOne(ace,handlist):
    while len(ace) > 0 and sum(handlist) > 21:
        handlist.remove(11)
        handlist.append(1)
        ace.remove(11)
        print(handlist)
        print(sum(handlist))

def calculate():
    pnumace = [num for num in playerHandList if num == 11]
    dnumace = [num for num in dealerHandList if num == 11]

    ElevToOne(pnumace,playerHandList) # If total > 21, changes ace to 1
    ElevToOne(dnumace,dealerHandList)
    if sum(playerHandList) > 21 and len(pnumace) == 0:
        print("Bust. You lose.")
        print(playerHandList)
        print(sum(playerHandList))
        exit()
    print("Your point total is: ", sum(playerHandList))
    print("The dealer's point total is: ", sum(dealerHandList))
    changenumto(cardValueList,11,1)
    print("Your chance of busting on your next card is: ", 100 * (
                float(len([num for num in cardValueList if num > (21 - sum(playerHandList))])) / float(
            len(cardValueList))), "%")
    if sum(playerHandList) <= 10:
        changenumto(cardValueList,1,11)
    print("The chance of succeeding on a double down is: ", 100 * (
                (float(len([num for num in cardValueList if num == (21 - sum(playerHandList))]))) / float(
            len(cardValueList))), "%")
    if len([num for num in playerHandList if num == 11]) > 0:
        print("Because you have an ace worth 11 points, you will not lose if your next card puts you over 21.")
    if sum(dealerHandList) < 20:
        changenumto(cardValueList,1,11)
    print("There is a ", 100 * (float(len([num for num in cardValueList if num == (21 - sum(dealerHandList))])) / float(
        len(cardValueList))), "% chance of the dealer's next card giving them 21.")
    changenumto(cardValueList,1,11)
    askLeave()

def dealerorplayer(num):
    if len(dealerHandList) == num:
        askDealervalue()
    else:
        askPlayervalue()

def testDealer():  # Prints a certain text depending on the number of the dealer's turn.
    global dealercardvalue

    if len(dealerHandList) == 0:
        dealercardvalue = input("What is the numerical value of the dealer's upcard? ")
    else:
        dealercardvalue = input("What is the numerical value of the card the dealer just pulled? Write "
                                "'stand' if the dealer is standing. ")


def testPlayer():  # Prints a certain text depending on the number of your turn.
    global cardvalue
    if len(playerHandList) == 0:
        cardvalue = input("What is the numerical value of the first card you were dealt? ")
    elif len(playerHandList) == 1:
        cardvalue = input("What is the numerical value of the second card you were dealt? (Say 'c' to calculate) ")
    else:
        cardvalue = input("What is the numerical value of the card you were just dealt? (Say 'c' to calculate or "
                          "'stand' to end your turn) ")


def askPlayervalue():
    testPlayer()
    if not str.isdigit(cardvalue):
        if cardvalue == 'exit':
            exit()
        elif cardvalue == 'c':
            if len(dealerHandList) > 0:
                calculate()
            else:
                print("Too soon to calculate. Input a card for the dealer first.")
                askPlayervalue()
        elif cardvalue == 'stand' and len(playerHandList) > 2:
            askDealervalue()
        elif cardvalue == 'stand' and len(playerHandList) <= 2:
            print("Please input your first 2 cards before standing.")
            askPlayervalue()
        else:
            print("Invalid response. Please input the numerical value of your card.")
            askPlayervalue()
    elif int(cardvalue) > 11 or int(cardvalue) < 2:
        print("Your card value cannot be higher than 10 or less than 1.")
        askPlayervalue()
    elif int(cardvalue) == 11:
        playerHandList.append(11)
        cardValueList.remove(11)
        dealerorplayer(0)

    else:
        playerHandList.append(int(cardvalue))
        cardValueList.remove(int(cardvalue))
        dealerorplayer(0)


def askDealervalue():  # Checks the value of the dealer's card.
    testDealer()
    if not str.isdigit(dealercardvalue):
        if dealercardvalue == 'exit':
            exit()
        elif dealercardvalue == 'c' and len(dealerHandList) != 0:
            calculate()
        elif dealercardvalue == 'c' and len(dealerHandList) == 0:
            print("Please input a card value for the dealer before calculating.")
            askDealervalue()
        elif dealercardvalue == 'stand' and len(dealerHandList) > 0:
            calculate()
        elif dealercardvalue == 'stand' and len(dealerHandList) == 0:
            print("Please input a value for the dealer before standing.")
            askDealervalue()
        else:
            print("Invalid response. Please input the numerical value of your card.")
            askDealervalue()
    elif int(dealercardvalue) > 11 or int(dealercardvalue) < 2:
        print("Your card value cannot be higher than 11 or less than 2.")
        askDealervalue()
    elif int(dealercardvalue) == 11:
        dealerHandList.append(11)
        cardValueList.remove(11)
        if len(dealerHandList) == 1:
            askPlayervalue()
        else:
            askDealervalue()
    else:
        dealerHandList.append(int(dealercardvalue))
        cardValueList.remove(int(dealercardvalue))
        if len(dealerHandList) == 1:
            askPlayervalue()
        else:
            askDealervalue()


print("Please keep in mind, you must input the value of an ace as '11'. Type 'exit' to leave at any time.")
askPlayervalue()
