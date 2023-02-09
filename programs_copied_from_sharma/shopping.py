amt=int(input("enter the amount : "))
if(amt<1000):
    x=5/100*amt
    y=amt-x
    print("amount has to be paid : ",y)
if(amt>=2000 and amt<=9999):
    z=15/100*amt
    n=amt-z
    print("amount has to be paid : ",n)
if(amt>10000):
    m=25/100*amt
    p=amt-m    
    print("amount has to be paid : ",m, "you got a gift voucher ")
    
         
