fname = input("enter the file name : ")
f = open(fname,'r')
s = f.readlines()
lines = []
for line in s:
    line = line.replace('\n','')
    reverse = line[::-1]
    lines.append(reverse)

f.close()
for line in lines:
    print(line)

y = input()
