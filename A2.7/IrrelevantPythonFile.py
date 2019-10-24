# This file is not included with the assessed sheet of A2

# The following lines of codes are
# for the matter of debugging, it is not included
# with the actual code for this project
# It is for the development of the REPEAT function

list_repeat = []
repeatfunc = []

def main():
    command = ''
    argument = ''
    split = []
    split2 = []
    wrong = False
    found = False
    state_pen = (0, 0, False, 0)
    filename = 'G:\Documents\Faketest.txt'
    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]

    for i in range(len(lines)):
        try:
            split = lines[i].split('<')
            split2 = split[1].split('>')
        except:
            wrong = True


        if wrong:
            split = lines[i].split(' ')
            split2 = split[1].split(' ')
            wrong = False
        command = split[0]
        argument = split2[0]

        if command == 'REPEAT' and argument != 'END':
            found = True

        if command == 'REPEAT' and argument == 'END':
            found = False

        if found:
            repeatfunc.append(command)
            repeatfunc.append(argument)

        if command == 'FORWARD':
            state_pen = forward(state_pen, argument)
        elif command == 'ROTATE':
            state_pen = rotate(state_pen, argument)
        elif command == 'PEN':
            state_pen = pen(state_pen, argument)

        else:
            print("Error!")
        # print(command, argument)
    # print(repeatfunc)


def pen(state, argument):
    print(state, argument)
    return state


def rotate(state, argument):
    print(state, argument)
    return state


def forward(state, argument):
    print(state, argument)
    return state


def repeat(state, argument):
    print("Argument: ", argument)
    for i in range(1, int(argument)):
        command = repeatfunc[i]
        if command == 'FORWARD':
            state = forward(state, repeatfunc[i+1])
        elif command == 'ROTATE':
            state = rotate(state, repeatfunc[i+1])
        elif command == 'PEN':
            state = pen(state, repeatfunc[i+1])
        else:
            print("Error!")
    return state


main()
