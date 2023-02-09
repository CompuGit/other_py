classxi=dict() 
n=int(input("Enter total number of section in xi class"))
i=1 
while i<=n:
    a=raw_input("enter section") 
    b=raw_input ("enter class teacher name") 
    classxi[a]=b 
    i=i+1 
    print ("Class","\t","Section","\t","teacher name" )
for i in classxi:
    print("XI","\t",i,"\t",classxi[i])
