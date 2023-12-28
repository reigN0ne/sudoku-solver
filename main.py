board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for row_idx, row in enumerate(board):
        print("--------------------------")
        for col_idx, column in enumerate(row):
            print(board[row_idx][col_idx], end=" ")
            if col_idx == 8:
                print("||")
            elif (col_idx + 1) % 3 == 0 and col_idx != 0:
                print("||", end=" ")
    print("--------------------------")
    
def row_check(board):
    pass

def column_check(board):
    pass

def grid_check(board):
    pass

def solve(board):
    pass

print_board(board)