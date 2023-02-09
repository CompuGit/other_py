1.#default arguments
def func(n,z=10):
    return z
print(func(10,20))
print(func(10))

2.#varible length arguments
def func(*arg):
    for a in arg:
        print(a,end=" ")
func(1,2)
print()
func(1,2,3)

3.#keyword arguments used as a variable length arguments
def func(**arg):
    for a in arg:
        print(arg[a],end=" ")
func(a=1,b=2)

4.#fibonanic series using moization i.e we have to store calculated values in one list
def fib(n):
    if (a[n]==-1):   
        if (n==0 or n==1):
            a[n]=n
            return a[n]
            
        else:
            a[n]=fib(n-1)+fib(n-2)
            return a[n]
    else:
        return a[n]
n=int(input("Enter number"))
a=[]
for i in range(0,n+1):
    a.append(-1)
res=fib(n)
print(res)

