1.class student:
    s_var=10
    def __init__(self):
        self.name="sai"
s=student()
s1=student()
student.s_var=20

print(s.s_var)
s.s_var=4#here it's create a variable to that object
print(s1.s_var)

output:
20
20

2.private variable

class student:
    __s_var=10
    def __init__(self):
        self.name="sai"
    def display(self):
        print(self.__s_var)
s=student()
s1=student()
print(s._student__s_var)
print(s.display())

output:
10
10
None

3.Accessing variable without initializing
class student:
    def __init__(self):
        self.name="sai"
    def mul(self):
        self.p=5
        self.b=10
        self.c=5
        return self.p*self.b*self.c
class student1(student):
    def __init(self):
        self.b1=10
        self.c=4
        self.a=6
    def add(self):
        self.a=self.b1+self.c
s1=student()
s=student()
print(s1.b)
print(s1.mul())

output:
Traceback (most recent call last):
  File "C:/Users/STUDENT/Desktop/gec/1.py", line 18, in <module>
    print(s1.b)
AttributeError: 'student' object has no attribute 'b'

2.Accessing after initializing and for "single level inheritance"
class student:
    def __init__(self):
        self.name="sai"
    def mul(self):
        self.p=5
        self.b=10
        self.c=5
        return self.p*self.b*self.c
class student1(student):
    def __init(self):
        self.b1=10
        self.c=4
        self.a=6
    def add(self):
        self.a=self.b1+self.c
s1=student()
s=student()
print(s1.mul())
print(s1.b)
output:
250
10

3.Multiple Inheritance
i.
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(C,B):#here first parameter is c so it's printing c
    pass
d=D()
d.show()

output:
c
ii.
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B,C):#here first parameter is B so it's printing B
    pass
d=D()
d.show()

output:
B

5.Balanced paranthesis:
======================
class Stack:
    l=[]
    def push(self,a):
        self.l.append(a)
    def pop(self):
        if len(self.l)!=0:
            b=self.l.pop()
            return b
        return -1
    def top(self):
        return self.l[-1]
s=Stack()
string=input()
flag=0
d={"{":"}","(":")","[":"]",-1:0}
for i in string:
    if i=="(" or i=="[" or i=='{':
        s.push(i)
    elif i!=d[s.pop()]:
        flag=1
        break
if flag==0 and len(s.l)==0:
    print("balanced")
else:
    print("Un balanced")

output:
1.





