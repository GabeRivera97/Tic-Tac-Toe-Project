import time, random

#A function that displays a blank board
def displayInitialBoard():
    initialBoard = [
        [' ',' ',' ','a',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ','c',' ',' '],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['1',' ',' ','-',' ',' ','|',' ',' ','-',' ',' ','|',' ',' ','-',' ',' '],
        [' ','_','_','_','_','_','|','_','_','_','_','_','|','_','_','_','_','_'],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['2',' ',' ','-',' ',' ','|',' ',' ','-',' ',' ','|',' ',' ','-',' ',' '],
        [' ','_','_','_','_','_','|','_','_','_','_','_','|','_','_','_','_','_'],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['3',' ',' ','-',' ',' ','|',' ',' ','-',' ',' ','|',' ',' ','-',' ',' '],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ']]
    for line in initialBoard:
            print(*line, sep = '')

#The introductory sequence for whenever the game is first ran
def intro():
    print("""
=======================
Welcome to Tic Tac Toe!
=======================
    """)
    time.sleep(1.5)
    displayInitialBoard()
    time.sleep(0.5)
    print("""
TUTORIAL:
-The board is shown above. To make a move, type the letter followed
by the number corresponding to your chosen grid location.
-The object of the game is to fill three grid locations in a row
with your icon, either a row, a columnm or diagonally.
-Your moves will be represented on the board with
the icon 'X' and mine will be the icon 'O'
    """)
    time.sleep(1)

#The main game of Tic Tac Toe
def main():
    #Dictionary which tracks the status of moves
    #made to the gameboard, and prevents overwriting
    #previous moves

    previousMoves = {'a1':'-', 'b1':'-', 'c1':'-',
                      'a2':'-', 'b2':'-', 'c2':'-',
                      'a3':'-', 'b3':'-', 'c3':'-'}

    playerIcon = 'X'
    computerIcon = 'O'

    #The loop used to restart the game if the player wants,
    #or exit the program if they are done playing
    def restart_loop():
        restart = str.lower(str.strip(input('\nWould you like to play again? (yes/no) ')))
        if restart in ("yes","y"):
            print('')
            displayInitialBoard()
            main()
        elif restart in ("no","n"):
            exit()
        else:
            print("\nPlease answer with either yes/no or y/n.")
            restart_loop()

    #Prints the board using dictionary
    #keys to refrence the status of each grid
    def printTheBoard():
        gameBoard=[
        [' ',' ',' ','a',' ',' ',' ',' ',' ','b',' ',' ',' ',' ',' ','c',' ',' '],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['1',' ',' ',previousMoves['a1'],' ',' ','|',' ',' ',previousMoves['b1'],' ',' ','|',' ',' ',previousMoves['c1'],' ',' '],
        [' ','_','_','_','_','_','|','_','_','_','_','_','|','_','_','_','_','_'],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['2',' ',' ',previousMoves['a2'],' ',' ','|',' ',' ',previousMoves['b2'],' ',' ','|',' ',' ',previousMoves['c2'],' ',' '],
        [' ','_','_','_','_','_','|','_','_','_','_','_','|','_','_','_','_','_'],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' '],
        ['3',' ',' ',previousMoves['a3'],' ',' ','|',' ',' ',previousMoves['b3'],' ',' ','|',' ',' ',previousMoves['c3'],' ',' '],
        [' ',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ','|',' ',' ',' ',' ',' ']]

        for line in gameBoard:
            print(*line, sep = '')

    #Asks the player for their move,
    #which is then cleaned and passed
    #through the dictionary of board values
    def playerMove():
        playerChoice = str.lower(str.strip((input('\nWhat is your move? '))))
        if (playerChoice,'-') in previousMoves.items():
            previousMoves[playerChoice] = playerIcon
            printTheBoard()
        elif (playerChoice,'X') in previousMoves.items() or (playerChoice,'O') in previousMoves.items():
            print('\nThis move is already taken!')
            playerMove()
        else:
            print("\nThat isn't a valid move! Try again.")
            playerMove()

    #The cumputer makes a random move using a list of keys
    #from the dictionary of board values, which is then
    #passed through the dictionary
    def computerMove():
        computerChoice = random.choice(list(previousMoves.keys()))
        if (computerChoice,'-') in previousMoves.items():
            previousMoves[computerChoice] = computerIcon
            printTheBoard()
            return
        else:
            computerMove()

    #The primary gameplay loop, which continuously passes the turn
    #between the player and the computer, and checks if any of the possible
    #win conditions have been met, or the board is full
    def gamePlayLoop():
        for turnCount in range(1, 11):

            if (previousMoves['a1'] == previousMoves['b1'] == previousMoves['c1'] !='-' or
            previousMoves['a2'] == previousMoves['b2'] == previousMoves['c2'] !='-' or
            previousMoves['a3'] == previousMoves['b3'] == previousMoves['c3'] !='-' or
            previousMoves['a1'] == previousMoves['a2'] == previousMoves['a3'] !='-' or
            previousMoves['b1'] == previousMoves['b2'] == previousMoves['b3'] !='-' or
            previousMoves['c1'] == previousMoves['c2'] == previousMoves['c3'] !='-' or
            previousMoves['a1'] == previousMoves['b2'] == previousMoves['c3'] !='-' or
            previousMoves['c1'] == previousMoves['b2'] == previousMoves['a3'] !='-'):
                if turnCount % 2 == 0:
                    print('You win! Congratulations!')
                    break
                elif turnCount % 2 == 1:
                    print('I win! Nice try!')
                    break
            if turnCount == 10:
                print("It's a tie!")
                break
            elif turnCount % 2 == 1:
                playerMove()
            elif turnCount % 2 == 0:
                computerMove()
    gamePlayLoop()
    restart_loop()

intro()
main()
