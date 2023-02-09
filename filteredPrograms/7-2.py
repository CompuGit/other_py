x,y,z = input('Enter three numbers to start fibonocci series : ').split()
x,y,z = int(x),int(y),int(z)

for i in range(15):
    print(x,end=' ')
    x,y,z = y,z,x+y
