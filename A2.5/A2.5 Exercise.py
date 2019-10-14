import matplotlib.pyplot as plot
import math

list_p = []
def polygon(xc , yc, nsides, length, angle):

    r = length * (1 / (2 * math.sin(math.pi / nsides)))
    listofpoints = []

    for i in range(nsides + 1):

        xi = xc + r * math.sin(((2 * math.pi / nsides) * i) + math.radians(angle))
        yi = yc + r * math.cos(((2 * math.pi / nsides) * i) + math.radians(angle))
        a = (xi, yi)
        listofpoints.append(a)

    return listofpoints


xc = float(input())
yc = float(input())
nsides = int(input())

if nsides < 2:
    exit(1)

length = float(input())
if length < 0:
    exit(1)

angle = float(input())

list_p = polygon(xc, yc, nsides, length, angle)

f = open('G:\Documents\points.txt', 'w')
f.write(str(len(list_p)))
f.write("\n")

for i in range(len(list_p)):
    for j in range(len(list_p[i])-1):
        px = round(list_p[i][j], 2)
        py = round(list_p[i][j], 2)
        f.write(str(px) + str(",") + str(py) + "\n")
f.close()




