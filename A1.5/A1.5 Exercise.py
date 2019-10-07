
import math
b=0
list = []
sortedlist = []
x = float(input("Enter a float: "))
list.append(x)
y = float(input("Enter a float: "))
list.append(y)
z = float(input("Enter a float: "))
list.append(z)

for i in range(len(list)):
    a = math.pow(list[i], 2)
    b = b + a
print(math.sqrt(b))

print("Type of the list -> ", type(list))
sortedlist = sorted(list)
print(sortedlist)

print("Sum of the lowest and highest -> ",sortedlist[0] + sortedlist[len(sortedlist)-1])
list.append(99.9)
print("The list -> ", list)