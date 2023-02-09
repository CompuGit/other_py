while(True):
    print("enter the number of your choice")
    print("1.To calculate simple interest")
    print("2.To calculate coumpound interest")
    print("3.Quit")
    ch=int(input("enter your choice"))
    if(ch==1):
       p=int(input("enter principal"))
       t=int(input("enter time peroid"))
       r=int(input("enter rate"))
       si=p*t*r/100
       print("The simple Interest is :",si)
    if(ch==3):
       break
    if(ch==2):
       p=int(input("enter principal"))
       t=int(input("enter time peroid"))
       r=int(input("enter rate"))
       ci=p*t+r/100
       print("The compound interest is :",ci)
    
