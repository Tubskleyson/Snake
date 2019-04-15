from tkinter import Frame,Label,Button

class Board:

    def __init__(self, launcher):

        self.launcher = launcher

        self.frame = Frame(launcher.window)

        cell0 = Frame(self.frame)

        scoreLbl = Label(cell0,text='Score', font=('Arial',20))
        self.score = Label(cell0,text=0,font=('Arial',15))

        scoreLbl.pack(pady=10)
        self.score.pack()

        levelLbl = Label(cell0,text='Level', font=('Arial',20))
        self.level = Label(cell0,text=0,font=('Arial',15))

        levelLbl.pack(pady=10)
        self.level.pack()

        cell0.pack(pady=30)

        self.frame.pack()

    def scoreup(self,value):

        self.score['text'] += value

    def levelup(self):

        self.level['text'] += 1

    def death(self):

        restart = Button(self.frame, text='Restart',font=('Arial',13), command=self.launcher.start)
        restart.pack(side='bottom')

