import math
n=int(input("enter any number: "))
y=" "
while(n>0):
    rem=n%2
    math.floor(rem)
    y+=str(rem)
    n=int(n/2)
    math.floor(n)
print(y[::-1])
    
