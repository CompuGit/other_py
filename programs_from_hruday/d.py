n=int(input("enter number of rows:"))
m=int(input("multiple of rows:"))
n1=n
r=(m-7)//2  # for it is use ful at i==size i.e both ends of the welcome are same
size=n//2+1 #It is for finding center element
s1=n//2*3   #It is for how many "-" are to calculate
k=1         #intitalizing ".|."
for i in range(1,n+1):
    if i < size:
        print(("-"*s1)+(".|."*k)+("-"*s1))
    elif i==size:
        print(("-"*r)+"welcome"+("-"*r))
    else:
        pass
    k=k+2
    s1=s1-3
k1=k-2
s1=s1+3
for i in range(1,n+1):
    if i>size:
        print(("-"*s1)+(".|."*k1)+("-"*s1))
    else:
        pass
    k1=k1-2
    s1=s1+3
    
        
'''  
output:
1.enter number of rows:7
multiple of rows:21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------welcome-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

2.enter number of rows:9
multiple of rows:27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------welcome----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''
