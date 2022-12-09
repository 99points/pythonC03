# 3.4 The factorial of a nonnegative integer n is written n! (pronounced “n factorial”)
# and is defined as follows:
# n!=n·(n-1)·(n-2)·...·1 (forvaluesofngreaterthanorequalto1) and n!=1 (forn=0).
# For example, 5! = 5 · 4 · 3 · 2 · 1, which is 120.
# Factorials increase in size very rapidly.
# What is the largest factorial that your
# program can calculate before leading to an overflow error?

import sys
factorial = 2
temp = factorial
while (True):

    if (factorial < 0 or factorial > sys.maxsize):
        break;

    temp = temp+1
    factorial = factorial*temp
    print(factorial)

print("\n")
print(temp-1)
