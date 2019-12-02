import matplotlib.pyplot as plt

from functions import plotList, makeList, correctFile, makeAverageList, plotWithError

parent_path = '..\A3/textfiles'
IO_monthly_files = ['_nh.txt', '_out.nh.txt', '_ns.txt',
                    '_out.ns.txt', '_sh.txt', '_out.sh.txt',
                    '_tropical.txt', '_out.tropical.txt']
monthly_input = '\Data.monthly'
monthly_output = '/Parsed.monthly'
colors = {1: 'darkcyan', 2: 'c', 3: 'aqua'}

# File data
file_data = '..\A3/textfiles\Data.nh.txt'
# Changes into a list of tuples
tuples_list = makeList(file_data)

# Plot list plots after the data is split into two new lists
plotList(name='Northern hemisphere', color='slateblue',
         list_tuples=tuples_list, xaxis='year', yaxis='temprature anomalies')
# Saves the graph
plt.savefig('..\A3/images/A3part1.png')
plt.show()

n = len(IO_monthly_files)
for i in range(n - 1):

    input_file_index = 2 * (i - 1)
    output_file_index = 2 * i - 1
    if input_file_index < 0 and output_file_index < 0:
        continue
    if input_file_index > n or output_file_index > n:
        break

    input_file = parent_path + monthly_input + IO_monthly_files[input_file_index]
    output_file = parent_path + monthly_output + IO_monthly_files[output_file_index]

    success = correctFile(input_file, output_file)

months = 48

list_nh = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 1, months)
list_nh1 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 8, months)
list_nh2 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 9, months)
list_nh3 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 10, months)
list_nh4 = makeAverageList(parent_path + '\Parsed.monthly_out.nh.txt', 0, 11, months)

list_ns = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 1, months)
list_ns1 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 8, months)
list_ns2 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 9, months)
list_ns3 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 10, months)
list_ns4 = makeAverageList(parent_path + '\Parsed.monthly_out.ns.txt', 0, 11, months)

list_sh = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 1, months)
list_sh1 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 8, months)
list_sh2 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 9, months)
list_sh3 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 10, months)
list_sh4 = makeAverageList(parent_path + '\Parsed.monthly_out.sh.txt', 0, 11, months)

list_trp = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 1, months)
list_trp1 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 8, months)
list_trp2 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 9, months)
list_trp3 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 10, months)
list_trp4 = makeAverageList(parent_path + '\Parsed.monthly_out.tropical.txt', 0, 11, months)

plotWithError('nh', 'nhu1', list_nh, list_nh3, list_nh4, colors[1], colors[3])
plotWithError('nh', 'nhu2', list_nh, list_nh1, list_nh2, colors[1], colors[2])
plt.show()

plotWithError('ns', 'nsu1', list_ns, list_ns3, list_ns4, colors[1], colors[3])
plotWithError('ns', 'nsu2', list_ns, list_ns1, list_ns2, colors[1], colors[2])
plt.show()

plotWithError('sh', 'shu1', list_sh, list_sh3, list_sh4, colors[1], colors[3])
plotWithError('sh', 'shu1', list_sh, list_sh1, list_sh2, colors[1], colors[2])
plt.show()

plotWithError('trp', 'trpu1', list_trp, list_trp3, list_trp4, colors[1], colors[3])
plotWithError('trp', 'trpu1', list_trp, list_trp1, list_trp2, colors[1], colors[2])
plt.show()

# plt.savefig('..\A3/images/A3part2aYear.png')
