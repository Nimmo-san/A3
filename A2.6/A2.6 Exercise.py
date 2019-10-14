import matplotlib.pyplot as plot


def draw(points, style='r-'):
    x = []
    y = []

    for i in range(len(points)):
        for j in range(len(points[i]) - 1):
            x.append(points[i][j])
            y.append((points[i][j + 1]))

    plot.plot(x, y, style)


def main():
    axis = [0, 400, 0, 400]
    plot.axis('square')
    plot.axis(axis)
    plot.title('A2.6: Reading Points')

    plot.xlabel('x')
    plot.ylabel('y')

    filename = input()
    with open(filename, 'r') as f:
        n = int(f.readline(1))

    points = []

    for i in range(2, n, 1):
        line = f.readline(i)
        splitline = line.split(',')
        x = float(splitline[0])
        y = float(splitline[1])
        a = (x, y)
        points.append(a)
    f.close()

    draw(points, 'b-')
    draw(points, 'ro')
    plot.show()


main()