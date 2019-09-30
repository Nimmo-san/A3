# Fibonacci sequence

# Version two took too long to calculate huge numbers,
# will use cache to store values that has been calculated before
previousterms = {}
digits = []

def fib(n):
    if n in previousterms:
        return previousterms[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fib(n-1)+fib(n-2)

    previousterms[n] = value
    return value


for i in range(1, 1001):
    num = fib(i)
    print(num, "\n")
    count = 0
    while num > 0:
        num = num//10
        count = count + 1


print(digits)
