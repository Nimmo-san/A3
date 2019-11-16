import os
import re

import matplotlib.pyplot as plt


def openFile(file_path, argument):
    list_arguments = ['r', 'w', 'w+', 'a', 'rb',
    'r+', 'rb+', 'wb', 'wb+', 'ab', 'a+', 'ab+']
    if os.path.exists(file_path):
        if argument in list_arguments:
            try:
                file = open(file_path, argument)
                return file
            except FileNotFoundError:
                return
        print("Given argument: {} is invalid".format(argument))
    else:
        print("File {} could not be found!".format(file_path))
    return file


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
    f.close()
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
    return full_list if len(full_list) != 0 else None


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


def remove_pattern(data):
    removed_pattern = []
    # Checks if the data is null
    if len(data) <= 0:
        print("Length of data is null!")
        # Returns none if null
        return None

    # If not finds a pattern and replaces it
    # with the chosen character
    for line in data:
        try:
            string = re.sub(' +', ',', line)
        except:
            pass
        removed_pattern.append(string)
    # Then return the data after
    return removed_pattern


def split_date(data):
    altered_data = []
    # Checks if data is null
    if len(data) <= 0:
        print("Length of data is null")
        # Returns none if null
        return None

    # Iterates through the data
    for line in data:
        # Splitting each line of the data
        split = line.split(',')
        try:
            # Accessing the data from the index 0 till 7
            # Assuming date is always betwene index 0 and 7
            date = line[0:7]
        except:
            # if not pass it
            pass

        # Splitting the data to get the year and month
        dates = date.split('/')
        month = int(dates[1]) * 0.083
        rounded_month = "{:2.3}".format(month)

        # Making a new string based on the recently new data
        # which is the normalisations of the month
        newstring = str(int(dates[0])+float(rounded_month))
        # The old is replaced with the new string using a list comprehension
        split = [word.replace(date, newstring) for word in split]
        # appended into the data
        altered_data.append(split)
    # and returned
    # print(altered_data)
    return altered_data


def write_tofile(data, file):
    if len(data) <= 0:
        return False

    for line in data:
        file.write(line + '\n')
    return True


def average(data):
    if len(data) <= 0:
        return 0
    aver = float('{:5.3}'.format(sum(data) / len(data)))
    return aver


def makeAverageList(input_file, column_Value=0, column_Value2=0, number_months=0):
    columndata1 = []
    columndata2 = []
    counter = 0
    file = openFile(input_file, 'r')
    lines = [line.rstrip('\n') for line in file]
    if not file.close():
        print("{} is Open!".format(file.name))
        file.close()

    if number_months <= len(lines):
        for line in lines:
            data2 = line.split(',')
            # print(data2)
            if counter < number_months:
                for i in range(1, len(data2)):
                    if column_Value == i:
                        columndata1.append(data2[i])
                    elif column_Value2 == i:
                        columndata2.append(data2[i])
                counter = counter + 1
    else:
        print("Number of months, {}, out of range!".format(number_months))

    columndata1 = [float(i) for i in columndata1]
    columndata2 = [float(i) for i in columndata2]

    return None


def correctFile(input_file, output_file):
    removed_pattern = []
    data = []
    full_data = []

    # Ignores an error, rather than crash if the files dont exist
    try:
        toreadfile = open(input_file, 'r')
        writefile = open(output_file, 'w')
    except FileNotFoundError:
        print("File, {} couldn't be found!".format(input_file))
        print("File, {} could't be found! \n File being created.".format(output_file))
        writefile = open(output_file, 'w+')
        exit(1)

    # Reads the data in the file
    lines = [line.rstrip('\n') for line in toreadfile]
    # Asks the function to remove the pattern
    removed_pattern = remove_pattern(lines)
    # Requests for the data to be split
    data = split_date(removed_pattern)
    # print(data)

    # Iterates through joining each one
    for line in data:
        string1 = ','.join(line)
        full_data.append(string1)

    success = write_tofile(full_data, writefile)

    toreadfile.close()
    writefile.close()
    return success

# # file = 'E:/University\Coding\A3ProjectPython\ProjectData\Data.nh.txt'
# file = '..\A3\Data.nh.txt'
# print(make_list(file))
