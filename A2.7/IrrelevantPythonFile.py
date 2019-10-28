# This file is not included with the assessed sheet of A2

# The following lines of codes are
# for the matter of debugging, it is not included
# with the actual code for this project
# It is for the development of the REPEAT function
#
all_func = []
repeat_func = []
rep_list = []


def init():
    filename = 'G:\Documents\Faketest.txt'
    f = open(filename, 'r')
    lines = [line.rstrip('\n') for line in f]
    return lines


def main(lines):
    command = ''
    argument = ''
    split = []
    split2 = []
    found_repeat = 0
    wrong = False
    found = False

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
            found_repeat = i
            found = True

        if command == 'REPEAT' and argument == 'END':
            found = False

        if found and command != 'REPEAT':

            repeat_func.append(command)
            repeat_func.append(argument)

        if argument != 'END':
            all_func.append(command)
            all_func.append(argument)

        # print(command, argument)
    print(change_to_tuple(repeat_func))
    print(change_to_tuple(all_func))
    print(merge_lists(rep_list, all_func, found_repeat))


# Might not be necessary
# def plot():
#
#     for i in range(1, len(all_func)+1):
#         command = all_func[2*(i-1)]
#         argument = all_func[2*i - 1]
#
#         # if command == 'REPEAT':
#         #     print(command, argument)
#         # elif command == 'FORWARD':
#         #     print(command, argument)
#         # elif command ==
#     return None


def repeat(list_to_repeated, argument):
    repeated_func = []

    # Checking if list to be repeated
    # is empty or not
    if len(list_to_repeated,) <= 0:
        return

    for i in range(int(argument)):
        for j in range(len(list_to_repeated,)):
            a = list_to_repeated[j]
            repeated_func.append(a)
    # Returning the new list after
    # the elements in the list are repeated
    # a certain number of times
    return repeated_func


def change_to_tuple(list):
    list_tuple = []

    # Going through the list to make
    # a new tuple with the given values
    # for each command and its corresponding argument
    for i in range(1, int(1/2 * len(list))+1):
        a = (list[2*(i-1)], list[2*i - 1])
        list_tuple.append(a)
    # Returning the list after adding
    # the tuple to a new list
    return list_tuple


def merge_lists(fromlist, tolist, index):

    # Checking if the length of the fromlist
    # is at least one
    if len(fromlist) <= 0:
        return

    for i in range(index, len(tolist), len(fromlist)):
        for j in range(len(fromlist)-1, -1, -1):
            tolist.insert(i, fromlist[j])
    # Returning the new list after merging
    # the two lists
    return tolist


main(init())

