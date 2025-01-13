#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.

    Parameters:
        board (list): The game board as a 2D list.

    Returns:
        str: The symbol of the winning player ("X" or "O"), or None if no winner.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_draw(board):
    """
    Check if the game is a draw.

    Parameters:
        board (list): The game board as a 2D list.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()