class Snake:

    def __init__(self,launcher):

        self.launcher = launcher

        self.table = launcher.table

        self.size = 5

        self.rings = []

        for i in range(self.size):

            p = self.table.side//2

            self.spawn(p-i,p)

        self.direction = [1,0]

        self.ate = 0

    def spawn(self,x,y):

        ring = self.table.get(x,y)
        ring.set(1)

        self.rings += [ring]

    def move(self):

        new = 0

        for i in range(self.size):

            old = self.rings[i]

            if not new:

                new = old.next(self.direction)

                if new.state == 2: self.ate = 1

            old.set(0)

            new.set(1)

            self.rings[i] = new

            new = old

        if self.ate:

            new.set(1)
            self.rings += [new]

            self.size += 1
            self.ate = 0

            self.launcher.food = 0