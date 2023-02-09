n = 2000000
total,primes = 0, [True]*n


for p in range(2,n):
    if primes[p]:
        total += p
          
        for i in range(p*p,n,p):
            primes[i] = False

print(total)
