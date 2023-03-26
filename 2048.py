# This project is my trial to replicate the 2048 game in Python
import random
# print the current board
def boardprint(lst):
    for i in range(4):
        for j in range(4):
            print(lst[i][j], end="\t")
        print()
# rotate the board for moving and merging process
def rotate(lst):
    tem = [[0,0,0,0] for i in range(4)]
    for i in range(4):
        for j in range(4):
                tem[3-j][i] = lst[i][j]

    return tem
# moving the board to the left direction, then combine the same number to 2x that number
def merge(lst):
    for i in range(0, 4):
        for j in range(3, 0, -1):
            # moving to the left
            if board[i][j] != 0 and board[i][j - 1] == 0:
                board[i][j - 1] = board[i][j]
                board[i][j] = 0
            # merging two same number
            if board[i][j] == board[i][j - 1]:
                board[i][j - 1] *= 2
                board[i][j] = 0
            # check after merging if there is any empty space, if yes, then move. These are 3 steps to simulate real moving 2048 game
            if board[i][j] != 0 and board[i][j - 1] == 0:
                board[i][j - 1] = board[i][j]
                board[i][j] = 0
    return board
# check if player has won or lost
def end(board):
    count = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                return "win"
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i + 1][j] or board[i][j] == 0:
                count += 1
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[i][j] == 0:
                count += 1
    if count == 0:
        return "lose"

# spawn a random 2 or 4 on a random empty position
def spawn(lst):
    ranpos = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                ranpos.append((i * 4 + j))
    try:
        t = random.choice(ranpos)
        lst[t // 4][t % 4] = random.choice([2, 2, 2, 2, 4])
    except IndexError:
        return None
# checking if player type start or not, if yes, creating a new board
print("Type start to play 2048")
if input().lower() == "start":
    board = []
    hold = []
    for i in range(4):
        board.append([0, 0, 0, 0])
    for i in range(2):
        hold.append((random.randint(0, 15), random.choice([2, 2, 2, 2, 4])))
    # position repeat handle, if yes, random until there is no more repeat
    while hold[0][0] == hold[1][0]:
        hold.pop(1)
        hold.append((random.randint(0, 15), random.choice([2, 2, 2, 2, 4])))
    board[hold[0][0] // 4][hold[0][0] % 4] = hold[0][1]
    board[hold[1][0] // 4][hold[1][0] % 4] = hold[1][1]
    boardprint(board)
# checking if win or lose has happen, if yes, stop the code
while end(board) != "win" and end(board) != "lose":
    # direction input
    print("Enter the direction you want to move: (A = left), (W = up), (D = right), (S = down)")
    direction = input()
    # Because the default moving and merging is the left, therefore, we must rotate the board to the left for merge function and then rotate it back to the normal board
    if direction.lower() == "a":
        merge(board)
        spawn(board)
        boardprint(board)
    elif direction.lower() == "w":
        board = rotate(board)
        merge(board)
        for i in range(3):
            board = rotate(board)
        spawn(board)
        boardprint(board)
    elif direction.lower() == "d":
        for i in range(2):
            board = rotate(board)
        merge(board)
        for i in range(2):
           board = rotate(board)
        spawn(board)
        boardprint(board)
    elif direction.lower() == "s":
        for i in range(3):
            board = rotate(board)
        merge(board)
        for i in range(1):
            board = rotate(board)
        spawn(board)
        boardprint(board)
# print text depending on player won or lost
if end(board) == "win":
    print("Congratulations, you have won the game")
elif end(board) == "lose":
    print("Better luck next time")