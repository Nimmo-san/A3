
import math
# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.


divisors = []
list = []
primeList = []
sum = 0
n = 100000000
x = 1000000000
# n = 30
# x = 100


def primeFunc(a):
    b = 0
    for c in range(2, int(a//2+1)):
        if a % c == 0:
            b = b + 1
    if b <= 0:
        return True
    else:
        return False


for i in range(1, x, 1):
    if n % i == 0:
        divisors.append(i)

for i in range(len(divisors)):
    a = divisors[i] + (n/divisors[i])
    if primeFunc(a):
        primeList.append(int(a))


for i in range(len(primeList)):
    sum = sum + primeList[i]

print(sum)