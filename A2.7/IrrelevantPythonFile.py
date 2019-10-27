# This file is not included with the assessed sheet of A2

# The following lines of codes are
# for the matter of debugging, it is not included
# with the actual code for this project
# It is for the development of the REPEAT function
#
all_func = []
repeatfunc = []

def main():
    command = ''
    argument = ''
    split = []
    split2 = []
    rep_list = []
    found_repeat = 0
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
            found_repeat = i
            found = True

        if command == 'REPEAT' and argument == 'END':
            found = False

        if found and command != 'REPEAT':
            repeatfunc.append(command)
            repeatfunc.append(argument)

        if command != 'REPEAT' and argument != 'END':
            all_func.append(command)
            all_func.append(argument)

        change_to_tuple(repeatfunc)
        change_to_tuple(all_func)

        # print(command, argument)
    print(repeatfunc)
    print(all_func)
    print(merge_lists(rep_list, all_func, found_repeat))


def repeat(list1, argument):
    repeatfunc = []
    if len(list1) <= 0:
        return
    for i in range(int(argument) * len(list1)):
        for j in range(len(list1)):
            a = list1[j]
            repeatfunc.append(a)
    print(len(list1))
    return repeatfunc


def change_to_tuple(list1):
    list_tuple = []
    for i in range(1, int(1/2 * len(list1))+1):
        a = (list1[2*(i-1)], list1[2*i - 1])
        list_tuple.append(a)
    return list_tuple


def merge_lists(fromlist, tolist, index):
    if len(fromlist) <= 0:
        return
    for i in range(index, len(tolist)):
        for j in range(len(fromlist)-1, -1, -1):
            tolist.insert(i, fromlist[j])
    return tolist


main()