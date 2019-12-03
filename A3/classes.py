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
            opened_Files.append(file)

        return

    def _retrieveData(data, tuple_, gra, min_, max_):
        list_ = []
        # list_ = func(data, (0,1,8,9,10,11), 3, 0, 4)
        if min_ >= 0 and max_ <= len(data):
            for elem in range(min_, max_, 1):
                split = data[elem].split(',')
                for j in range(len(split)):
                    if j in tuple_:
                        list_.append(split[j])
        else:
            print(min_, max_, "Out of bounds!")
        return list_

    def scatterPlot(self, one, two, color='m'):
        return
