#count no.of Unbalanced parantheses:
#===================================
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
count=0
d={"{":"}","(":")","[":"]",-1:0}
for i in string:
    if i=="(" or i=="[" or i=='{':
        s.push(i)
    elif i!=d[s.pop()]:
        flag=1
        count+=1
count=count+len(s.l)
if flag==0 and len(s.l)==0:
    print("balanced")
else:
    print("Un balanced")
    print("count is:",count)

