from itertools import count
import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rows = 50
        self.columns = 100
        self.cellwidth = 15
        self.cellheight = 15

        w = self.columns*self.cellwidth+2*self.cellwidth
        h = self.rows*self.cellheight+50

        if (w < 300):
            w = 300
        if (h < 300):
            h = 300

        self.canvas = tk.Canvas(
            self, width=w, height=h, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.title("Data Visualization")

        self.rect = {}
        self.oval = {}
        for column in range(self.columns):
            for row in range(self.rows):
                x1 = column * self.cellwidth + self.cellwidth
                y1 = row * self.cellheight + self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", tags="rect")

        file = open("maps/map1_data1.txt", 'r')
        text = file.read().splitlines()
        file.close()

        path = []

        initial = tuple(map(int, text[1].split()))

        for i in range(self.columns):
            path.append(tuple(map(int, text[i+3].split())))

        actions = text[self.columns+4]
        observations = text[self.columns+6]

        print(path[0][0])

        for i in range(self.columns-1):
            self.displayLine(path[i][0], path[i][1],
                             path[i+1][0], path[i+1][1])

        self.canvas.create_text(
            w/2, h-25, text="Actions: " + actions, font=('Helvetica 11 bold'), fill="black")
        self.canvas.create_text(w/2, h-10, text="Observations: " +
                                observations, font=('Helvetica 11 bold'), fill="black")

    def displayLine(self, x1, y1, x2, y2):
        lineID = self.canvas.create_line(
            (x1-1)*7, (y1-1)*7, (x2-1)*7, (y2-1)*7, fill="red", width=3, arrow=tk.LAST)


if __name__ == "__main__":
    app = App()
    app.mainloop()
