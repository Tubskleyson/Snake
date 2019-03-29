from tkinter import Tk
from table import Table
from snake import Snake
from random import randint

class Launcher:

    def __init__(self,side):

        self.window = Tk()
        self.window.geometry("%sx%s"%(side,side))

        self.table = Table(self.window,50,side,side)

        self.snake = Snake(self)

        self.window.after(100, self.update)

        self.window.bind("<Key>", self.keypress)

        self.food = 0

        self.fc = 20 #food countdown

        self.window.mainloop()



    def update(self):

        self.snake.move()

        self.window.after(100, self.update)

        if not self.food:
            self.fc -= 1

        if not self.fc:

            self.makefood()


    def keypress(self,e):

        key = e.char

        l = ['w',[0,-1],'a',[-1,0],'s',[0,1],'d',[1,0]]

        if key in l:
            self.snake.direction = l[l.index(key)+1]

    def makefood(self):

        while 1:

            rx = randint(0, 50)
            ry = randint(0, 50)

            node = self.table.get(rx,ry)

            if node and not node.state:

                node.set(2)
                break

        self.food = 1
        self.fc = 20



l = Launcher(500)