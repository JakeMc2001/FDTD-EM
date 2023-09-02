import numpy as np
from generateWaterfall import *
from implementGridObj import *

imp0 = 377.0

def main():
    SizeX = 200
    maxTime = 250
    cdtds = 1.0 #courant number
    
    # Define grid
    g = Grid(SizeX, maxTime, cdtds)

    # define arrays to store time steps and ez[50] values
    timeSteps = np.linspace(0,maxTime,maxTime)
    ez50Values = np.zeros(maxTime, dtype=float)

    # time stepping
    for qTime in timeSteps:
        # update hy and ez
        g.hy = updateH2(g)
        g.ez = updateE2(g)

        # hardwire a source node
        g.ez[0] = source(qTime)

        # append current value of ez[50] to array
        currentIndex = np.where(timeSteps == qTime)[0]
        ez50Values[currentIndex] = g.ez[50]

    # create and display plot of ez[50] values
    plt.plot(timeSteps, ez50Values)
    plt.xlabel('Time Step')
    plt.ylabel('Ez[50] (V/m)')
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle=':')
    plt.title("improved2.py (Program 4.11)")
    plt.show()

def updateH2(g):
    for mm in range(0, g.sizeX - 1):
        g.hy[mm] = g.hy[mm] + (g.ez[mm+1] - g.ez[mm]) / imp0
    return g.hy

def updateE2(g):
    for mm in range(1, g.sizeX-1):
        g.ez[mm] = g.ez[mm] + (g.hy[mm] - g.hy[mm-1]) * imp0
    return g.ez

def source(time):
    return np.exp(-(time - 30.0) * (time - 30.0) / 100.0)


main()