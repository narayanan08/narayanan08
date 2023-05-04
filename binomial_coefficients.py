def cal_binomial_coefficient(n,k):
    if k>n:
        return 0
    if k==n or k==0:
        return 1
    return cal_binomial_coefficient(n-1,k-1)+cal_binomial_coefficient(n-1,k)

ans=cal_binomial_coefficient(5,3)
print(ans)