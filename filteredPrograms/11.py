primearr = []
result = []
a = 0
b = 3
i = 0

 
for num in range(2,100):
   for i in range(2,num):
      if (num % i) == 0:
         break
   else:
      primearr.append(num)


while i<11:
    arr = primearr[a:b]
    result.append(arr[0] * arr[1] + arr[2])
    a,b = b,b+3
    i+=1

print(result)
