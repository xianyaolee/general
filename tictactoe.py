import time

print("Please key in Player 1 name.")
player_one_name = input()
print("Please key in Player 2 name.")
player_two_name = input()
print("Hi, {name_one} and {name_two}".format(name_one = player_one_name,name_two = player_two_name))

# default board with no inputs
theBoard = {"1": " ","2": " ","3": " ","4": " ","5": " ","6": " ","7": " ","8": " ",
"9": " "}

# print the status of the board
def printBoard(board):
    print("|"+board["1"]+"|"+board["2"]+"|"+board["3"]+"|")
    print("+-+-+-+")
    print("|"+board["4"]+"|"+board["5"]+"|"+board["6"]+"|")
    print("+-+-+-+")
    print("|"+board["7"]+"|"+board["8"]+"|"+board["9"]+"|")

# to play a turn in tic tac toe game
def play_a_turn(playername, board, first_player = True):
    print("{player}, it\'s your turn!".format(player=playername))
    while True:
        try:
            player_input = input("Pick a number between 1 to 9 (inclusive).")
            if int(player_input) in range(1,10):
                break #why break here? 
        except:
            print("Invalid input, try again!")
            pass
    while board[player_input] != " ":
        print("This box is already selected, try again!")
        player_input = input()
    if first_player == True:
        board[player_input] = "X"
    else:
        board[player_input] = "O"

# to check and return the winner
def check_winner(player_one_name, player_two_name, board):
    winning_combinations = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for winning_combination in winning_combinations:
        if (board[str(winning_combination[0])] != " ") and(board[str(winning_combination[0])] == board[str(winning_combination[1])]) and (board[str(winning_combination[1])] == board[str(winning_combination[2])]):
            global end_game
            end_game += 1
            if board[str(winning_combination[0])] == "X" :
                print("{winner_name} have won!".format(winner_name = player_one_name))
            else:
                print("{winner_name} have won!".format(winner_name = player_two_name))
            printBoard(board)
            break
        else:
            pass

# sequence of the game 
def game(board):
    print("Let's get started.")
    global end_game
    end_game = 0
    for i in range(4):
        if end_game == 0:
            printBoard(board)
            play_a_turn(player_one_name,theBoard, True)
            if i > 1: # duplicate code here as line 70
                check_winner(player_one_name, player_two_name,board) 
        if end_game == 0:
            printBoard(board)
            play_a_turn(player_two_name,theBoard, False)
            if i > 1:
                check_winner(player_one_name, player_two_name,board)
    if end_game == 0:
        printBoard(board)
        play_a_turn(player_one_name,theBoard, True)
        if i > 1:
            check_winner(player_one_name, player_two_name,board)
    if end_game == 0:
        print("It's a draw! It\'s ok, life is not always about winning. :)")

# execute game play and check if the players want to play again after the game.
while True:
    theBoard = {"1": " ","2": " ","3": " ","4": " ","5": " ","6": " ","7": " ","8": " ",
"9": " "}
    game(theBoard)
    try:
        play_again = input("Do you want to play again? Yes/No \n")
        if play_again == "Yes":
            continue
        if play_again == "No":
            break
    except:
        pass

print("Good bye.")
time.sleep(3)

# Some codes are referenced from:
# https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

# potential improvements:
# 1) to modify draw as the draw could take place before the last possible move (e.g. no potential winning combinations.)
