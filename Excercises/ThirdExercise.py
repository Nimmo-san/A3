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

# Euclid's Method
# Try as long as  m>n
#     a = m^2-n^2
#     b = 2mn
#     c = m^2+c^2
# Dickinson's method #
# Try again later #

def coprime(a, b):
    while b:
        # b != 0
        a, b = b, a % b
    return a == 1
    
    
nums = []
a=0
b=0
c=0
s = 1000
m=0
k=0
n=0
d=0
mlimit = int(math.sqrt(s/2))
found = False
for m in range(2, mlimit):
    if (s / 2) % m == 0:
        if m % 2 == 0:
            k = m + 1
        else:
            k = m + 2

        while k<2*m and k<=s/(2*m):
            if (s/(2*m)) % k == 0 and coprime(k,m) == True:
                d = s/2/(k*m)
                n=k-m
                a = d*(math.pow(m,2) - math.pow(n,2))
                b=2*d*n*m
                c = d*(math.pow(m,2)+math.pow(n,2))
                nums.append(int(a))
                nums.append(int(b))
                nums.append(int(c))
                found = True
                break
            k = k+2
    if found:
        break


print (nums)
print (nums[0]*nums[1]*nums[2])
    



