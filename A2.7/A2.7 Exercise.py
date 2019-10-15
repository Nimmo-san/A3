# A2.7
import matplotlib.pyplot as plot
import math


def forward(state, distance):
    print(state, distance)
    # Returns if the state of the pen is up
    if state[2] == False or state[2] == 0:
        return state
    # Moves in the direction its facing if state of pen is down
    elif state[2] == True or state[2] == 1:
        x1 = state[0] + (int(distance) * math.cos(math.radians(state[len(state)-1])))
        y1 = state[1] + (int(distance) * math.sin(math.radians(state[len(state)-1])))
        xlist = [state[0], x1]
        ylist = [state[1], y1]
        plot.plot(xlist, ylist, 'r')
        return change_state(state, x1, y1)


def rotate(state, angle):
    print(state, angle)
    if int(angle) < 0:
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
    list1 = list(state)
    list1[0] = x1
    list1[1] = y1
    return tuple(list1)


def main():
    filename = input()
    command = ''
    argument = ''
    axis = [-400, 400, -400, 400]
    plot.axis('square')
    plot.axis(axis)
    plot.title('Name...')

    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]
    # print(lines)
    for i in range(len(lines)):
        split = lines[i].split('<')
        split2 = split[1].split('>')
        command = split[0]
        argument = split2[0]
        # test(command, argument)
        print(command, argument)
        if command == 'FORWARD':
            penstate = forward(penstate, argument)
        elif command == 'ROTATE':
            penstate = rotate(penstate, argument)
        elif command == 'PEN':
            penstate = pen(penstate, argument)
        else:
            print("Error!")
    plot.show()


def test(command, argument):
    penstate = (0, 10, True, 10)

    if command == 'PEN':
        print(pen(penstate, argument))
    # elif command == 'ROTATE':
    #     print(rotate(penstate, argument))
    # elif command == 'FORWARD':
    #     print(forward(penstate, argument))
    else:
        print("Error, no function found!")

main()
# pen = (x, y, state, angle)
penstate = (0, 0, False, 45)
