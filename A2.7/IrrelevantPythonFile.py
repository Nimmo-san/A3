# This file is not included with the assessed sheet of A2

# The following lines of codes are
# for the matter of debugging, it is not included
# with the actual code for this project
# It is for the development of the REPEAT function

list_repeat = []


def main():
    command = ''
    argument = ''
    filename = 'G:\Documents\Faketest.txt'
    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]

    for i in range(len(lines)):
        try:
            split = lines[i].split('<')

            if split[0] == 'REPEAT':
                while not 'REPEAT':
                    list_repeat.append(split[0], split[1])

        except ValueError:
            print("Cant split!")

        print(command, argument)
        print(list_repeat)


main()
