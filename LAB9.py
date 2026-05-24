def is_safe(board, row, col, n):
    for i in range(col): # previous columns
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col: #queen in same row, upper left diagonal, lower left diagonal
            return False 
    return True
def solve_csp(board, col, n):
    if col == n: # all queens placed succesfully
        return True
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row #stores queens position
            if solve_csp(board, col + 1, n):
                return True
            board[col] = -1 #if fails remove queen
    return False
def print_solution(board, n):
    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
n = int(input("Enter n : "))
board = [-1] * n
if solve_csp(board, 0, n):
    print("Solution for", n, "Queens Problem:")
    print_solution(board, n)
else:
    print("No solution exists")
    