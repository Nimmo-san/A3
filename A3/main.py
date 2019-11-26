import matplotlib.pyplot as plt

from functions import plotList, makeList, correctFile, makeAverageList

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh', '_out.nh', '_ns', '_out.ns', '_sh', '_out.sh', '_tropical', '_out.tropical']
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'

# File data
file_data = '..\A3/textfiles\Data.nh.txt'
# Changes into a list of tuples
tuples_list = makeList(file_data)

# Plot list plots after the data is split into two new lists
plotList(name='Northern hemisphere', color='slateblue',
         list_tuples=tuples_list, xaxis='year', yaxis='temprature anomalies')
# Saves the graph
plt.savefig('..\A3/images/A3part1.png')

n = len(IO_monthly_files)
for i in range(n - 1):


    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > n or output_file_index > n:
        break

    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index] + '.txt'
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index] + '.txt'

    success = correctFile(input_file, output_file)

months = 48
dark = 'darkcyan'
medium = 'c'
bright = 'aqua'

list_nh = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)
list_nh1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)
list_nh2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)
list_nh3 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)
list_nh4 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 2, months)

list_ns = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)
list_ns1 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)
list_ns2 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)
list_ns3 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)
list_ns4 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 2, months)

list_sh = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)
list_sh1 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)
list_sh2 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)
list_sh3 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)
list_sh4 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 2, months)

list_trp = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)
list_trp1 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)
list_trp2 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)
list_trp3 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)
list_trp4 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 2, months)

# plotList("nh", list1, 'mo', 'year', 'temp')
# plotList("ns", list2, 'ko', 'year', 'temp')
# plotList("sh", list3, 'ro', 'year', 'temp')
# plotList("Trpl", listtrp, 'bo', 'year', 'temp')

# plt.savefig('..\A3/images/A3part2aYear.png')
plt.show()
