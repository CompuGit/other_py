#power set of the given characters
l=input().split()
n=len(l)
r=2**n
print("{",end="")
for i in range(r):
    temp=i
    print("{",end="")
    for j in range(n):
        res=temp%2
        temp=temp//2
        if(res == 1):
            print(l[j],end="")
    print("}",end=",")
print("}") 
