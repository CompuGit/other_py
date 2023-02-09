numberslist = [num for num in range(100,1001)]

#list comprehension
squareslist = [n for n in numberslist for i in range(1,len(numberslist)) if n/i==i]

print("\nSquares list is : \n",squareslist)

###method 1###
'''
squareslist = []
for n in numberslist:
    for i in range(1,len(numberslist)):
        if n/i==i:
            squareslist.append(n)
print("\nSquares list is : \n",squareslist)
'''

###method 2###
'''
for i in range(len(numberslist)):
    for j in range(len(numberslist)):
        h = numberslist[i]
        if(h == j**2):
            squareslist.append(h)
print("\nSquares list is : \n",squareslist)
'''

###method 3###
'''
def find(n):
    for i in range(1,len(numberslist)):
        if n/i==i:
            return True

numberslist = [num for num in range(100,1001)]

squareslist = list(filter(lambda x:find(x),numberslist))
print(squareslist)

'''

