from itertools import count
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        App.initialize(self)
        App.grid(self)
        App.show_path(self)

    def initialize(self):

        folder = "maps"
        mapFile = open(folder + "/map1")
        self.mapText = []
        for line in mapFile.readlines():
            line = line.strip()
            self.mapText.append(line.split(' '))
        mapFile.close

        dataFile = open(folder + "/map1_data3.txt", 'r')
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
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        #self.canvas.configure(yscrollcommand=self.vsb.set)
        #self.vsb.pack(side="right", fill="y")
        #self.canvas.pack(side="left", fill="both", expand=True)

        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical",
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.rect = {}
        self.oval = {}
        self.lines = {}

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

    def show_path(self):
        # Generate Lines
        # print(len(self.path))
        for i in range(len(self.actions)-1):
            y1 = (self.path[i][0]+1) * self.cellwidth + self.cellwidth/2
            x1 = (self.path[i][1]+1) * self.cellheight + self.cellheight/2
            y2 = (self.path[i+1][0]+1) * self.cellwidth + self.cellwidth/2
            x2 = (self.path[i+1][1]+1) * self.cellheight + self.cellheight/2
            # print(str(x1) + "," + str(y1) + " -> " + str(x2) + str(y2))
            self.lines = self.canvas.create_line(
                x1, y1, x2, y2, fill="green", width=3)

        # Plot Points
        for item in self.path:
            y1 = (item[0]+1) * self.cellwidth + self.cellwidth/4
            x1 = (item[1]+1) * self.cellheight + self.cellheight/4
            x2 = x1 + self.cellwidth - self.cellwidth/4*2
            y2 = y1 + self.cellheight - self.cellheight/4*2
            self.oval = self.canvas.create_oval(
                x1, y1, x2, y2, fill="#F0FFF0", tags="point")

        # Recolor first point
        y1 = (self.path[0][0]+1) * self.cellwidth + self.cellwidth/4
        x1 = (self.path[0][1]+1) * self.cellheight + self.cellheight/4
        x2 = x1 + self.cellwidth - self.cellwidth/4*2
        y2 = y1 + self.cellheight - self.cellheight/4*2
        self.oval = self.canvas.create_oval(
            x1, y1, x2, y2, fill="#FFBF00", tags="point")

        # Recolor last point
        y1 = (self.path[len(self.path)-1][0]+1) * \
            self.cellwidth + self.cellwidth/4
        x1 = (self.path[len(self.path)-1][1]+1) * \
            self.cellheight + self.cellheight/4
        x2 = x1 + self.cellwidth - self.cellwidth/4*2
        y2 = y1 + self.cellheight - self.cellheight/4*2
        self.oval = self.canvas.create_oval(
            x1, y1, x2, y2, fill="#74C365", tags="point")

        # Legend
        self.canvas.create_text(
            self.w/2, self.h-80, text="Actions: " + self.actions, font=('Helvetica 11 bold'), fill="black")
        self.canvas.create_text(self.w/2, self.h-65, text="Observations: " +
                                self.observations, font=('Helvetica 11 bold'), fill="black")

        self.canvas.create_rectangle(
            self.w-400, self.h/2-120, self.w-100, self.h/2+120, fill="black")
        self.canvas.create_text(
            self.w-250, self.h/2-70, text="Legend", font=('Helvetica 24'), fill="white")
        self.canvas.create_text(
            self.w-250, self.h/2-40, text="Starting Point", font=('Helvetica 16'), fill="#FFBF00")
        self.canvas.create_text(
            self.w-250, self.h/2-20, text="Ending Point", font=('Helvetica 16'), fill="#74C365")
        self.canvas.create_text(
            self.w-250, self.h/2, text="Normal Cell", font=('Helvetica 16'), fill="#E1E7FF")
        self.canvas.create_text(
            self.w-250, self.h/2+20, text="Highway Cell", font=('Helvetica 16'), fill="#FDFFE1")
        self.canvas.create_text(
            self.w-250, self.h/2+40, text="Hard to Traverse Cell", font=('Helvetica 16'), fill="#FFE1FF")
        self.canvas.create_text(
            self.w-250, self.h/2+60, text="Blocked Cell", font=('Helvetica 16'), fill="red")


if __name__ == "__main__":
    app = App()
    app.mainloop()
