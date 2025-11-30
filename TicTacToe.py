import random

print('Welcome to Tic Tac Toe!')
answer = input("Would you like to play? ").strip().lower()

if answer not in ('y', 'yes', 'sure', 'yeah', 'okay'):
    print("Don't be shy, come back when you are ready!")
    exit()

while True:  
    print("Great, let's get started!")

    choice = input('Choose your character. X or O? ').strip().upper()
    if choice == 'X':
        player, computer = 'X', 'O'
    elif choice == 'O':
        player, computer = 'O', 'X'
    else:
        print('Invalid input. Please enter "X" or "O".')
        continue 

    board = [' '] * 9

    def display_board():
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('-----------')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('-----------')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('\n')

    def player_move():
        while True:
            move = int(input('Enter your move (1-9): '))
            if move < 1 or move > 9:
                print('Invalid move. Please enter a number between 1 and 9.')
            elif board[move - 1] != ' ':
                print('That space is already taken. Please choose another.')
            else:
                board[move - 1] = player
                break

    def computer_move():
        while True:
            move = random.randint(0, 8)
            if board[move] == ' ':
                board[move] = computer
                break

    def check_win():
        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != ' ':
                return True
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != ' ':
                return True
        if board[0] == board[4] == board[8] != ' ':
            return True
        if board[2] == board[4] == board[6] != ' ':
            return True
        return False

    while True:
        display_board()
        player_move()
        if check_win():
            display_board()
            print('Dang it, you beat me! Nice game!')
            break

        computer_move()
        if check_win():
            display_board()
            print('You lose! Better luck next time.')
            break


    again = input('Would you like to play again? (y/n) ').strip().lower()
    if again not in ('y', 'yes', 'sure', 'yeah', 'okay'):
        print('Oh well, goodbye!')
        break