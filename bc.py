def binomial_coefficient(n,k):
    #formula=n!/(n-k)!k!
    d=n-k
    n-=d
    t=(i for i in range(d+1,n+1))
    num=1
    for i in t:
        num*=i
    den=1
    for i in range(1,k+1):
        den*=i
    return num/den

print(binomial_coefficient(5,3))

