
# def facto(n):
#     f=1
#     while n>0:
#         f=f*n
#         n=n-1
#         return f
# n = int(input("enter any number:-"))
# result=facto(n)
# print("factorial of ",n,result)

def digitalsum():
    sum=0
    while n>0:
        rem = n%10
        sum=sum+sum
        n=n//10
        return(sum)
    n= int(input("enter the number"))
    s = digitalsum(n)
    print(s)
        