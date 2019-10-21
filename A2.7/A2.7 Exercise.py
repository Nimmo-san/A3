# A2.7
import matplotlib.pyplot as plot
import math


x1 = [0, 0]
y1 = [-400, 400]
x2 = [-400, 400]
y2 = [0, 0]


def forward(state, distance):
    print(state, distance)
    x1 = state[0] + (int(distance) * math.cos(math.radians(state[len(state) - 1])))
    y1 = state[1] + (int(distance) * math.sin(math.radians(state[len(state) - 1])))
    # Returns if the state of the pen is up
    if state[2] == False or state[2] == 0:
        return change_state(state, x1, y1)
    # Moves in the direction its facing if state of pen is down
    elif state[2] == True or state[2] == 1:
        xlist = [state[0], x1]
        ylist = [state[1], y1]
        plot.plot(xlist, ylist, 'r')
        newstate = change_state(state, x1, y1)
        return newstate


def rotate(state, angle):
    print(state, angle)
    if int(angle) < -360:
        print("Error!")
        exit(1)
    else:
        list1 = list(state)
        list1[len(list1)-1] = int(angle) + list1[len(list1)-1]
        state = tuple(list1)
        return state


def pen(state, value):
    print(state, value)
    if value == 'down':
        list1 = list(state)
        list1[2] = True
        state = tuple(list1)
        return state
    elif value == 'up':
        list1 = list(state)
        list1[2] = False
        state = tuple(list1)
        return state
    else:
        print("Error! Pen")


def change_state(state, x1, y1):
    # print(x1, y1)
    list1 = list(state)
    list1[0] = x1
    list1[1] = y1
    # print(tuple(list1))
    return tuple(list1)


def main():
    filename = input()
    command = ''
    argument = ''

    axis = [-400, 400, -400, 400]
    plot.axis('square')
    plot.axis(axis)
    plot.title('Name...')
    plot.plot(x2, y2, 'k:')
    plot.plot(x1, y1, 'k:')

    # pen = (x, y, state, angle)
    state_pen = (0, 0, False, 0)

    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]
    # print(lines)
    for i in range(len(lines)):
        split = lines[i].split('<')
        split2 = split[1].split('>')
        command = split[0]
        argument = split2[0]
        print(command, argument)
        # Testing each of the functions
        # using three different test functions
        if command == 'FORWARD':
            test_forward(state_pen, argument)
            # state_pen = forward(state_pen, argument)
            # print(penstate)
        elif command == 'ROTATE':
            test_rotate(state_pen, argument)
            # state_pen = rotate(state_pen, argument)
        elif command == 'PEN':
            test_pen(state_pen, argument)
            # state_pen = pen(state_pen, argument)
        else:
            print("Error!")
    plot.show()


def test_forward(state, argument):
    # Forward function test
    print(forward(state, argument))


def test_rotate(state, argument):
    # Rotate function test
    print(rotate(state, argument))


def test_pen(state, argumeent):
    # Pen function test
    print(pen(state, argumeent))

main()
