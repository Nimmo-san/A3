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


def is_prime(n):
    if n==1:
        return False;

    if n>2 and n % 2 ==0:
        return False;

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_divisor, 2):
        if n % i == 0:
            return False;
    return True;


def main():
    for i in range(1,1000):
        print(i, is_prime(i));
