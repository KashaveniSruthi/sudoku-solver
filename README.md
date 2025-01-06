# Sudoku Solver and Generator

A Python-based Sudoku solver and generator using `tkinter`. This project allows users to generate, solve, and interact with Sudoku puzzles. The solver uses a backtracking algorithm to find solutions, and the generator creates puzzles of varying difficulty levels.

## Features

- **Interactive Grid**: 
  - Click on cells to edit values.
  - Highlight editable cells in green and non-editable cells (clues) in red.
  
- **Puzzle Generator**:
  - Generates a Sudoku puzzle of varying difficulty levels (1-5).
  - Randomly removes values from a solved Sudoku grid to create a valid puzzle.

- **Puzzle Solver**:
  - Solves any given Sudoku puzzle using a backtracking algorithm.
  - Provides visual feedback during the solving process.

- **Customizable Interface**:
  - Buttons for generating a new puzzle, solving the current puzzle, and selecting difficulty levels.



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KashaveniSruthi/sudoku-solver.git
   cd sudoku-solver
   
2. Make sure you have Python installed (Python 3.x recommended).

3. Install tkinter (usually comes pre-installed with Python:
     pip install tk
4. Run the application:
     python sudoku_solver.py

**Usage**

1. Generate Puzzle: Click the Generate button to create a random Sudoku puzzle. You can adjust the difficulty using the dropdown menu.
2. Solve Puzzle: Click the Solve button to automatically solve the current puzzle.
3. Edit Cells: Click on editable cells and type in values to modify the puzzle. Editable cells are marked in green.

**Algorithm**

-The puzzle is solved using a backtracking algorithm that tries numbers 1-9 in empty cells and checks if they satisfy Sudoku constraints:

  -The number must be unique in the row.
  -The number must be unique in the column.
  -The number must be unique in the 3x3 subgrid.
-The puzzle generation uses a randomized approach to fill the diagonal sub-grids first, then solves the grid, and finally removes values to create the puzzles.

**Contributing**

Feel free to fork this repository and submit issues or pull requests if you'd like to contribute.

**License**

This project is open-source and available under the MIT License.

**Acknowledgments**

Special thanks to the contributors and the Python community.
The backtracking algorithm for Sudoku solving is based on well-known solving methods.
