eng=int(input("enter marks in english : "))
mat=int(input("enter marks in maths : "))
cs=int(input("enter marks in computer science : "))
total=eng+mat+cs
avg=total/3
if(avg>=80):
    print("Grade A")
if(avg>=70 and avg<=69):
    print("Grade B")
if(avg>=60 and avg<=69):
    print("Grade C")
if(avg>=50and avg<=59):
    print("Grade D")
if(avg>=40 and avg<=49):
    print("Grade E")
if(avg<=39):
    print("Grade R")
