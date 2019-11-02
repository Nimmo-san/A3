
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

        # try:
        #     split = lines[i].split('<')
        #     split2 = split[1].split('>')
        # except:
        #     wrong = True
        #
        # if wrong:
        #     split = lines[i].split(' ')
        #     split2 = split[1].split(' ')
        #     wrong = False
        try:
            split = lines[i].split(' ')
            split2 = split[1].split(' ')
        except:
            pass
        tuple1 = (split[0], split2[0])
        list_of_commands.append(tuple1)

    print(list_of_commands)


main()
