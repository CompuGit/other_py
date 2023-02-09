#WAP to get any two numbers from user to start fibonacci series until k numbers
#Input : 0 1 12 #0 and 1 are the two number and k is 12
#Output : 0 1 1 2 3 5 8 13 21 34 55 89

x,y,k = input().split()
x,y,k = int(x), int(y), int(k)

for i in range(k):
    print(x,end=' ')
    x,y = y,x+y
