import sys
import copy
import random


game_board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
winning_conditions = [['X', 'X', 'X'], ['O', 'O', 'O']]


def print_board(game_board):
    print ' ', '1', '2', '3'
    print '1', ' '.join(game_board[0])
    print '2', ' '.join(game_board[1])
    print '3', ' '.join(game_board[2])
    print
 

def assign_player_token(plays_first):
    if plays_first.lower() == 'h':
        player_token = 'X'
    else:
        player_token = 'O'
    return player_token


def assign_computer_token(plays_first):
    if plays_first.lower() == 'h':
        computer_token = 'O'
    else:
        computer_token = 'X'
    return computer_token


def player_move(player_token):    
    while True:
        player_row_guess = -1
        while player_row_guess not in range(0, 3):
            try:
                player_row_guess = raw_input('Enter a row (1-3): ')
                player_row_guess = int(player_row_guess) - 1              
            except ValueError:
                print "Oops, that wasn't a number!"              
        player_column_guess = -1
        while player_column_guess not in range(0, 3):
            try:
                player_column_guess = raw_input('Enter a column (1-3): ')
                player_column_guess = int(player_column_guess) - 1 
            except ValueError:
                print "Oops, that wasn't a number!"
        if game_board[player_row_guess][player_column_guess] == '_':       
            game_board[player_row_guess][player_column_guess] = player_token           
            break
        else:
            print "Oops, that space has already been chosen!"
    print   


def winning_computer_move(computer_token):    
    for i in range(0, 3):
        for j in range(0, 3):
            if game_board[i][j] == '_':
                game_board_copy = copy.deepcopy(game_board)                
                game_board_copy[i][j] = computer_token
                if check_winning_conditions(winning_conditions, game_board_copy):
                    game_board[i][j] = computer_token
                    return game_board


def block_player_win(computer_token, player_token):    
    for i in range(0, 3):
        for j in range(0, 3):
            if game_board[i][j] == '_':
                game_board_copy = copy.deepcopy(game_board)                
                game_board_copy[i][j] = player_token
                if check_winning_conditions(winning_conditions, game_board_copy):
                    game_board[i][j] = computer_token
                    return game_board


def play_corner(computer_token):      
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for row, column in corners:
        if game_board[row][column] == '_':
            game_board[row][column] = computer_token
            return game_board


def play_center(computer_token):    
    if game_board[1][1] == '_':
        game_board[1][1] = computer_token
        return game_board


def play_sides(computer_token):    
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for row, column in sides:
        if game_board[row][column] == '_':
            game_board[row][column] = computer_token
            return game_board


def computer_move(computer_token, player_token):    
    print "The computer makes its move:"
    if winning_computer_move(computer_token):
        winning_computer_move
    elif block_player_win(computer_token, player_token):
        block_player_win
    elif play_corner(computer_token):        
        play_corner
    elif play_center(computer_token):
        play_center
    else:
        play_sides(computer_token)
    print


def check_board_full(game_board):
    return ('_' not in game_board[0] and '_' not in game_board[1] 
           and '_' not in game_board[2])


def check_winning_conditions(winning_conditions, game_board):
    return (winning_conditions[0] == game_board[0] or
            winning_conditions[1] == game_board[0] or
            winning_conditions[0] == game_board[1] or
            winning_conditions[1] == game_board[1] or
            winning_conditions[0] == game_board[2] or
            winning_conditions[1] == game_board[2] or
            winning_conditions[0] == [game_board[0][0], 
                                      game_board[1][0], 
                                      game_board[2][0]] or
            winning_conditions[1] == [game_board[0][0], 
                                      game_board[1][0], 
                                      game_board[2][0]] or
            winning_conditions[0] == [game_board[0][1], 
                                      game_board[1][1], 
                                      game_board[2][1]] or
            winning_conditions[1] == [game_board[0][1], 
                                      game_board[1][1], 
                                      game_board[2][1]] or
            winning_conditions[0] == [game_board[0][2], 
                                      game_board[1][2], 
                                      game_board[2][2]] or
            winning_conditions[1] == [game_board[0][2], 
                                      game_board[1][2], 
                                      game_board[2][2]] or
            winning_conditions[0] == [game_board[0][0], 
                                      game_board[1][1], 
                                      game_board[2][2]] or
            winning_conditions[1] == [game_board[0][0], 
                                      game_board[1][1], 
                                      game_board[2][2]] or
            winning_conditions[0] == [game_board[0][2], 
                                      game_board[1][1], 
                                      game_board[2][0]] or
            winning_conditions[1] == [game_board[0][2], 
                                      game_board[1][1], 
                                      game_board[2][0]])


def play_game(game_board, winning_conditions):
    while True:
        plays_first = raw_input("Who should play first, (h)uman or (c)omputer? ")
        print        
        if plays_first.lower() == 'h' or plays_first.lower() == 'c':
            player_token = assign_player_token(plays_first)
            computer_token = assign_computer_token(plays_first)
            print_board(game_board)
            break
    while True:                
        if check_board_full(game_board) == True:            
            print "The board is full!"        
            break
        else:
            None
        if plays_first.lower() == 'h':            
            player_move(player_token)
            print_board(game_board)
            if check_winning_conditions(winning_conditions, game_board) == True:
                print "You win!"
                break
        else:
            computer_move(computer_token, player_token)
            print_board(game_board)                
            if check_winning_conditions(winning_conditions, game_board) == True:                
                print "The computer wins!"
                break                        
        if check_board_full(game_board) == True:            
            print "The board is full!"                    
            break
        else:
            None
        if plays_first.lower() == 'h':
            computer_move(computer_token, player_token)
            print_board(game_board)                
            if check_winning_conditions(winning_conditions, game_board) == True:                
                print "The computer wins!"
                break
        else:            
            player_move(player_token)
            print_board(game_board)
            if check_winning_conditions(winning_conditions, game_board) == True:
                print "You win!"
                break        


def reset_game_board(game_board):     
    game_board = [['_', '_', '_'],['_', '_', '_'],['_', '_', '_']]
    return game_board 


def close_program():
    print "Thanks for playing!"
    exit_program = raw_input("Press 'Enter' to close the program.")
    sys.exit()


print "Let's play tic-tac-toe!"
print
while True:    
    play_game(game_board, winning_conditions)
    while True:
        play_again = raw_input('Would you like to play again (y/n)? ')
        print
        if play_again.lower() == 'y':
            game_board = reset_game_board(game_board)
            break
        elif play_again.lower() == 'n':            
            close_program()
        else:
            None