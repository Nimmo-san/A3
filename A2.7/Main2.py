
# This file is not included with the assessed sheet A2.7, its sole purpose is for testing
list_of_commands = []


def init():
    filename = 'G:\Documents\Faketest.txt'
    f = open(filename, 'r')
    lines1 = [line.rstrip('\n') for line in f]
    return lines1


def main(lines):

    command_repeat = []
    repeat_index = []
    list1= []
    repeat_index1 = []
    found = False
    command = ''
    argument = ''

    for i in range(len(lines)):
        # print(lines[i])
        try:
            split = lines[i].split(' ')
            split2 = split[1].split(' ')
        except:
            pass

        command = split[0]
        argument = split2[0]
        list_of_commands.append((command, argument))

    for j in range(len(list_of_commands)):
        for k in range(len(list_of_commands[i])-1):
            value_c = list_of_commands[j][k]
            value_a = list_of_commands[j][k+1]

            if value_c == 'REPEAT' and value_a != 'END':
                repeat_index.append(j)
                found = True

            if found:
                command_repeat.append((value_c, value_a))

            if value_c == 'REPEAT' and value_a == 'END':
                repeat_index.append(j)
                found = False

    for i in range(len(command_repeat)):
        for j in range(len(command_repeat[i])):
            value_c = command_repeat[i][j]

            if value_c == 'REPEAT':
                repeat_index1.append(i)
    for i in range(len(command_repeat)):
        for j in range(len(command_repeat[i])-1):
            value_c = command_repeat[i][j]
            value_a = command_repeat[i][j+1]
            start = False
            list12 = []
            if value_c == 'REPEAT' and value_a != 'END':
                start = True

            if start:
                list12 = [value_c, value_a]

            if value_c == 'REPEAT' and value_a == 'END':
                start = False
        list1.append(list12)

    print(list_of_commands)
    print(command_repeat)
    print(repeat_index)
    print(repeat_index1)
    print(list1)


lines2 = init()
main(lines2)

# index_a = 2*(j - 1)
# index_b = (2 * j) - 1
# if index_a < 0 and index_b < 0:
#     continue
# if index_a > 24 or index_b > 24:
#     break
#
# value_c = list_of_commands[index_a]
# value_a = list_of_commands[index_b]

# print(index_a, value_c, index_b, value_a)
# if value_c == 'REPEAT' and value_a != 'END':
#     repeat_index.append(j)
#     found = True
#
# if found:
#     command_repeat.append((value_c, value_a))
#
# if value_c == 'REPEAT' and value_a == 'END':
#     repeat_index.append(j)
#     found = False
