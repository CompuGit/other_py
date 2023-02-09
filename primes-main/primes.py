class Primes:

    def __init__(self, n=2, m=20):
        self.n = n-1
        self.range = n,m
        self._list = []
        while n<=m:
            if (x:=next(self._gen()))<=m: self._list.append(x)
            n += 1

        

    def __repr__(self) -> str:
        return f'Primes{self.range}  object at id<{hex(id(self))}>'

    def __iter__(self):
        return iter(self._list)
    
    def __len__(self):
        return len(self._list)

    def _gen(self):
        while True:
            self.n+=1
            if self.isprime(self.n): yield self.n

    def isprime(self, n:int ) -> bool:
        if (n <= 1): return False
        elif (n == 2): return True
        elif (n % 2 == 0): return False
        else:
            i = 3
            while i <= n**(1/2):
                if n % i == 0: return False
                i += 2
            return True
        
'''
class Primes:

    def __init__(self, n=2, m=20):
        self.n = n-1
        self.m = m

    def __repr__(self) -> str:
        return f'Primes{self.n+1, self.m}  object at id<{hex(id(self))}>'

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n>self.m:
            raise StopIteration
        #if self.isprime(self.n):
        self.n+=1
        return self.n if self.isprime(self.n) else self.__next__()
            
    def isprime(self, n:int ) -> bool:
        if (n <= 1): return False
        elif (n == 2): return True
        elif (n % 2 == 0): return False
        else:
            i = 3
            while i <= n**(1/2):
                if n % i == 0: return False
                i += 2
            return True
'''
