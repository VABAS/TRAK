import sys
from fractions import Fraction

def fibo(n):
    if n < 0:
        print "Unsuitable number for function fibo()"
        sys.exit(1)
    elif n == 0 or n == 1:
        return 1
    else:
        return fibo(n - 2) + fibo(n - 1)

def luku(n):
    return fibo(n - 1) / float(fibo(n))

#print luku(0) # Mahdoton
print Fraction(luku(3)).limit_denominator()
print Fraction(luku(5)).limit_denominator()
