
import matplotlib.pyplot as plot

length = float(input())
radius = int((length/2))

if length < 0 or length > 400:
    print("error!")
    exit(1)

axis = [0, 400, 0, 400]

plot.axis('square')
plot.axis(axis)

plot.title('A2.2 Length')
plot.xlabel('x')
plot.ylabel('y')

plot.plot(200, 200, 'o')
x = [200+radius, 200+radius, 200-radius, 200-radius, 200+radius]
y = [200+radius, 200-radius, 200-radius, 200+radius, 200+radius]
plot.plot(x, y, 'b')


plot.show()


