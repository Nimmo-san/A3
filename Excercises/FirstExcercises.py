import math
import csv

# f(n) = [(n! mod (n+1))/n](n-1)+2
# def prime(n):
#     a = math.factorial(n) % (n+1)
#     b = a / n
#     c = (b * (n-1)) + 2
#     return c

# Euler Problems
# Producing a prime number

num = 600851475143
primes = []
foundprimes = []


def is_prime(n):
    if n == 1:
        return False

    if n > 2 and n % 2 == 0:
        return False

    max_divisor = int(math.floor(math.pow(n,0.5)))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


def main():
    for n in range(1, 1000000):
        if is_prime(n) == True:
            primes.append(n)


def findlpf(n):
    for i in range(len(primes)):
        if n % primes[i] == 0:
            foundprimes.append(primes[i])


def findhpf(list):
    return list[len(list)-1]


main()
# print(primes)
findlpf(num);
print(foundprimes)
print("Highest Prime Factor of {} : ".format(num), findhpf(foundprimes))
