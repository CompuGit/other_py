n=int(input("enter any number"))
x=n*n
digits=len[x]
temp=n
while(temp!=0):
    digits+=1
    temp=temp/10
    rem=temp%10
    s=pow(rem,digits)
    if(n==sum):
        print("  armstrong number")
    else:
        print("not armstrong number")


