from fractions import Fraction

def reku(n):
    if n == 0:
        return 1

    else:
        return 1 / float(1 + reku(n - 1))

print Fraction(reku(0)).limit_denominator()
print Fraction(reku(1)).limit_denominator()
print Fraction(reku(2)).limit_denominator()
print Fraction(reku(3)).limit_denominator()
print Fraction(reku(4)).limit_denominator()
print Fraction(reku(5)).limit_denominator()
