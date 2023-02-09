a=[23,32,12,7,5,98,24,9]
print("Intial List is : ",a)
for index in range(1,len(a)):
    currentvalue=a[index]
    position=index
    while(position>0 and a[position-1]>currentvalue):
        a[position]=a[position-1]
        position=position-1
    a[position]=currentvalue
print("Sorted List is : ",a)
