import random 
#Display Board 
def display_board(board_list):
    print(board_list[7] + '|' + board_list[8] + '|' + board_list[9])
    print(board_list[4] + '|' + board_list[5] + '|' + board_list[6])
    print(board_list[1] + '|' + board_list[2] + '|' + board_list[3])


#Testing 
#board_list = ['#','X','O','X','O','X','O','X','O','X']
#display_board( board_list ) 

#Good test passed first try let's goo!! 

#Asking the player if he wants to be X or O 

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("What would you like to be X or O ?")
    
    player_one = marker 
    if player_one == 'X':
        return ('X','O')
    else:
        return ('O' , 'X')
    #Testing 
#player_input()

# First try easy. 

#Player changing the list 
def place_marker(board_list, marker,position):
    board_list[position] = marker

#place_marker(board_list, "Balram", 1)
#display_board(board_list)




#how win 

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal




def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"
    

def space_check(board,position):

    return board[position] == ''


#checking for empty spaces 
def empty_space(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 



def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Please enter where you want to play next (1-9)" ))

    return position




def replay():
    asking = input("Do you wish to play again ? ")
    if asking == "Yes":
        return True
    else:
        return False 
    

# Real Logic starts now 
while True:
    the_board = ['']*10
    player1_marker, player2_marker = player_input()
    play_game = input("Are you ready to play ? yes or no")
    if play_game == "yes":
        game_on = True 
    else: 
        game_on = False 

    turn = choose_first()
    print("It's" + turn + "turn to go first")
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board,player1_marker):
                print("Congratulations, Player 1 has won the game hes the best!!")
                game_on = False 
            else:
                if empty_space(the_board):
                    print("This game has been a DRAW ! Try again.")
                    break 
                else:
                    turn = 'Player 2'
        
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board,player2_marker):
                print("Congratulations, Player 2 has won the game hes the best!!")
                game_on = False 
            else:
                if empty_space(the_board):
                    print("This game has been a DRAW ! Try again.")
                    break 
                else:
                    turn = 'Player 1'
    if not replay():
        break