# checking the state of the board
def win(lst):
    # column win
    for i in range(3):
        if lst[0][i] == lst[1][i] == lst[2][i] and lst[0][i] != "*":
            return (lst[0][i] + " win")
    # row win
        if lst[i][0] == lst[i][1] == lst[i][2] and lst[i][0] != "*":
            return (lst[i][0] + " win")
    # diagonal win
    if lst[0][0] == lst[1][1] == lst[2][2] and lst[0][0] != "*":
        return (lst[0][0] + " win")
    elif lst[0][2] == lst[1][1] == lst[2][0] and lst[0][2] != "*":
        return (lst[2][0] + " win")
    return "continue"
hold = " "
board = []
# variable for dividing the turn between two player
count = "X"
tem = []
#variable to check for draw:
counter = 0

print("Welcome to Tic Tac Toe")
print("To play, just enter the coordinator of the space you want to play on. For example: 1 1 will return the piece in the central")
print("Type start to start the game.")
# check if input = start
if input().lower() == "start":
# creating and printing the new board
    for i in range(3):
        board.append(["*", "*", "*"])
    for j in range(3):
        print(board[j])
    print("X goes first")
# continue to play the game until one of two player win
while hold != "X win" and hold != "O win" :
    # X turn, enter the coordinator to move
    while count == "X":
        print("Enter the coordinator you want for X, from 0 to 2, on a line")
        tem = input().split(" ")
        if board[int(tem[0])][int(tem[1])] == "*":
            board[int(tem[0])][int(tem[1])] = "X"
            count = "O"
            counter += 1
        else:
            print("this place have already been taken, please enter another coordinator for X")
    # board state after X move
    for i in range(3):
        print(board[i])
    hold = win(board)
    print(hold)
    # check for draw
    if counter == 9:
        print("draw")
        break

    # O turn. enter the coordinator to move
    while count == "O":
        print("Enter the coordinator you want for O, from 0 to 2, on a line")
        tem = input().split(" ")
        if board[int(tem[0])][int(tem[1])] == "*":
            board[int(tem[0])][int(tem[1])] = "O"
            count = "X"
            counter += 1
        else:
            print("this place have already been taken, please enter another coordinator for O")
    # board state after O move
    for i in range(3):
        print(board[i])
    hold = win(board)
    print(hold)
    # check for draw
    if counter == 9:
        print("draw")
        break
