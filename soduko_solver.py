soduku_lenght = 9
row_num = 3
col_num = 3
#takies in an array of arrays
def solver(board):
    empty_cell = finding_empty(board)
    #this means that the bored is solved because if cell is full
    if not empty_cell:
        return True  

    row, col = empty_cell

    for num in range(1, 10):
        if iscorrect(board, row, col, num):
            board[row][col] = num

            if solver(board):
                return True

            board[row][col] = 0  

    return False

def finding_empty(board):
    for row in range(soduku_lenght):
        for col in range(soduku_lenght):
            if board[row][col] == 0:
                return row, col
    return None

def iscorrect(board, row, col, num):
    for i in range(soduku_lenght):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = row_num * (row // row_num), col_num * (col // col_num)
    for i in range(row_num):
        for j in range(col_num):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def return_board(board):
    return board

sudoku_board = [
    #array of arrays
]

if solver(sudoku_board):
    return_board(sudoku_board)
else:
    print("No solution exists.")