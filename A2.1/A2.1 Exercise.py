import matplotlib.pyplot as plot
import math

axis = [0, 400, 0, 400]

plot.axis('square')
plot.axis(axis)


plot.title('A2.1 Square')
plot.xlabel('x')
plot.ylabel('y')


plot.plot(200, 200, 'k+')
x = [350, 350, 50, 50, 350]
y = [350, 50, 50, 350, 350]
plot.plot(x, y, 'b')

x = [100, 300, 300, 100, 100]
y = [300, 300, 100, 100, 300]
plot.plot(x, y, 'r')
plot.show()



