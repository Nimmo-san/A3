import os
import re

import matplotlib.pyplot as plt


def openFile(file_path, argument):
    file = None
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
    f = openFile(data_full_path, 'r')
    if f == None:
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


# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]


def changetuples(data):
    return [tuple(element) for element in data]


def tofloat(lst):
    return [tofloat(i) if isinstance(i, list) else float(i) for i in lst]


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def makeAverageList(input_file, column_v1=0, column_v2=0, number_months=0):
    column1 = []

    file = openFile(input_file, 'r')
    lines = [line.rstrip('\n') for line in file]
    if not file.close():
        file.close()

    if len(lines) % number_months != 0:
        print("Pick a value that evenly divides the data! {}".format(file.name))
        exit(1)

    i = 0
    while len(lines) - i != 0:
        split = lines[i].split(',')
        for element in split:
            if split.index(element) == column_v1:
                column1.append(element)
            elif split.index(element) == column_v2:
                column1.append(element)
        i = i + 1

    # print(column1)
    list1 = []
    for i in range(len(column1) - 1):
        data1 = 2 * (i - 1)
        data2 = 2 * i - 1
        if data1 < 0 and data2 < 0:
            continue
        if data1 > len(column1) or data2 > len(column1):
            break

        # print(data1, data2)
        tuple1 = (column1[data1], column1[data2])
        list1.append(tuple1)

    list1 = list(divide_chunks(list1, number_months))
    ave_list = []

    for line in list1:
        # print(line)
        summ = 0
        average = 0
        summ2 = 0
        average2 = 0
        i = 0
        j = 0
        while len(line) - i != 0 and len(line[i]) - j != 0:
            summ = summ + float(line[i][j])
            average = summ / len(line)
            summ2 = summ2 + float(line[i][j + 1])
            average2 = summ2 / len(line)
            i = i + 1
        tuple2 = ("{:5.3f}".format(average), "{:5.3f}".format(average2))
        ave_list.append(tuple2)
    return ave_list


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
