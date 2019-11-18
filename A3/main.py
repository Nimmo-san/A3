import matplotlib.pyplot as plt

from functions import plotList, makeList, correctFile, makeAverageList

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tropical']

# File data
file_data = '..\A3/textfiles\Data.nh.txt'
# Changes into a list of tuples
tuples_list = makeList(file_data)

# Plot list plots after the data is split into two new lists
# plotList(name='Northern hemisphere', color='slateblue',
#          list_tuples=tuples_list, xaxis='year', yaxis='temprature anomalies')
# Saves the graph
plt.savefig('..\A3/images/A3part1.png')
# Then shows the graph
# plt.show()


for i in range(len(IO_monthly_files) - 1):
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

months = 48
list1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)
list2 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)
list3 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)
list4 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)
print(list1, list2, list3, list4)
plotList('Average Data: {:2.2f} years'.format(months / 12), list1, 'mo', 'YEAR', 'TEMP')
plotList('Average Data: {:2.2f} years'.format(months / 12), list2, 'mo', 'YEAR', 'TEMP')
plotList('Average Data: {:2.2f} years'.format(months / 12), list3, 'mo', 'YEAR', 'TEMP')
plotList('Average Data: {:2.2f} years'.format(months / 12), list4, 'mo', 'YEAR', 'TEMP')
plt.show()
plt.savefig('..\A3/images/A3part1.png')
