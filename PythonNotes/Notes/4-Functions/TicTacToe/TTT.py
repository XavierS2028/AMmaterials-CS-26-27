# TTT.py

# Imports

# Globals
gameBoard = [["x", "x", "x"], 
             ["x", "x", "x"], 
             ["x", "x", "x"]]
player1Token = "x"
player2Token = "o"

# Functions
def printBoardNew(board):
    for row in range(len(board)):
        print(f"\t", end="")

        for column in range(len(board[row])):
            print(f" {board[row][column]}", end="")

            if not(column == (len(board[0]) - 1)):
                print(" |", end="")
            else:
                print("")

        if not(row == (len(board) - 1)):
            print("\t", end="")
            print("-" * (3 * len(board[row]) + len(board[row]) - 1))
    
    print("")

printBoardNew(gameBoard)

def userMove(symbol, board):
    print(f"It is {symbol}'s turn")
    row = int(input(f"Row: ")) - 1
    col = int(input(f"Column: ")) - 1

    if row in range(len(board)) and col in range(len(board[row])):
        if board[row][col] == " ":
            board[row][col] = symbol
        else:
            print("You may not go here")
    else:
        print("Your move is out of bounds")

def isSquareEmpty(row, column):
    if gameBoard[row - 1][column - 1] == " ":
        return True
    else:
        return False


#   CheckForWinner
#       vertical
#       horizontal
#       diagnal
#   CheckForCat

# Main Loop
#   Draw Board
#   User Makes Turn
#   Check for winner or cat
