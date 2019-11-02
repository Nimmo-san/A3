
# This file is not included with the assessed sheet A2.7, its sole purpose is for testing
list_of_commands = []


def main():
    filename = 'G:\Documents\Faketest.txt'
    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]

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
        list_of_commands.append(command)
        list_of_commands.append(argument)

    print(list_of_commands)
    print(len(list_of_commands))
    for j in range(len(list_of_commands)):

        index_a = 2*(j - 1)
        index_b = (2 * j) - 1
        if index_a < 0 and index_b < 0:
            continue
        if index_a > 24 or index_b > 24:
            break

        value_c = list_of_commands[index_a]
        value_a = list_of_commands[index_b]

        print(index_a, value_c, index_b, value_a)

#
# for j in range(len(func)):
#
#     index_a = 2 * (j - 1)
#     index_b = (2 * j) - 1
#     if index_a < 0 and index_b < 0:
#         continue
#     if index_a > len(func) or index_b > len(func):
#         break
#
#     value1 = func[index_a]
#     value2 = func[index_b]
#
#     if value1 == 'REPEAT' and value2 != 'END':
#         found = True
#
#     if found:
#         value = (value1, value2)
#         emptylist.append(value)
#
#     if value1 == 'REPEAT' and value2 == 'END':
#         found = False

main()
