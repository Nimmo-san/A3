
import math

# Pythagorean Triplet
# Set of natural numbers a < b < c
# for which a^2 + b^2 = c^2
# There exists exactly one pythagorean triplet
# for which a + b + c = 1000.
# Find the product abc

# Largest prime that always divided abc is 60
# All prime factors of c are primes of the form 4n + 1, thus c is of the form 4n + 1
# The area k, ab/2 is a congruent number divisible by 6
# Can be encoded into a square matrix of the form
#
#     | c+b  a |
# X = | a  c-b |
# det X = c^2 - a^2 - b^2

def coprime(a, b):
    while b:
        # b != 0
        a, b = b, a % b
    return a == 1


divNums = []
pairsNum = []
numCoprimePairs = []
num = 18


def pythagorean_triples(n):
    a, b, c = 1, 3, 0
    while c < n:
        a_ = (a * b) + a
        c = math.sqrt(a_**2 + b**2)
        if c == int(c):
            yield b, a_, int(c)
        a += 1
        b += 2


# Dickson's Method

def factorpairs(n):
     for i in range(1, num+1):
        if n % i == 0:
             divNums.append(i)
     # divNums.append(num)


def main():
    for i in range(len(divNums)-len(divNums)/2):
        a = 0
        b = 0
        if num % divNums[i] == 0:
            a = divNums[i]
            b = num / a
            pairsNum.append(a)
            pairsNum.append(b)


def checkcoprime():
    for i in range(len(pairsNum)-1):
        if coprime(pairsNum[i], pairsNum[i+1]) == True:
            numCoprimePairs.append(pairsNum[i])
            numCoprimePairs.append(pairsNum[i+1])


def findtriples():
    x=0
    y=0
    z=0

    for i in range(len(numCoprimePairs)-1):
        s = numCoprimePairs[i]
        t = numCoprimePairs[i+1]
        r = int(math.pow(2 * num, 0.5))
        x = r + s
        y = r + t
        z = r + s + t
        print(int(math.pow(x, 2)),  " + ", int(math.pow(y, 2)), " = ", int(math.pow(z, 2)))


factorpairs(num)
main()
checkcoprime()
findtriples()
# print divNums
# print pairsNum
print numCoprimePairs



