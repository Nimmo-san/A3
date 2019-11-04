# A2.7
import math
import matplotlib.pyplot as plt

all_func = []
repeat_func = []
lines = []


def init():
    filename = '..\A2.7\test.txt'
    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]
    return lines


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
        plt.plot(xlist, ylist, 'r')
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


def main(lines):
    axis = [-400, 400, -400, 400]
    plt.axis('square')
    plt.axis(axis)
    plt.title('Name...')

    # pen = (x, y, state, angle)
    state_pen = (0, 0, False, 0)
    command = ''
    argument = ''
    split = []
    split2 = []
    found_repeat = 0
    found = False

    for i in range(len(lines)):
        try:
            split = lines[i].split(' ')
            split2 = split[1].split(' ')
        except:
            pass
        command = split[0]
        argument = split2[0]

        if command == 'REPEAT' and argument != 'END':
            found_repeat = i
            found = True

        if command == 'REPEAT' and argument == 'END':
            found = False

        if found and command != 'REPEAT':
            tuple_to = change(command, argument)
            repeat_func.append(tuple_to)

        if command != 'REPEAT':
            tuple_functions = change(command, argument)
            all_func.append(tuple_functions)

            # print(command, argument)
    rep_list = repeat(repeat_func, found_repeat)
    remove_items(all_func, found_repeat, len(repeat_func))
    state_pen = plot(rep_list, found_repeat, state_pen)


# Might not be necessary
def plot(repeated, given_index, state):
    all_functions = merge_lists(repeated, all_func, given_index)
    # print(all_functions)
    for i in range(len(all_functions)):
        for j in range(len(all_functions[i]) - 1):
            command = all_functions[i][j]
            argument = all_functions[i][j + 1]
            # print(command, argument)

            if command == 'FORWARD':
                state = forward(state, argument)
            elif command == 'ROTATE':
                state = rotate(state, argument)
            elif command == 'PEN':
                state = pen(state, argument)
            else:
                print("Error!")
    plt.show()
    return state


def remove_items(list1, index, elements):
    # print(list1)
    if len(list1) <= 0:
        return

    end_index = index + elements
    del list1[index:end_index]

    return list1


def change(command, argument):
    tuple_of = (command, argument)
    return tuple_of


def repeat(list_to_repeated, argument):
    repeated_func = []

    # Checking if list to be repeated
    # is empty or not
    if len(list_to_repeated, ) <= 0:
        return

    for i in range(int(argument)):
        for j in range(len(list_to_repeated, )):
            a = list_to_repeated[j]
            repeated_func.append(a)
    # Returning the new list after
    # the elements in the list are repeated
    # a certain number of times
    return repeated_func


def merge_lists(fromlist, tolist, index):
    # Checking if the length of the fromlist
    # is at least one
    # print(len(fromlist), fromlist)
    # print(len(tolist), tolist)
    # print(index)
    if len(fromlist) <= 0:
        return

    for i in range(index, len(tolist), len(fromlist)):
        for j in range(len(fromlist) - 1, -1, -1):
            tolist.insert(i, fromlist[j])
    # Returning the new list after merging
    # the two lists
    return tolist


def test_forward(state, argument):
    # Forward function test
    print(forward(state, argument))


def test_rotate(state, argument):
    # Rotate function test
    print(rotate(state, argument))


def test_pen(state, argument):
    # Pen function test
    print(pen(state, argument))


lines = init()
main(lines)
