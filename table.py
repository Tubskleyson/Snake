from tkinter import *
from node import *

class Table:

    def __init__(self,window,side,width,height):

        self.window = window

        self.side = side
        self.width = width
        self.height = height

        self.canvas = Canvas(self.window, width = self.width, height = self.height)
        self.canvas.pack(side='left')

        self.node_side = min([self.height,self.width])/side

        self.nodes = []

        for x in range(side):

            column = []

            for y in range(side):

                column += [Node(x,y,self,self.node_side)]

            self.nodes += [column]

    def get(self,x,y):

        if all(i>=0 and i<self.side for i in [x,y]):
            return self.nodes[x][y]

        if x<0: x = self.side-1
        if y < 0: y = self.side - 1
        if x == self.side: x = 0
        if y == self.side: y = 0

        return self.nodes[x][y]