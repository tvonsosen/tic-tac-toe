# 2 player tic tac toe game

squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # Each position where and X or O can be played
def printBoard(squares):
    """ Prints tic-tac-toe board """
    
    print(" ") # Space on top

    print(squares[0], "  #  ", squares[1], "  #  ", squares[2])
    print("-------------------")
    print(squares[3], "  #  ", squares[4], "  #  ", squares[5])
    print("-------------------")
    print(squares[6], "  #  ", squares[7], "  #  ", squares[8])

    print(" ") # Space on bottom



def moves(squares, move):
    """ Function for each move and to check if the move is valid """

    # Printing the board at first move
    if move == 1: 
        printBoard(squares)

    errorCheck = True
    while errorCheck:
        firstPlayerMove = input("Pick a space that isn't taken 1-9 (1 is at the top left, and 9 is at the bottom right):   ")
        
        # Checks if the input is a positive integer inside of the string
        if firstPlayerMove.isdigit() == False:
            errorCheck = True
            print("That's not a valid integer!")
            continue # skips to top of loop
        
        # Checks if the input is between 1 and 9 
        elif int(firstPlayerMove) < 1 or int(firstPlayerMove) > 9:
            print("That's not a number 1-9!")
            errorCheck = True
            continue # skips to top of loop
            

        # Checks if the square is vacant or not
        elif squares[int(firstPlayerMove)-1] != " ":
            errorCheck = True
            print("That square is taken!")
            continue # skips to top of loop
            
        
        # If the move is valid it enters this else statement
        else: 
            errorCheck = False # exits while loop
            move += 1 # adding 1 to count for this move being valid


    # Even moves are Xs' and odd moves are 0s' 
    if move%2 == 0:
        squares[int(firstPlayerMove)-1] = "X"
    else:
        squares[int(firstPlayerMove)-1] = "O"

    printBoard(squares) # Prints the new updated board

    # Checks if there is a win or tie
    if checkGame(squares) == False:
        exit()
    else:
        moves(squares,move)

    
    

def checkGame(squares):
    """ Checking for wins and ties """

    keepPlaying = True # If keepPlaying is True, the game is not over yet

    # Checking for horizontal wins
    for i in range(0,7,3):
        if squares[i] != " ":
            if squares[i] == squares[i+1] and squares[i] == squares[i+2]:
                print(squares[i], "WINS!!!")
                print("") # new line in between
                keepPlaying = False
                return keepPlaying

    # Checking for vertical wins
    for i in range(3):
        if squares[i] != " ":
            if squares[i] == squares[i+3] and squares[i] == squares[i+6]:
                print(squares[i], "WINS!!!")
                print("") # new line in between
                keepPlaying = False
                return keepPlaying

    # Checking for any diagonal wins 
    if squares[0] != " ":
        if squares[0] == squares[4] and squares[0] == squares[8]:
            print(squares[0], "WINS!!!")
            print("") # new line in between
            keepPlaying = False
            return keepPlaying
    if squares[2] != " ":
        if squares[2] == squares[4] and squares[2] == squares[6]:
            print(squares[2], "WINS!!!")
            print("") # new line in between
            keepPlaying = False
            return keepPlaying

    # Checking for ties
    filledUp = 0
    for i in squares:
        if i != " ":
            filledUp += 1
    if filledUp == 9:
        print("TIE")
        print("") # new line in between
        keepPlaying = False
        return keepPlaying
    
    return keepPlaying


move = 1 # number of valid moves

moves(squares,move)