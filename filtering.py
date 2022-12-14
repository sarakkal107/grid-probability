from itertools import count
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        App.initialize(self)
        App.grid(self)

    def initialize(self):

        folder = "stepA"
        mapFile = open(folder + "/map")
        self.mapText = []
        for line in mapFile.readlines():
            line = line.strip()
            self.mapText.append(line.split(' '))
        mapFile.close

        dataFile = open(folder + "/map_data.txt", 'r')
        self.dataText = dataFile.read().splitlines()
        dataFile.close()

        self.rows = len(self.mapText)
        self.columns = len(self.mapText[0])
        self.cellwidth = 10
        self.cellheight = 10

        self.w = self.columns*self.cellwidth+2*self.cellwidth + 500
        self.h = self.rows*self.cellheight+120

        if (self.w < 300):
            self.w = 300
        if (self.h < 300):
            self.h = 300

        self.actions = self.dataText[self.rows+4]
        # print(self.actions)
        self.observations = self.dataText[self.rows+6]

        self.path = [tuple(map(int, self.dataText[1].split()))]
        for i in range(self.rows):
            self.path.append(tuple(map(int, self.dataText[i+3].split())))
        # print(path)

        self.canvas = tk.Canvas(
            self, width=self.w, height=self.h, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.title("Data Visualization")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.rect = {}

        # Filtering Stuff
        count = 0
        self.previousState = [[1]*self.columns for x in range(self.rows)]
        self.observationalN = [[1]*self.columns for x in range(self.rows)]
        self.observationalH = [[1]*self.columns for x in range(self.rows)]
        self.observationalT = [[1]*self.columns for x in range(self.rows)]

        for row in range(self.rows):
            for column in range(self.columns):
                if self.mapText[row][column] == 'B':
                    self.previousState[row][column] = 0.0
                    self.observationalN[row][column] = 0.0
                    self.observationalH[row][column] = 0.0
                    self.observationalT[row][column] = 0.0
                else:
                    count += 1
                    if self.mapText[row][column] == 'N':
                        self.observationalN[row][column] = 0.9
                        self.observationalH[row][column] = 0.05
                        self.observationalT[row][column] = 0.05
                    elif self.mapText[row][column] == 'H':
                        self.observationalN[row][column] = 0.05
                        self.observationalH[row][column] = 0.9
                        self.observationalT[row][column] = 0.05
                    elif self.mapText[row][column] == 'T':
                        self.observationalN[row][column] = 0.05
                        self.observationalH[row][column] = 0.05
                        self.observationalT[row][column] = 0.9

        for row in range(self.rows):
            for column in range(self.columns):
                if self.previousState[row][column] != 0.0:
                    self.previousState[row][column] = 1/count

        self.currentState = self.previousState
        print(self.previousState)
        print(self.observationalN)
        print(self.observationalH)
        print(self.observationalT)

    def grid(self):
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellwidth + self.cellwidth
                y1 = row * self.cellheight + self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                color = ""
                if (self.mapText[row][column] == "N"):
                    color = "#E1E7FF"
                elif (self.mapText[row][column] == "H"):
                    color = "#FDFFE1"
                elif (self.mapText[row][column] == "T"):
                    color = "#FFE1FF"
                else:
                    color = "red"

                self.rect[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, tags="rect")


if __name__ == "__main__":
    app = App()
    app.mainloop()
