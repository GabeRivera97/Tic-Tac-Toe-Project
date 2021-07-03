import time, random

userName = None

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
-The board is shown above. To make a move, type the letter followed by the number corresponding to your chosen grid location.
-The object of the game is to fill three grid locations in a row with your icon, either a row, a columnm or diagonally.
-Your moves will be represented on the board with the icon 'X' and mine will be the icon 'O'
    """)
    time.sleep(1)
    global userName
    userName = str.capitalize(str.strip(input('Enter your username (or make a new one): ')))
    usernameCheck(userName)

#Checks the username passed to it from the intro function.
#Creates a new save file if the username hasnt been used or edits
#the players stats if they have played before. Also allows the user to
#access their stats or play the game
def usernameCheck(name):
    try:
        saveFileDoc = open("TicTacToeSaveFiles.txt" , "r+")
        fileLines = saveFileDoc.read()
        textList = fileLines.split()
        if userName in textList:
            choiceReturn = str.lower(str.strip(input('Welcome back, ' +  userName + ", to view the your stats type 'L', to play type 'P' ")))
            if choiceReturn == 'p':
                main()
            elif choiceReturn == 'l':
                displayLeaderboard()
        elif userName not in textList:
            saveFileDoc.write(userName + ' 0 0 0 ')
            saveFileDoc.close()
            choiceNew = str.lower(str.strip(input('Hello ' + userName + ", it looks like you haven't played before. I've created a save file for you. To play type 'P', to exit type 'E'.")))
            if choiceNew == 'p':
                main()
            elif choiceNew == 'e':
                exit()
    except FileNotFoundError:
        
        open("TicTacToeSaveFiles.txt" , "w")
        usernameCheck(userName)

#Pulls stats from the text file containing usernames,
#and displays the sats of the player
def displayLeaderboard():
    saveFileDoc = open("TicTacToeSaveFiles.txt" , "r+")
    fileLines = saveFileDoc.read()
    textList = fileLines.split()
    print("Displaying gameplay statistics for " + userName + ":")
    print("Wins = " + str(textList[textList.index(userName) + 1]))
    print("Losses = " + str(textList[textList.index(userName) + 2]))
    print("Ties = " + str(textList[textList.index(userName) + 3]))
    try:
        print("Win/Loss Ratio = " + str(int(textList[textList.index(userName) + 1]) / int(textList[textList.index(userName) + 2])))
        saveFileDoc.close()
    except ZeroDivisionError:
        print("Win/Loss Ratio = " + str(float(textList[textList.index(userName) + 1])) + " (You have never lost a game)")
    def afterStats():
        restart = str.lower(str.strip(input('\nReturn to main menu? (yes/no) ')))
        if restart in ("yes","y"):
            intro()
        elif restart in ("no","n"):
            exit()
        else:
            print("\nPlease answer with either yes/no or y/n.")
            afterStats()
    afterStats()

#Displays a blank board
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
        elif restart in("mainmenu"):
            intro()
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
                    leaderboardUpdate(1)
                    break
                elif turnCount % 2 == 1:
                    print('I win! Nice try!')
                    leaderboardUpdate(2)
                    break
            if turnCount == 10:
                print("It's a tie!")
                leaderboardUpdate(3)
                break
            elif turnCount % 2 == 1:
                playerMove()
            elif turnCount % 2 == 0:
                computerMove()

    #Updates the stats associated with the players username after the game is over
    def leaderboardUpdate(winner):
        saveFileDoc = open("TicTacToeSaveFiles.txt" , "r+")
        fileLines = saveFileDoc.read()
        textList = fileLines.split()
        textList[textList.index(userName) + winner] = str(int(textList[textList.index(userName) + winner]) + 1)
        newSave = ' '.join(textList)
        saveFileDoc.seek(0)
        saveFileDoc.write(newSave)
        saveFileDoc.close()
        
    gamePlayLoop()
    restart_loop()

intro()
