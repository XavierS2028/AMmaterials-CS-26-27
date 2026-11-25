# TTTAi.py

import random
import string

gameBoard = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]

# Helper Location Lists
#               Top L,  Top R,  Bot L,  Bot R
boardCorners = [[0, 0], [0, 2], [2, 0], [2, 2]]
#               Top,    Left,   Right,   Bottom
boardEdges   = [[0, 1], [1, 0], [1, 2], [2, 1]]

playerToken = "x"
aiToken = "o"
isPlayerTurn = True

playerTurns = [0] # Needs to be a list because Python doesn't like ints for reasons

# General Helper Functions
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

# User Helper Functions
def userMove(symbol, board):
    print(f"It is {symbol}'s turn")

    row = int(input(f"Row: ")) - 1
    col = int(input(f"Column: ")) - 1

    
    while not isValidMove(row, col, board):
        print("You may not go here, try again.")

        row = int(input(f"Row: ")) - 1
        col = int(input(f"Column: ")) - 1

    board[row][col] = symbol
    playerTurns[0] += 1


# Algorithm Helper Functions
def getRandomEmptySlot(board) -> list[int, int]:
    randomRow = random.randint(0, len(board) - 1)
    randomCol = random.randint(0, len(board) - 1)

    while not (board[randomRow][randomCol] == " "):
        randomRow = random.randint(0, len(board) - 1)
        randomCol = random.randint(0, len(board) - 1)

    return [randomRow, randomCol]

def counterOpeningMove(userToken: string, board) -> list[int, int]:
    playerOpening = [0, 0]

    for row in range(len(board)):
        if userToken in board[row]:
            playerOpening = [row, board[row].index(userToken)]

    # If player opens in the center position
    if playerOpening == [1, 1]:
        bestMove = boardCorners[random.randint(0, 3)]
    else:
        bestMove = [1, 1]

    return bestMove

def counterSecondMove(userToken: string, board, bestMove: list[int, int]) -> list[int, int]:
    playerLocations = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == userToken:
                playerLocations.append([row, col])

    # If both of the player's moves are in the corners
    if (playerLocations[0] in boardCorners) and (playerLocations[1] in boardCorners):
        # If Opposite Corners (neither row nor column of the two match)
        # If Adjacent Corners, just fall through and use the preexisting defense logic
        if (not(playerLocations[0][1] == playerLocations[1][1])) and (not(playerLocations[0][0] == playerLocations[1][0])):
            bestMove = boardEdges[random.randint(0, 3)]

    # If both of the player's moves are in the edges
    if (playerLocations[0] in boardEdges) and (playerLocations[0] in boardEdges):
        # If the locations share either a row or a column, they must be opposite of each other
        if (playerLocations[0][0] == playerLocations[1][0]) or (playerLocations[0][1] == playerLocations[1][1]):
            openEdgeList = boardEdges
            openEdgeList.remove(playerLocations[0]) 
            openEdgeList.remove(playerLocations[1])

            bestMove = openEdgeList[random.randint(0, 1)]

        # If the locations are not opposite, the algorithm must go in the corner between the two
        else:
            # If the top is taken by the player
            if (playerLocations[0] == boardEdges[0]) or (playerLocations[1] == boardEdges[0]):
                # If left is taken
                if (playerLocations[0] == boardEdges[1]) or (playerLocations[1] == boardEdges[1]):
                    bestMove = boardCorners[0] # Top Left Corner
                # If right is taken
                else:
                    bestMove = boardCorners[1] # Top Right Corner
            # If the bottom is taken by the player
            else:
                # If left is taken
                if (playerLocations[0] == boardEdges[1]) or (playerLocations[1] == boardEdges[1]):
                    bestMove = boardCorners[2] # Bottom Left Corner
                # If right is taken
                else:
                    bestMove = boardCorners[3] # Bottom Right Corner
            

    return bestMove

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
    # First, find a random empty slot. Worst case scenario move
    bestMove = getRandomEmptySlot(gameBoard)

    # Counter opening move before moving to regular algorithm
    if playerTurns[0] == 1:
        bestMove = counterOpeningMove(playerToken, gameBoard)

    elif playerTurns[0] == 2:
        bestMove = counterSecondMove(playerToken, gameBoard, bestMove)
        bestMove = getStretchFinishPosition(playerToken, aiToken, gameBoard, bestMove)

    # After countering the opening move, perform regular algorithm
    else:
        # Check Defensive Moves
        # If a stretch is almost won, it's blocking move becomes the best move
        bestMove = getStretchFinishPosition(playerToken, aiToken, gameBoard, bestMove)

        # Check For Offensive Moves
        # If a winning offensive move exists, it becomes the best move
        bestMove = getStretchFinishPosition(aiToken, playerToken, gameBoard, bestMove)

    board[bestMove[0]][bestMove[1]] = aiToken

# Game Board Helper Functions
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