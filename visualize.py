from itertools import count
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        file = open("Step A/map1_data7.txt", 'r')
        text = file.read().splitlines()
        file.close()

        self.rows = 3
        self.columns = 3
        self.cellwidth = 16
        self.cellheight = 16

        w = self.columns*self.cellwidth+2*self.cellwidth
        h = self.rows*self.cellheight+50
        small = False

        if (w < 300):
            w = 300
        if (h < 300):
            h = 300

        actions = text[self.columns+4]
        observations = text[self.columns+6]

        path = []
        for i in range(self.columns):
            path.append(tuple(map(int, text[i+3].split())))

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
                self.rect[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", tags="rect")

                #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        # Generate Lines
        for i in range(len(actions)-1):
            x1 = path[i][1] * self.cellwidth + \
                self.cellwidth + self.cellwidth/2
            y1 = path[i][0] * self.cellheight + \
                self.cellheight + self.cellheight/2
            x2 = path[i+1][1] * self.cellwidth + \
                self.cellwidth + self.cellwidth/2
            y2 = path[i+1][0] * self.cellheight + \
                self.cellheight + self.cellheight/2
            self.lines = self.canvas.create_line(
                x1, y1, x2, y2, fill="red", width=3)

            #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        # Generate Points
        for item in path:
            x1 = item[1] * self.cellwidth + self.cellwidth + self.cellwidth/4
            y1 = item[0] * self.cellheight + \
                self.cellheight + self.cellheight/4
            x2 = x1 + self.cellwidth - self.cellwidth/4*2
            y2 = y1 + self.cellheight - self.cellheight/4*2
            self.oval = self.canvas.create_oval(
                x1, y1, x2, y2, fill="red", tags="point")

            #print(str(x1) + "," + str(y1) + " -> " + str(x2) + "," + str(y2))

        initial = tuple(map(int, text[1].split()))

        # print(path)

        self.canvas.create_text(
            w/2, h-25, text="Actions: " + actions, font=('Helvetica 11 bold'), fill="black")
        self.canvas.create_text(w/2, h-10, text="Observations: " +
                                observations, font=('Helvetica 11 bold'), fill="black")


if __name__ == "__main__":
    app = App()
    app.mainloop()
