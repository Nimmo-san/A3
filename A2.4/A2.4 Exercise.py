
import matplotlib.pyplot as plot
import math

points = []
xc = 200
yc = 200
length = 300
n = 3
r = length * (1/(2*math.sin(math.pi/n)))


def drawPoints(points):
    x = []
    y = []

    for i in range(len(points)):
        for j in range(len(points[i])-1):
            x.append(points[i][j])
            y.append((points[i][j+1]))

    plot.plot(x, y, 'b')
    plot.plot(x, y, 'ro')
    plot.show()


axis = [0, 400, 0, 400]
plot.axis('square')
plot.axis(axis)
plot.title('A2.4: Points')

plot.xlabel('x')
plot.ylabel('y')

# Do the calculation explicitly, later !!!!!!
for i in range(n+1):
        xi = xc + r*math.sin((2*math.pi/n) * i)
        yi = yc + r*math.cos((2*math.pi/n) * i)
        a = (xi, yi)
        points.append(a)
# !!!!!
drawPoints(points)

