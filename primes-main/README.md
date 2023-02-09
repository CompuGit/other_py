# primes

this module helps us to generate list of primes in a given range.

default range is 2 to 20.

return object is iterable, has length, can be converted to list/tuple/set


# installation
pip install git+https://github.com/CompuGit/primes.git


# example
import primes

p = primes.Primes(1000,10010)

print(p)

print(len(p))

print(list(p))
