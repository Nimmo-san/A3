# This file is not included with the assessed sheet of A2

# The following lines of codes are
# for the matter of debugging, it is not included
# with the actual code for this project
# It is for the development of the REPEAT function
#
all_func = []
repeat_func = []


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
            tuple_to = change(command, argument)
            repeat_func.append(tuple_to)

        if command != 'REPEAT':
            tuple_functions = change(command, argument)
            all_func.append(tuple_functions)

        # print(command, argument)
    # rep_list = repeat(repeat_func, found_repeat)
    # remove_items(all_func, found_repeat, len(repeat_func))
    # plot(rep_list, found_repeat)


# Might not be necessary
def plot(repeated, given_index):
    all_functions = merge_lists(repeated, all_func, given_index)
    # print(all_functions)
    for i in range(len(all_functions)):
        for j in range(len(all_functions[i])-1):
            command = all_functions[i][j]
            argument = all_functions[i][j+1]
            # print(command, argument)

            if command == 'FORWARD':
                print(command, argument)
            elif command == 'ROTATE':
                print(command, argument)
            elif command == 'PEN':
                print(command, argument)
            else:
                print("Error!")
    return None


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


def merge_lists(fromlist, tolist, index):

    # Checking if the length of the fromlist
    # is at least one
    # print(len(fromlist), fromlist)
    # print(len(tolist), tolist)
    # print(index)
    if len(fromlist) <= 0:
        return

    for i in range(index, len(tolist), len(fromlist)):
        for j in range(len(fromlist)-1, -1, -1):
            tolist.insert(i, fromlist[j])
    # Returning the new list after merging
    # the two lists
    return tolist

#
# def change_to_tuple(list):
#     list_tuple = []
#
#     # Going through the list to make
#     # a new tuple with the given values
#     # for each command and its corresponding argument
#     for i in range(1, int(1/2 * len(list))+1):
#         a = (list[2*(i-1)], list[2*i - 1])
#         list_tuple.append(a)
#     # Returning the list after adding
#     # the tuple to a new list
#     return list_tuple


main(init())

