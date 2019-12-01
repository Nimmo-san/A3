class Analysis:
    def __init__(self, x='x', y='y'):
        self.x_title = x
        self.y_title = y
        self.input_files = []
        self.titles = []
        self.list_tuples = []
        self.list_uncertainty1 = []
        self.list_uncertainty2 = []

    def addFile(self, input_file, title):
        if input_file and title:
            self.input_files.append(input_file)
            self.titles.append(title)

    def printLists(self):
        print("input_file data:")
        for data in self.input_files:
            print('->' + data)

        print("\ntitles data:")
        for data in self.titles:
            print('->' + data)

    def plotListTuples(self):
        x = []
        y = []

        for (xp, yp) in self.list_tuples:
            x.append(xp)
            y.append(yp)

    def updateLists(self, tuple_columns, granularity=0, type_='', type_2='', min_=0, max_=0):
        return
