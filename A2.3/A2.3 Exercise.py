import matplotlib.pyplot as plot
import math


def draw_polygon(xc, yc, n, length):
    if n < 3 or length <= 0:
        exit(1)

    xp = []
    yp = []

    r = length * (1/(2*math.sin(math.pi/n)))

    for i in range(n+1):
        xi = xc + r*math.sin((2*math.pi/n) * i)
        yi = yc + r*math.cos((2*math.pi/n) * i)
        xp.append(xi)
        yp.append(yi)

    plot.plot(xp, yp, 'r')
    plot.show()


axis = [0, 400, 0, 400]
plot.axis('square')
plot.axis(axis)
plot.title('A2.3 Polygon')
plot.xlabel('x')
plot.ylabel('y')

draw_polygon(100, 100, 3, 100)
draw_polygon(200, 200, 5, 75)
draw_polygon(300, 300, 7, 50)
