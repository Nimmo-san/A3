import matplotlib.pyplot as plt


def makeList(data_full_path):
    # print(data_full_path)
    full_list = []
    # Checks if the file exists or not
    try:
        f = open(data_full_path, 'r')
    except FileNotFoundError:
        # If not it prints an error statement to the console
        print("FILE COULD NOT BE OPENED!")
        # And exits with argument 1
        exit(1)

    # Reads the data from the list and appends it to a list
    lines = [line.rstrip('\n') for line in f]
    # Iteration through the data and splits by a space
    for line in lines:
        try:
            split = line.split(' ')
        except:
            pass
        # Saves it to a tuple to be appended to a list
        year_data_tuple = (split[0], split[1])
        full_list.append(year_data_tuple)
    # Checks if list is empty, if not it returns the list
    if len(full_list) != 0:
        return full_list


def plotList(name, list_tuples, color, xaxis, yaxis):
    # Creates new empty lists for the x and y axis respectively
    x = []
    y = []
    # Goes through the list of tuples
    # And appends it to its corresponding list
    for i in range(len(list_tuples)):
        for j in range(len(list_tuples[i]) - 1):
            xi = list_tuples[i][j]
            yi = list_tuples[i][j + 1]
            x.append(xi)
            y.append(yi)
    # Plots a 2-dimensional graph
    # With the corresponding values of x and y
    plt.plot(x, y, color, label=name)
    # Shows the legend, which is the label name in the argument
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.legend()


def correctFile(input_file, output_file):
    try:
        toreadfile = open(input_file, 'r')
    except FileNotFoundError:
        print("File couldn't be found!")
        exit(1)

    try:
        writefile = open(output_file, 'w')
    except FileNotFoundError:
        print("File could't be found! \n File being created.")
        writefile = open(output_file, 'w+')

    lines = [line.rstrip('\n') for line in toreadfile]
    print(lines[0][0:8])
    toreadfile.close()
    writefile.close()

# # file = 'E:/University\Coding\A3ProjectPython\ProjectData\Data.nh.txt'
# file = '..\A3\Data.nh.txt'
# print(make_list(file))
