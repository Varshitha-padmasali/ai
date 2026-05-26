def print_solution(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
    print()
def solve_nqueens(board,col,n):
    if col>=n:
        print_solution(board,n)
        return True
    res=False
    for i in range(n):
        if is_safe(board,i,col,n):
            board[i][col]=1
            res=solve_nqueens(board,col+1,n) or res
            board[i][col]=0
    return res

n=int(input("Enter the value of n : "))
board=[[0 for _ in range(n)] for _ in range(n)]
if not solve_nqueens(board,0,n):
    print("No Solution Found")


    