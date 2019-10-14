import matplotlib.pyplot as plot


def draw(points, style='r-'):
    x = []
    y = []

    # Watch out for this one, wrong way of reading tuples
    for i in range(len(points)):
        for j in range(len(points[i])):
            if j == 0:
                x.append(points[i][j])
                # print(j)
            else:
                y.append(points[i][j])
                # print(j)

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

    for i in range(n):
        split = lines[i].split(',')
        x = split[0]
        y = split[1]
        tuple_numbers = (x, y)
        points.append(tuple_numbers)
    f.close()

    draw(points, 'b-')
    draw(points, 'ro')
    plot.show()


main()

