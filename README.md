# Tic-Tac-Toe-Project

A human vs computer game of tic tac toe, built using Python 3. I made this project in order to practice and display 
a large portion of my knowledgebase as I learn more about Python. I hope to update this project in fun ways as I learn
more about the language. I plan to add features including a difficulty setting, a local leaderboard, and a save file 
using .txt files. I'm always excited to learn more efficient ways to implement the features of my code, so please feel 
free to give any suggestions on anything that was written amateurishly.

------
UPDATE LOG:
------

Ver 1.10, Leaderboard Update:

Added the long toiled hard mode. The player will now be asked to choose a difficulty when they first start a game, which will then be stored and implemented by the AI to determine what logical method it will use to make its moves. In hard mode, the AI will: check the board to see if it's about to win and make that move if so, if not it will check if the player is about to win and steal that move, and if no one is about to win it will choose a random spot. The AI will only think one move in advance, as I decided any further strategizing would make such a simple game unwinnable by the player (this feature may be implemented in a "very hard" mode for example).

Ver 1.04:
General bug fixes for user inputs.

Ver 1.03, Leaderboard Update:
The player can now display a leaderboard of their stats. So far only shows wins, losses, ties, and W/L ratio for one player at a time, but may be updated to show more. Username has to be consistent to track stats for you.

Ver 1.02, Savefile Update:
The game will now create a save file wherever it is saved on your computer which stores game statistics for each game played by the username chosen by the player.
