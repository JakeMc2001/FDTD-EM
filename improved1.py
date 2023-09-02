import numpy as np
from generateWaterfall import *
from implementGridObj import *

def main():
    SizeX = 200
    imp0 = 377.0
    maxTime = 250
    cdtds = 1.0 #courant number
    
    # Define grid
    g = Grid(SizeX, maxTime, cdtds)
    ez = g.ez
    hy = g.hy

    # define arrays to store time steps and ez[50] values
    timeSteps = np.linspace(0,maxTime,maxTime)
    ez50Values = np.zeros(maxTime, dtype=float)

    # time stepping
    for qTime in timeSteps:
        for mm in range(0,SizeX-1):
            hy[mm] = hy[mm] + (ez[mm+1] - ez[mm]) /imp0

        for mm in range(1,SizeX-1):
            ez[mm] = ez[mm] + (hy[mm] - hy[mm-1]) * imp0
        
        # hardwire a source node
        ez[0] = np.exp(-(qTime - 30.0) * (qTime - 30.0) / 100.0)

        # append current value of ez[50] to array
        currentIndex = np.where(timeSteps == qTime)[0]
        ez50Values[currentIndex] = ez[50]

    # create and display plot of ez[50] values
    plt.plot(timeSteps, ez50Values)
    plt.xlabel('Time Step')
    plt.ylabel('Ez[50] (V/m)')
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-')
    plt.grid(which='minor', linestyle=':')
    plt.title("improved1.py (Program 4.6)")
    plt.show()

main()