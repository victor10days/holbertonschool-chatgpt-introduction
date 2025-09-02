#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if all(cell == row[0] and cell != " " for cell in row):
            return True

    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(len(board))):
            return True

    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(len(board))):
        return True

    if all(board[i][2-i] == board[0][2] and board[0][2] != " " for i in range(len(board))):
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")
    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()