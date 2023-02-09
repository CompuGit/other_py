l=[2,1,31,34,66,42,90]
print("Initial List is :",l)
n=len(l)
for i in range(n):
    for j in range(0,n-1-i):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print("Sorted List is :",l)
