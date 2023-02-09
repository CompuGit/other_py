fname = input('Enter Filename : ')
f = open(fname,'r')

#sp = fname.split('.')
#index = sp[0]
#ext = sp[1]
#print("it is a ",ext," file.")

index = fname.index('.')
ext = fname[index + 1:]

if (ext == 'py'):
    print("it is a Python File")
elif (ext == 'c'):
    print("it is a C File")
elif (ext == 'txt'):
    print("it is a txt File")

s = f.read()
f.close()
dict = {}

for ch in s:
    dict[ch] = s.count(ch)

print(dict)

y = input()
