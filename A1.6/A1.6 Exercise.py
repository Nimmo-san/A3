
list = []
secondList = ['X', 'Y', 'Z']
thirdList = []
# b=0
# a=0
n = int(input("Enter an integer: "))
print("Enter Floating numbers: ")
for i in range(n):
    x = float(input())
    list.append(x)


print(list)
print(sorted(list, reverse=True))

print("-------------------------------------")
for i in range(len(list)):
    print(list[i])
    #print("\n")

print("-------------------------------------")
for i in range(len(list)):
    a = list[i]
    if a < 5:
        print("{} < 5".format(a))
    elif a > 5:
        print("{} > 5".format(a))
    else:
        print("{} = 5".format(a))
    #print("\n")
print("-------------------------------------")


for i in range(3*n):
    for j in range(len(list)):
        for z in range(len(secondList)):
            new_tuple = (list[j], secondList[z])
            thirdList.append(new_tuple)

print(thirdList)
