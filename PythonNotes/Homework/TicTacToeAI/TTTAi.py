# TTTAi.py

import random
import string

gameBoard = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]

playerToken = "x"
aiToken = "o"
isPlayerTurn = True

# Functions
def printBoard(board):
    for row in range(len(board)):
        print(f"\t", end="")

        for column in range(len(board[row])):
            print(f" {board[row][column]}", end="")

            if not(column == (len(board[row]) - 1)):
                print(" |", end="")
            else:
                print("")

        if not(row == (len(board) - 1)):
            print("\t", end="")
            print("-" * (3 * len(board[row]) + len(board[row]) - 1))
    
    print("")

def isValidMove(row: int, col: int, board) -> bool:
    if row in range(len(board)) and col in range(len(board[row])):
        if board[row][col] == " ":
            return True
        else:
            return False
    else:
        return False

def userMove(symbol, board):
    print(f"It is {symbol}'s turn")

    row = int(input(f"Row: ")) - 1
    col = int(input(f"Column: ")) - 1

    
    while not isValidMove(row, col, board):
        print("You may not go here, try again.")

        row = int(input(f"Row: ")) - 1
        col = int(input(f"Column: ")) - 1

    board[row][col] = symbol

def getRandomEmptySlot(board) -> list[int, int]:
    randomRow = random.randint(0, len(board) - 1)
    randomCol = random.randint(0, len(board) - 1)

    while not (board[randomRow][randomCol] == " "):
        randomRow = random.randint(0, len(board) - 1)
        randomCol = random.randint(0, len(board) - 1)

    return [randomRow, randomCol]


# Returns a row, column location of the first almost-won stretch of the board
# If no columns are almost-won, it will return the same best move that is passed in
def getStretchFinishPosition(tokenToMatch: string, outlierToken:string, board, bestMove: list[int, int]) -> list[int, int]:
    # Check For Almost-Won Rows
    for row in range(len(board)):
        if (not outlierToken in board[row]) and (board[row].count(tokenToMatch) == 2):
            return [row, board[row].index(" ")]

    # Check For Almost-Won Columns
    for column in range(len(board[0])):
        columnData = []

        for row in range(len(board)):
            columnData.append(board[row][column])

        if (not outlierToken in columnData) and (columnData.count(tokenToMatch) == 2):
            return [columnData.index(" "), column]

    # Check for Almost-Won Diagnals
    # Check top-left to bottom-right
    diagnal = []

    for i in range(len(board)):
        diagnal.append(board[i][i])

    if (not outlierToken in diagnal) and (diagnal.count(tokenToMatch) == 2):
        index = diagnal.index(" ")
        return [index, index]

    # Check for top-right to bottom-left
    index = 0
    diagnal = []

    for i in range(len(board)):
        diagnal.append(board[i][2 - i])

    if (not outlierToken in diagnal) and (diagnal.count(tokenToMatch) == 2):
        index = diagnal.index(" ")
        return [index, 2 - index]

    # If no almost-won stretches
    return bestMove

def aiMove(board):
    bestMove = getRandomEmptySlot(gameBoard)

    # Check Defensive Moves
    # If a stretch is almost won, it's blocking move becomes the best move
    bestMove = getStretchFinishPosition(playerToken, aiToken, gameBoard, bestMove)

    # Check For Offensive Moves
    # If a winning offensive move exists, it becomes the best move
    bestMove = getStretchFinishPosition(aiToken, playerToken, gameBoard, bestMove)

    board[bestMove[0]][bestMove[1]] = aiToken

def isBoardCAT(board) -> bool:
    for row in board:
        for col in row:
            if " " in col:
                return False
    return True

def hasWonBoard(board):
    # Horizontal
    for row in board:
        if ((row[0] == row[1]) and (row[1] == row[2])) and (not " " in row):
            return True
    
    # Vertical
    for col in range(3):
        if (board[0][col] == board[1][col]) and (board[1][col] == board[2][col]) and (not board[0][col] == " "):
            return True

    # Diagonal
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (not board[0][0] == " "):
       return True 

    if (board[2][0] == board[1][1]) and (board[1][1] == board[0][2]) and (not board[1][1] == " "):
        return True

print()

gameOver = False

while not gameOver:
    # Draw Board
    printBoard(gameBoard)

    if isPlayerTurn:
        userMove(playerToken, gameBoard)
    else:
        aiMove(gameBoard)

    # Check for winner or cat
    if hasWonBoard(gameBoard):
        if isPlayerTurn:
            print(f"Congrats Player!")
            print(f"You Won")
        else:
            print(f"Sorry, you lost")

        gameOver = True
        break

    if isBoardCAT(gameBoard):
        print("CAT Game")

        gameOver = True
        break

    isPlayerTurn = not isPlayerTurn

print("\n\n\n" + "==== " * 6 + "\n")
printBoard(gameBoard)

print("Good Game")