import matplotlib.pyplot as plot


def draw(points, style='r-'):
    x = []
    y = []

    # Watch out for this one, wrong way of reading tuples
    for i in range(len(points)):
        for j in range(len(points[i])):
            if j == 0: x.append(points[i][j])
            else: y.append(points[i][j])

    plot.plot(x, y, style)


def main():
    axis = [0, 400, 0, 400]
    plot.axis('square')
    plot.axis(axis)
    plot.title('A2.6: Reading Points')

    plot.xlabel('x')
    plot.ylabel('y')

    filename = input()
    f = open(filename, 'r')
    n = int(f.readline())

    points = []

    lines = [line.rstrip('\n') for line in f]

    for i in range(len(lines)):
        linesplit = lines[0].split(',')
        x = linesplit[0]
        y = linesplit[1]
        a = (x, y)
        points.append(a)
    f.close()

    print(points)

    draw(points, 'b-')
    draw(points, 'ro')
    plot.show()

main()
