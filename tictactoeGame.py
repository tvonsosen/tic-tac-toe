# Tic Tac Toe Bot
# Created with help of tutorial from youtube channel 'Tech With Tim'
squares = [' ' for x in range(9)]

def insertLetter(letter, pos):
    squares[pos] = letter

def spaceIsFree(pos):
    return squares[pos] == ' '


def printBoard(squares):
    
    """ Prints tic-tac-toe squares """
    
    print(" ") # Space on top

    print(squares[0], "  #  ", squares[1], "  #  ", squares[2])
    print("-------------------")
    print(squares[3], "  #  ", squares[4], "  #  ", squares[5])
    print("-------------------")
    print(squares[6], "  #  ", squares[7], "  #  ", squares[8])

    print(" ") # Space on bottom



def isWinner(bo, le):
    return (bo[6] == le and bo[7] == le and bo[8] == le or bo[3] == le and bo[5] == le and bo[4] == le or bo[0] == le and bo[2] == le and bo[1] == le or bo[0] == le and bo[3] == le and bo[6] == le or bo[1] == le and bo[4] == le and bo[7] == le or bo[2] == le and bo[5] == le and bo[8] == le or bo[4] == le and bo[8] == le and bo[0] == le or bo[2] == le and bo[4] == le and bo[6] == le)

def playerMove():
    run = True
    while run:
        move = input("Pick a space that isn't taken 1-9 (1 is at the top left, and 9 is at the bottom right) to place an X:   ")
        try:
            move = int(move) - 1
            if move >=0 and move <9:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('That space is taken!')
            else:
                print('Please type a number within the given range!')
        except:
            print('Please type a number!')
def compMove():
    possibleMoves = [x for x, letter in enumerate(squares) if letter == ' ']
    move = 10

    for let in ['0','X']:
        for i in possibleMoves:
            boardCopy = squares[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    if 4 in possibleMoves:
        move = 4 
        return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
def selectRandom(list1):
    import random

    ln = len(list1)
    ranNumber = random.randrange(0,ln)
    return list1[ranNumber]

def isBoardFull(squares):
    if squares.count(' ')>0:
        return False
    
    else:
        return True

def main():
    print('TIC TAC TOE')
    printBoard(squares)

    while not(isBoardFull(squares)):
        if not(isWinner(squares, 'O')):
            playerMove()

            printBoard(squares)
            if isBoardFull(squares):
                if isWinner(squares, 'X'):
                    print('X wins!')
                    break
                else:
                
                    break
        else:
            print('O wins!')
            break
        if not(isWinner(squares, 'X')):
            move = compMove()
            if move == 10:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an O in position ', move, ':')
                printBoard(squares)
        else:
            print('X wins!')
            break

    if isBoardFull(squares):
        print('TIE')

main()

# ! 2 player tic tac toe game

# squares = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # Each position where and X or O can be played
# def printBoard(squares):
#     """ Prints tic-tac-toe board """
    
#     print(" ") # Space on top

#     print(squares[0], "  #  ", squares[1], "  #  ", squares[2])
#     print("-------------------")
#     print(squares[3], "  #  ", squares[4], "  #  ", squares[5])
#     print("-------------------")
#     print(squares[6], "  #  ", squares[7], "  #  ", squares[8])

#     print(" ") # Space on bottom



# def moves(squares, move):
#     """ Function for each move and to check if the move is valid """

#     # Printing the board at first move
#     if move == 1: 
#         printBoard(squares)

#     errorCheck = True
#     while errorCheck:
#         firstPlayerMove = input("Pick a space that isn't taken 1-9 (1 is at the top left, and 9 is at the bottom right):   ")
        
#         # Checks if the input is a positive integer inside of the string
#         if firstPlayerMove.isdigit() == False:
#             errorCheck = True
#             print("That's not a valid integer!")
#             continue # skips to top of loop
        
#         # Checks if the input is between 1 and 9 
#         elif int(firstPlayerMove) < 1 or int(firstPlayerMove) > 9:
#             print("That's not a number 1-9!")
#             errorCheck = True
#             continue # skips to top of loop
            

#         # Checks if the square is vacant or not
#         elif squares[int(firstPlayerMove)-1] != " ":
#             errorCheck = True
#             print("That square is taken!")
#             continue # skips to top of loop
            
        
#         # If the move is valid it enters this else statement
#         else: 
#             errorCheck = False # exits while loop
#             move += 1 # adding 1 to count for this move being valid


#     # Even moves are Xs' and odd moves are 0s' 
#     if move%2 == 0:
#         squares[int(firstPlayerMove)-1] = "X"
#     else:
#         squares[int(firstPlayerMove)-1] = "O"

#     printBoard(squares) # Prints the new updated board

#     # Checks if there is a win or tie
#     if checkGame(squares) == False:
#         exit()
#     else:
#         moves(squares,move)

    
    

# def checkGame(squares):
#     """ Checking for wins and ties """

#     keepPlaying = True # If keepPlaying is True, the game is not over yet

#     # Checking for horizontal wins
#     for i in range(0,7,3):
#         if squares[i] != " ":
#             if squares[i] == squares[i+1] and squares[i] == squares[i+2]:
#                 print(squares[i], "WINS!!!")
#                 print("") # new line in between
#                 keepPlaying = False
#                 return keepPlaying

#     # Checking for vertical wins
#     for i in range(3):
#         if squares[i] != " ":
#             if squares[i] == squares[i+3] and squares[i] == squares[i+6]:
#                 print(squares[i], "WINS!!!")
#                 print("") # new line in between
#                 keepPlaying = False
#                 return keepPlaying

#     # Checking for any diagonal wins 
#     if squares[0] != " ":
#         if squares[0] == squares[4] and squares[0] == squares[8]:
#             print(squares[0], "WINS!!!")
#             print("") # new line in between
#             keepPlaying = False
#             return keepPlaying
#     if squares[2] != " ":
#         if squares[2] == squares[4] and squares[2] == squares[6]:
#             print(squares[2], "WINS!!!")
#             print("") # new line in between
#             keepPlaying = False
#             return keepPlaying

#     # Checking for ties
#     filledUp = 0
#     for i in squares:
#         if i != " ":
#             filledUp += 1
#     if filledUp == 9:
#         print("TIE")
#         print("") # new line in between
#         keepPlaying = False
#         return keepPlaying
    
#     return keepPlaying


# move = 1 # number of valid moves

# moves(squares,move)