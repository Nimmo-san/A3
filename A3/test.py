import matplotlib.pyplot as plt

from classes import Analysis
from functions import makeList, plotList, correctFile, makeAverageList, plotWithError

# Constant variables to be used globally
parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tr']
test_data = '..\A3/textfiles\FakeData.txt'
test_output = '..\A3/textfiles/Here.txt'
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'

# The test data to be plotted
data_file = '..\A3/textfiles\Data.nh.txt'
list_tuples = makeList(data_file)

plotList('DEAD!', list_tuples, 'r', 'DEAD I', 'DEAD II')
# The figure is saved and displayed
plt.savefig('..\A3/images/test.png')
plt.show()

print(correctFile(test_data, test_output))

# Iterates through the files stored
# and aplies the correctFile function
n = len(IO_monthly_files)
for i in range(n - 1):

    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > n or output_file_index > n:
        break

        # print("File, I:O -> {}:{}".format(IO_monthly_files[input_file_index],
        # IO_monthly_files[output_file_index]))
    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'

    # print("INPUT:OUTPUT -->> {}:{}".format(input_file, output_file))
    success = correctFile(input_file, output_file)

# makeAverageList function invoked to find the averages of the nh data over a
# different period of columns and they are plotted
list1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, 4)
list2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 8, 4)
list3 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 9, 4)
plotList('C1', list1, 'm', 'x', 'y')
plotList('C8', list2, 'k', 'x', 'y')
plotList('C9', list3, 'r', 'x', 'y')
plt.show()
# plotWithError invoked to plot an error
# Displays the plot
plotWithError('', 'uncertainty', list1, list2, list3, 'k', 'r', 'x', 'y')
plt.show()

# An instance of a class
ana = Analysis()

# Iterates through it and adds the output function to the input file
for i in range(n - 1):
    output_file_index = 2 * i - 1
    if output_file_index < 0:
        continue
    if output_file_index > n:
        break
    # Invokes the addFile and updateLists function for each input file
    ana.addFile(parent_path + monthly_output + IO_monthly_files[output_file_index],
                IO_monthly_files[output_file_index][-2:])
    ana.updateLists((0, 2, 4, 6, 8, 10), 12, 'nhu', 'nhu2', 1, 6)

# Prints the corresponding input file and its title
ana.printLists()
