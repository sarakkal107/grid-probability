from itertools import count
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        folder = "maps"
        mapFile = open(folder + "/map1")
        mapText = []
        for line in mapFile.readlines():
            line = line.strip()
            mapText.append(line.split(' '))
        mapFile.close

        dataFile = open(folder + "/map1_data3.txt", 'r')
        dataText = dataFile.read().splitlines()
        dataFile.close()

        self.rows = len(mapText[0])
        self.columns = len(mapText)
        self.cellwidth = 16
        self.cellheight = 16

        w = self.columns*self.cellwidth+2*self.cellwidth
        h = self.rows*self.cellheight+100

        if (w < 300):
            w = 300
        if (h < 300):
            h = 300

        actions = dataText[self.columns+4]
        observations = dataText[self.columns+6]

        path = []
        for i in range(self.columns):
            path.append(tuple(map(int, dataText[i+3].split())))
        # print(path)

        self.canvas = tk.Canvas(
            self, width=w, height=h, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.title("Data Visualization")

        self.rect = {}
        self.oval = {}
        self.lines = {}

        # Generate Grid
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellwidth + self.cellwidth
                y1 = row * self.cellheight + self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                color = ""
                if (mapText[column][row] == "N"):
                    color = "#E1E7FF"
                elif (mapText[column][row] == "H"):
                    color = "#FDFFE1"
                elif (mapText[column][row] == "T"):
                    color = "#FFE1FF"
                else:
                    color = "red"

                self.rect[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, tags="rect")

                #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        # Generate Lines
        for i in range(len(actions)-1):
            x1 = (path[i][0]+1) * self.cellwidth + self.cellwidth/2
            y1 = (path[i][1]+1) * self.cellheight + self.cellheight/2
            x2 = (path[i+1][0]+1) * self.cellwidth + self.cellwidth/2
            y2 = (path[i+1][1]+1) * self.cellheight + self.cellheight/2
            self.lines = self.canvas.create_line(
                x1, y1, x2, y2, fill="green", width=3)

            #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        # Generate Points
        for item in path:
            x1 = (item[0]+1) * self.cellwidth + self.cellwidth/4
            y1 = (item[1]+1) * self.cellheight + self.cellheight/4
            x2 = x1 + self.cellwidth - self.cellwidth/4*2
            y2 = y1 + self.cellheight - self.cellheight/4*2
            self.oval = self.canvas.create_oval(
                x1, y1, x2, y2, fill="green", tags="point")

            #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        initial = tuple(map(int, dataText[1].split()))

        # print(path)

        self.canvas.create_text(
            w/2, h-60, text="Actions: " + actions, font=('Helvetica 11 bold'), fill="black")
        self.canvas.create_text(w/2, h-45, text="Observations: " +
                                observations, font=('Helvetica 11 bold'), fill="black")
        self.canvas.create_rectangle(
            0+self.cellwidth, h-30, w-self.cellwidth, h-10, fill="black")
        self.canvas.create_text(w/5*1, h-20, text="N",
                                font=('Helvetica 11 bold'), fill="#E1E7FF")
        self.canvas.create_text(w/5*2, h-20, text="H",
                                font=('Helvetica 11 bold'), fill="#FDFFE1")
        self.canvas.create_text(w/5*3, h-20, text="T",
                                font=('Helvetica 11 bold'), fill="#FFE1FF")
        self.canvas.create_text(w/5*4, h-20, text="B",
                                font=('Helvetica 11 bold'), fill="red")


if __name__ == "__main__":
    app = App()
    app.mainloop()
