from re import A

a=int(input("give amount:"))
def fib(n):
    a,b=0,1
    for _ in range(n):
     yield a
     a,b=b,a+b
print(list(fib(a)))
    