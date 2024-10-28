def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:  # 0 represents an empty space
                return (i, j)  # row, column
    return None

def is_valid(board, guess, row, col):
    # Check the row
    for j in range(len(board[0])):
        if board[row][j] == guess:
            return False

    # Check the column
    for i in range(len(board)):
        if board[i][col] == guess:
            return False

    # Check the 3x3 square
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == guess:
                return False

    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:  # No empty space means the board is solved
        return True
    else:
        row, col = empty

    for guess in range(1, 10):  # Numbers 1 to 9
        if is_valid(board, guess, row, col):
            board[row][col] = guess  # Place the guess

            if solve_sudoku(board):  # Recursively try to solve
                return True

            board[row][col] = 0  # Reset (backtrack)

    return False  # Trigger backtracking

# Example Sudoku puzzle (0 represents empty spaces)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
