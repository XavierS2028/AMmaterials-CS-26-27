# TTT.py

# Imports

# Globals
gameBoard = [[" ", " ", " "], 
             [" ", " ", " "], 
             [" ", " ", " "]]
player1Token = "x"
player2Token = "o"

playerID = 1
playerTokens = (" ", player1Token, player2Token)

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

print()

gameOver = False

while not gameOver:
    # Draw Board
    printBoard(gameBoard)

    # User Makes Turn
    userMove(playerTokens[playerID], gameBoard)
    playerID *= -1

    # Check for winner or cat
    if hasWonBoard(gameBoard):
        print(f"Congrats {playerTokens[-playerID]}!")
        print(f"You Won")

        gameOver = True
        break

    if isBoardCAT(gameBoard):
        print("CAT Game")

        gameOver = True
        break

printBoard(gameBoard)

print("Good Game.")
