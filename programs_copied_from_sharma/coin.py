#WAP to to flip coin n times and show counts of heads and tails in (heads, tails) tuple

import random
n=int(input("no of times coin is flipped : "))
i=1
head=0
tail=0
while(i<=n):
    x=(random.random())
    if(round(x))>0:
        head+=1
    else:
        tail+=1
    i+=1
print("no of heads: ",head)
print("no of tails :",tail)
        

