import math
n=int(input("enter any number "))
i=2
j=0
while i<(math.floor(math.sqrt(n))):
    if(n%i)==0:
            j=0
            print(n,"is not a prime number")
            break
    else:
         i+=1
         j=1               
if(j==1):
    print(n,"is a prime number")
    
    
    
       
