fname = input("Enter the file name : ")
f = open(fname,'r')
s = f.read()
f.close
print(s)
w = 0; c = 0; l = 0
l = s.count('\n')
w = s.count(' ')+1
c = len(s)-w+1

print("number of lines : ",l)
print("number of words : ",w)
print("number of chars : ",c)
y = input()
