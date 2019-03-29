class Node:

    def __init__(self,x,y,table,side):

        self.table = table

        self.x = x
        self.y = y
        self.coords = [x,y]

        self.canvas = table.canvas
        self.side = side

        self.rect = self.canvas.create_rectangle(x*side,y*side,(x+1)*side,(y+1)*side, outline='white')

        self.state = 0

    def set(self,state):

        self.state = state

        colors = ['','black','red']

        self.canvas.itemconfig(self.rect, fill=colors[state])

    def next(self,direction):

        x,y = [self.coords[i]+direction[i] for i in range(2)]
        return self.table.nodes[x][y]

