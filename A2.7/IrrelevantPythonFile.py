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

        print(command, argument)
    print(repeatfunc)


def repeat(state, list):
    # print("This is not working!")
    if isinstance(int(list[1]), int):
        for i in range(2, int(list[1])):
            print("command, argument ", list[i], list[i+1])
    else:
        return
    return state


main()
