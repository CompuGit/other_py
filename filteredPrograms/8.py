a,b = 0,1
total = 0
result = []

while (b < 1000000):
    a,b = b,a+b
    if( b%2 == 0):
        result.append(b)

total = sum(result)

print(result)
print('The sum of Even Fibonocci under 1000000 is :',total)

