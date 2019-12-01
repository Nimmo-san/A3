class Analysis:
    def __init__(self, x='x', y='y'):
        self.x_title = x
        self.y_title = y
        self.input_files = []
        self.titles = []

    def addFile(self, input_file, title):
        if input_file and title:
            self.input_files.append(input_file)
            self.titles.append(title)

    def printLists(self):
        if len(self.input_files) != len(self.titles):
            print("{} data: \n".format(input_files))
            for data in self.input_files:
                print(data)

            print("")
