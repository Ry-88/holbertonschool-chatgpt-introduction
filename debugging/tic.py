def print_board(board):
    """
    Prints the current game board in a formatted style.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks for a winning condition: 3 same symbols in a row, column, or diagonal.

    Returns:
        bool: True if there's a winner, False otherwise
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_draw(board):
    """
    Checks if the board is full and there's no winner.

    Returns:
        bool: True if it's a draw, False otherwise
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(player):
    """
    Prompts the user until a valid row and column are entered.

    Returns:
        tuple: (row, col) integers
    """
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Row and column must be 0, 1, or 2. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def tic_tac_toe():
    """
    Main game loop. Handles player turns, input, board updates, and win/draw detection.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        row, col = get_valid_input(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()