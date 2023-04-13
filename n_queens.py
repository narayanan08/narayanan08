c=0
def solve(solution,N,col=0):
    global c
    if col==N:
        c+=1
        print(c)
        for row in solution:
            print(row)
        print()
    else:
        for row in range(N):
            if check_row(solution,row)==True and check_diagonal(solution,row,col,N)==True:
                solution[row][col]="Q"
                s=solve(solution,N,col+1)
                solution[row][col]='#'
        

def check_row(intermediate,i):
    if 'Q' not in intermediate[i]:
        return True
    else:
        return False

def check_diagonal(intermediate,i,j,N):
    i_upper=i
    j_upper=j
    while (i_upper>=0 and j_upper>=0):
        if intermediate[i_upper][j_upper]=='Q':
            return False
        i_upper-=1
        j_upper-=1
    
    i_down=i
    j_down=j
    while (i_down<N and j_down>-1):
        if intermediate[i_down][j_down]=='Q':
            return False
        i_down+=1
        j_down-=1
    
    return True

    
N=8

chess_board=[['#' for i in range(N)]for j in range(N)]
for row in chess_board:
    print(row)

print()
solve(chess_board,N)
