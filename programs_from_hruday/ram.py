#linked lists "creation" and "insertion"
class Node:
    def __init__(self,v=-1):
        self.val=v
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,pos,value):
        node=Node(value)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        node.next=temp.next
        temp.next=node
    def __str__(self):
        temp=self.head
        st=""
        while(temp):
            st+=str(temp.val)+" "
            temp=temp.next
        return st+"\n"
l1=Linkedlist()
n=int(input("Enter how many values you want: "))
temp=Node()
for i in range(n):
    val=int(input("Enter value"+str(i+1)+": "))
    node=Node(val)
    if(l1.head==None):
        l1.head=node
        temp=node
    else:
        temp.next=node
        temp=node
print("Elements in linked list are: ",l1)
#Insert at the middle
pos,value=map(int,input().split())
l1.insert(pos,value)
print(l1)

output:
Enter how many values you want: 5
Enter value1: 1
Enter value2: 2
Enter value3: 3
Enter value4: 4
Enter value5: 5
Elements in linked list are:  1 2 3 4 5 

2 98
1 2 98 3 4 5 

2.#Identifying "kth" element from yhe linked list
class Node:
    def __init__(self,v=-1):
        self.val=v
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,pos,value):
        node=Node(value)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        node.next=temp.next
        temp.next=node
    def kth_element(self,kpos):
        t1=self.head
        temp=self.head
        for i in range(kpos):
            temp=temp.next
        while(temp):
            temp=temp.next
            t1=t1.next
        return t1
            
    def __str__(self):
        temp=self.head
        st=""
        while(temp):
            st+=str(temp.val)+" "
            temp=temp.next
        return st+"\n"
l1=Linkedlist()
n=int(input("Enter how many values you want: "))
temp=Node()
for i in range(n):
    val=int(input("Enter value"+str(i+1)+": "))
    node=Node(val)
    if(l1.head==None):
        l1.head=node
        temp=node
    else:
        temp.next=node
        temp=node
print("Elements in linked list are: ",l1)
#Insert at the middle
pos,value=map(int,input().split())
l1.insert(pos,value)
print(l1)
kpos=int(input("enter kpos: "))
res=l1.kth_element(kpos)
print(res.val)

output:
Enter how many values you want: 8
Enter value1: 1
Enter value2: 2
Enter value3: 3
Enter value4: 4
Enter value5: 5
Enter value6: 6
Enter value7: 7
Enter value8: 8
Elements in linked list are:  1 2 3 4 5 6 7 8 

2 10
1 2 10 3 4 5 6 7 8 
enter kpos: 2
7