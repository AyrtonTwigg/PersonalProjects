# This program will assist in performing the exact trick explained here: https://www.youtube.com/watch?v=4UDlmyMyq7Q
# Input the cards in this way: 5H 10D AS QC

def FindNumber(cards):
    number = ReadValue(cards[0][:-1])
    first = ReadValue(cards[1][:-1]) * 4
    second = ReadValue(cards[2][:-1]) * 4
    third = ReadValue(cards[3][:-1]) * 4
    to_add = 1
    
    if first == second == third:
        first += SuitNum(cards[1][-1])
        second += SuitNum(cards[2][-1])
        third += SuitNum(cards[3][-1])
    elif first == second:
        first += SuitNum(cards[1][-1])
        second += SuitNum(cards[2][-1])
    elif second == third:
        second += SuitNum(cards[2][-1])
        third += SuitNum(cards[3][-1])
    elif first == third:
        first += SuitNum(cards[1][-1])
        third += SuitNum(cards[3][-1])
    
    if first < second:
        if second > third:
            if first < third:
                to_add = 2
            else:
                to_add = 4
    else:
        if second < third:
            if first < third:
                to_add = 3
            else:
                to_add = 5
        else:
            to_add = 6

    number += to_add
    if number > 13:
        number -= 13
    value = ReadNumber(number)
    
    return value

def ReadValue(value):
    if value == 'A':
        return 1
    elif value == 'J':
        return 11
    elif value == 'Q':
        return 12
    elif value == 'K':
        return 13
    else:
        return int(value)

def SuitNum(suit):
    if suit == 'C':
        return 3
    elif suit == 'H':
        return 2
    elif suit == 'S':
        return 1
    elif suit == 'D':
        return 0
    else:
        print('Values could not be read.')
        exit()

def ReadNumber(number):
    if 2 <= number <= 10:
        return str(number)
    elif number == 1:
        return 'A'
    elif number == 11:
        return 'J'
    elif number == 12:
        return 'Q'
    elif number == 13:
        return 'K'
    else:
        print('Values could not be read.')
        exit()

def ExtendSuit(suit):
    if suit == 'C':
        return 'Clubs'
    elif suit == 'H':
        return 'Hearts'
    elif suit == 'S':
        return 'Spades'
    elif suit == 'D':
        return 'Diamonds'
    else:
        print('Values could not be read.')
        exit()


cards = input("What are the cards?\n").split()
suit = ExtendSuit(cards[0][-1])
number = FindNumber(cards)
print('The card is:\n%s of %s' %(number, suit))
