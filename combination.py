def myfact(n):
    if n==1:
        return n
    else:
        return n*myfact(n-1)


def combination(n,r):
    return (myfact(n)/  (myfact(r))*(myfact(n-r)) )

n=5 
r=3
print(combination (n,r))
