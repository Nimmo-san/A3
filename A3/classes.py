class Analysis:
    def __init__(self, x='x', y='y'):
        self.x_title = x
        self.y_title = y
        self.input_files = []
        self.titles = []
        self.list_tuples = []
        self.list_uncertainty1 = []
        self.list_uncertainty2 = []
        self.colors = {'d': 'm', 'me': 'fuchsia', 'l': 'magenta', 'vl': 'orchid'}

    def addFile(self, input_file, title):
        if input_file and title:
            self.input_files.append(input_file)
            self.titles.append(title)

    def printLists(self):
        print("\nInput files, titles: \n")
        for data in range(len(self.input_files)):
            print(" -> {}.txt, {}".format(self.input_files[data], self.titles[data]))

    def plotListTuples(self):
        x = []
        y = []

        for (xp, yp) in self.list_tuples:
            x.append(xp)
            y.append(yp)

    def updateLists(self, tuple_columns, granularity=0, type_='', type_2='', min_=0, max_=0):
        opened_Files = []
        files_data = []
        for i in self.input_files:
            file = open(i + '.txt', 'r')
            # opened_Files.append(file)
            lines = [line.rstrip('\n') for line in file]
            self._retrieveData(lines, tuple_columns, min_, max_)

        return

    def chunks(list_, offset):
        for i in range(0, len(list_), offset):
            yield list_[i:i + offset]

    def _retrieveData(self, data, tuple_, min_, max_):
        list_ = []

        list_xy = []
        list_u = []
        list_u2 = []

        # list_ = func(data, (0,1,8,9,10,11), 3, 0, 4)
        if min_ >= 0 and max_ <= len(data):
            for elem in range(min_, max_, 1):
                split = data[elem].split(',')
                for j in range(len(split)):
                    if j in tuple_:
                        list_.append(split[j])
        else:
            print(min_, max_, "Out of bounds!")

        list_ = self.chunks(list_, 2)
        size = len(list_)
        for i in range(1, size):
            in1 = 3 * (i - 1)  # nominal values
            in2 = 3 * i - 2  # uncertainty 1
            in3 = 3 * i - 1  # uncertainty 2
            if in1 > size or in2 > size or in3 > size:
                break

            list_xy.append(list_[in1])
            list_u.append(list_[in2])
            list_u2.append(list_[in3])

        return

    def scatterPlot(self, one, two, color='m'):
        return

# def _retrieveData(data, tuple_, gra, min_, max_):
#         list_ = []
#         list_xy = []
#         list_u = []
#         list_u2 = []
#         # list_ = func(data, (0,1,8,9,10,11), 3, 0, 4)
#         if min_ >= 0 and max_ <= len(data):
#             for elem in range(min_, max_, 1):
#                 split = data[elem].split(',')
#                 for j in range(len(split)):
#                     if j in tuple_:
#                         list_.append(split[j])
#         else:
#             print(min_, max_, "Out of bounds!")
#
#
#         list_ = list(list_into_chunks(list_, 2))
#
#         for i in range(1, len(list_)):
#             in1 = 3 * ( i - 1)
#             in2 = 3 * i - 2
#             in3 = 3 * i - 1
#             if in1 > len(list_) or in2 > len(list_) or in3 > len(list_):
#               break
#
#             # print(in1, in2, in3)
#             list_xy.append(list_[in1])
#             list_u.append(list_[in2])
#             list_u2.append(list_[in3])
#
#         list_xy = list(list_into_chunks(list_xy, gra))
#         list_u = list(list_into_chunks(list_u, gra))
#         list_u2 = list(list_into_chunks(list_u2, gra))
#         return (list_xy, list_u, list_u2)
#         # return list_
