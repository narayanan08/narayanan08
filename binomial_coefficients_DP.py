

def cal_binomial_coefficient(n,k):
    for i in range(0,n+1):
        end=min(i,k)+1
        for j in range(0,end):
            if j==0 or j==i:
                C[i][j]=1
            else:
                C[i][j]=C[i-1][j-1]+C[i-1][j]
            print(C)
    return C[n][k]



n,k=tuple(map(int,input().split()))
C=[[0 for j in range(k+1)] for i in range(n+1)]
print(C)
print()
ans=cal_binomial_coefficient(n,k)
print(ans)
print()
print(C)