import math
b=0
list = []
sortedlist = []
x = float(input())
list.append(x)
y = float(input())
list.append(y)
z = float(input())
list.append(z)

for i in range(len(list)):
    a = math.pow(list[i], 2)
    b = b + a
print(math.sqrt(b))

print(type(list))
sortedlist = sorted(list)
print(sortedlist)

print(sortedlist[0] + sortedlist[len(sortedlist)-1])
list.append(99.9)
print(list)