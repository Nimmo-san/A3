from functions import plotList, makeList
import matplotlib.pyplot as plt

# File data
file_data = '..\A3\Data.nh.txt'
# Changes into a list of tuples
tuples_list = makeList(file_data)

# Plot list plots after the data is split into two new lists
plotList(name='Northern hemisphere', color='slateblue',
         list_tuples=tuples_list, xaxis='year', yaxis='temprature anomalies')
# Saves the graph
plt.savefig('A3part1.png')
# Then shows the graph
plt.show()

