from tkinter import *
from table import Table
from board import Board
from snake import Snake
from random import randint

class Launcher:

    def __init__(self,side):

        self.side = side

        self.window = Tk()
        self.window.geometry("%sx%s"%(side+200,side))

        self.menu = Frame(self.window)

        title = Label(self.menu,text="The Snake",font=('Arial',40))
        bt1 = Button(self.menu, text='Start', font=('Arial',15), width=10, command=self.start)

        self.menuWidg = [title,bt1]

        for i in self.menuWidg: i.pack(pady=30)

        self.menu.pack(pady=70)

        self.onscreen = [self.menu]

        self.window.mainloop()

    def start(self):

        side = self.side

        self.speed = 50

        for i in self.onscreen: i.destroy()

        self.table = Table(self.window, 50, side, side)

        self.board = Board(self)

        self.snake = Snake(self)

        self.window.after(100, self.update)

        self.window.bind("<Key>", self.keypress)

        self.food = 0

        self.fc = 20  # food countdown

        self.onscreen = [self.table.canvas, self.board.frame]

        self.nvl = 1


    def update(self):

        if not self.snake.dead: self.window.after(self.speed, self.update)

        else:

            self.board.death()
            return

        if self.snake.size/10 == self.nvl:

            print('Level up')
            self.nvl += 1
            self.speed -= 2

            self.board.levelup()

        self.snake.direction = self.snake.newdirection
        self.snake.move()

        if not self.food:

            self.fc -= 1

        if not self.fc:

            self.makefood()


    def keypress(self,e):

        code = e.keycode
        char = e.char

        l = ['w',[0,-1],'a',[-1,0],'s',[0,1],'d',[1,0]]
        k = [38, [0, -1], 37, [-1, 0], 40, [0, 1], 39, [1, 0]]

        d = 0
        if char in l: d = l[l.index(char)+1]
        if code in k: d = k[k.index(code) + 1]

        if d and not all(not i for i in [d[i]+self.snake.direction[i] for i in range(2)]):
            self.snake.newdirection = d

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

    def restart(self):

        pass



l = Launcher(500)
