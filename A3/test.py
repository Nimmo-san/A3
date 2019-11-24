import matplotlib.pyplot as plt

from functions import makeList, correctFile, plotList, makeAverageList

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tropical']

data_file = '..\A3/textfiles\Data.nh.txt'
list_tuples = makeList(data_file)

# plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')
#
# plt.savefig('..\A3/images/test.png')

# plt.show()

fakedata = '..\A3/textfiles\FakeData.txt'
fakeoutput = '..\A3/textfiles/Here.txt'
correctFile(fakedata, fakeoutput)

# def removefile(file):
#     if os.path.exists(file):
#         os.remove(file)
#         return True
#     return False


for i in range(len(IO_monthly_files) - 1):
    delete = False
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
    # print("FILE: {} --> {}".format(input_file, success))

    # if delete:
    #     print("FILE: {} --> {}".format(output_file, removefile(output_file)))
    #     print('\n')

# list1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 4)
# list2 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 1, 12)
list3 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 4, 12)
# plotList("Data1", list1, 'mo', 'x', 'y')
# plotList("Data2", list2, 'ko', 'x', 'y')
plotList("Data3", list3, 'ro', 'x', 'y')
plt.show()



# lines = [line.rstrip('\n') for line in f]
# for line in lines:
#     print(line)
