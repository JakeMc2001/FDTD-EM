import numpy as np

class Grid:
    def __init__(self, sizeX, maxTime, cdtds):
        self.sizeX = sizeX
        self.maxTime = maxTime
        self.cdtds = cdtds #courant number
        self.ez = np.zeros(sizeX,dtype=float)
        self.hy = np.zeros(sizeX-1,dtype=float)
    
    def currentEz(self):
        for value in self.ez:
            print(value)
    
    def currentHy(self):
        for value in self.hy:
            print(value)

# g = Grid(5,10,1.0)
# g.currentEz()
# print("spacer --------")
# g.currentHy()