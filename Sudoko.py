# Function to check if placing a number is valid
def is_valid(board, row, col, num):
    # Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is in the 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):
                            return True
                        
                        board[row][col] = 0  # Reset if it leads to dead end
                return False
    return True

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Example of a Sudoku puzzle (0 represents empty cells)
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

print("Sudoku Board Before Solving:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSudoku Board After Solving:")
    print_board(sudoku_board)
else:
    print("No solution exists for this Sudoku puzzle.")
# Function to check if placing a number is valid
def is_valid(board, row, col, num):
    # Check if the number is in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is in the 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False

    return True

# Function to solve the Sudoku board using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):
                            return True
                        
                        board[row][col] = 0  # Reset if it leads to dead end
                return False
    return True

# Function to print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Example of a Sudoku puzzle (0 represents empty cells)
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

print("Sudoku Board Before Solving:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSudoku Board After Solving:")
    print_board(sudoku_board)
else:
    print("No solution exists for this Sudoku puzzle.")
