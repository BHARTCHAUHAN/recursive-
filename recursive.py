def facto(n):
    f=1
    while n>0:
        f=f*n
        n=n-1
        return f
    n=int(input("enter any number:-"))
    result=facto(n)
    print("factorial of",n,result)