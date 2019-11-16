import os

import matplotlib.pyplot as plt

from functions import makeList, plotList, correctFile, makeAverageList

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tropical']

data_file = '..\A3/textfiles\Data.nh.txt'
list_tuples = makeList(data_file)

plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')

plt.savefig('..\A3/images/test.png')

# plt.show()

fakedata = '..\A3/textfiles\FakeData.txt'
fakeoutput = '..\A3/textfiles/Here.txt'
correctFile(fakedata, fakeoutput)


def removefile(file):
    if os.path.exists(file):
        os.remove(file)
        return True
    return False


for i in range(len(IO_monthly_files) - 1):
    delete = True
    monthly_input = '\Data.monthly'
    monthly_output = '/Parsed.monthly'

    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > len(IO_monthly_files) or output_file_index > len(IO_monthly_files):
        break

        # print("File, I:O -> {}:{}".format(IO_monthly_files[input_file_index],
        # IO_monthly_files[output_file_index]))
    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'

    # print("INPUT:OUTPUT -->> {}:{}".format(input_file, output_file))
    success = correctFile(input_file, output_file)
    print("FILE: {} --> {}".format(input_file, success))

    if delete:
        print("FILE: {} --> {}".format(output_file, removefile(output_file)))
        print('\n')

makeAverageList(parent_path + '\Here.txt', 0, 0, 0)


# lines = [line.rstrip('\n') for line in f]
# for line in lines:
#     print(line)
