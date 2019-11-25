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
    for (xp, yp) in list_tuples:
        x.append(xp)
        y.append(yp)
    # Plots a 2-dimensional graph
    # With the corresponding values of x and y
    plt.plot(x, y, color, label=name, markersize=2)
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


def change_tuples(data):
    return [tuple(element) for element in data]


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
        # exit(1)

    column1 = []
    for element in lines:
        linessplit = element.split(',')
        for i in range(len(linessplit)):
            if i == column_v1:
                column1.append(linessplit[i])
            elif i == column_v2:
                column1.append(linessplit[i])
            else:
                pass

    # print(column1)
    data_list = []
    n = len(column1)
    for i in range(n):
        c1data = 2 * (i - 1)
        c2data = (2 * i) - 1

        if c1data < 0 or c2data < 0:
            continue
        if c1data > n or c2data > n:
            break
        tuple1 = (column1[c1data], column1[c2data])
        data_list.append(tuple1)

    list1 = list(divide_chunks(data_list, number_months))
    ave_list = []

    for line in list1:
        sum1 = 0
        average1 = 0
        sum2 = 0
        average2 = 0
        i = 0
        j = 0
        while len(line) - i != 0 and len(line[i]) - j != 0:
            sum1 = sum1 + float(line[i][j])
            average1 = sum1 / len(line)
            sum2 = sum2 + float(line[i][j + 1])
            average2 = sum2 / len(line)
            i += 1
        tuple1 = ("{:5.3f}".format(average1), "{:5.3f}".format(average2))
        ave_list.append(tuple1)
    return ave_list


def correctFile(input_file, output_file):
    removed_pattern = []
    data = []
    full_data = []

    # Catches the error, rather than crash if the files don't exist
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


def checkSize(n, m, l):
    return True if n == m and l == m else False

# def plotWithError(name, type_s, list_tuples, list_tuples2, list_tuples3, color1='mo', color2='ro', xname='X', yname='Y'):
#     n = len(list_tuples)
#     m = len(list_tuples2)
#     l = len(list_tuples3)
#     if checkSize(n, m, l):
#         continue
#     else:
#         Print("Size of list not equal: ", n, m, l)
#
#
#
#     return None
