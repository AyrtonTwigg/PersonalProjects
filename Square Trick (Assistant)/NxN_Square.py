# This program was created to assist me in performing a trick involving an nxn square (where n is a square number).
# Each coordinate can be empty or occupied, based on the spectator's choice.
# The spectator then selects a "secret" square which the program/assistant will have to find.
# I then change 1 square only (flip it from empty to occupied, or occupied to empty).
# Finally, I input the grid starting from top to bottom, and right to left. (0=empty, 1=occupied).
# The program will determine the chosen secret square based on specific rules planned by me.

import math

def ReadBoard(board, board_length):
    list_binary = []
    for twice in range(2):
        for x in range(int(math.log2(board_length))):
            check_even = 0
            for row in range(int(board_length/(2**(x+1)))):
                for col in range(board_length):
                    for jump in range(2**x):
                        if board[row+jump*int((board_length/2**x))][col]:
                            check_even += 1
            if check_even %2 == 0:
                list_binary.append(int("1"))
            else:
                list_binary.append(int("0"))
        if twice == 0:
            board = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
    return list_binary

def Decode(list_binary):
    x_coordinate = 1
    y_coordinate = 1
    
    pow_x = pow_y = int(math.log2(board_length))-1
    
    for i in range(len(list_binary)):
        if list_binary[i]:
            y_coordinate += 2**pow_y
        pow_y -= 1
    for i in range(int(len(list_binary)/2), len(list_binary)):
        if not list_binary[i]:
            x_coordinate += 2**pow_x
        pow_x -= 1
    
    print("Your chosen coordinate was: (%d,%d)" %(x_coordinate, y_coordinate))


user_board = [int(x) for x in list(input("Enter board configuration:"))]
board_length = int(math.sqrt(len(user_board)))
if board_length**2 != len(user_board):
    print("The length of the board is incorrect.")
    exit()

board = []
for i in range(board_length):
    board.append(user_board[i*board_length:(i+1)*board_length])

Decode(ReadBoard(board, board_length))
