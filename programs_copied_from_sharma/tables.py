#WAP to print desired math table for n X k

n=int(input("enter number which table has to be printed : "))
k=int(input("enter value to which table has to be printed : "))

i=1
while(i<=k):
    print(n,"x",i,"=",n*i)
    i+=1

