import math
import csv

# Euler Problems
# Producing a prime number

num = 13195
primes = []
# f(n) = [(n! mod (n+1))/n](n-1)+2


def prime(n):
    a = math.factorial(n) % (n+1)
    b = a / n
    c = (b * (n-1)) + 2
    return c


def main():
    for i in range(20):
        a = 0
        if i == 0:
            a = prime(i+1)
            primes.append(a)
        else:
            a = prime(i)
            primes.append(a)
    clear()


def clear():
    for i in range(len(primes)-1):
        if primes[i+1] == 2:
            primes.remove(primes[i])


main()
print(primes)
