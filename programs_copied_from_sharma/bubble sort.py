a=[2,32,43,12,4,55,28]
print("Intial List is : ",a)
for j in range(len(a)):
    swapped=False
    i=0
    while i<len(a)-1:
        if(a[i]>a[i+1]):
           a[i],a[i+1]=a[i+1],a[i]
           swapped=True
        i+=1
    if(swapped==False):
           break
print("Sorted List is : ",a)
