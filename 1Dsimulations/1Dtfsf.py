# import parent file to sys path
import sys
sys.path.append('../')
import numpy as np
from matplotlib import pyplot as plt
from generateWaterfall import *

SIZE = 200

def main():
    # initialize Ez and Hy arrays with zeros
    ez = np.zeros(SIZE, dtype=float)
    hy = np.zeros(SIZE, dtype=float)
    # define constants
    imp0 = 377.0
    maxTime = 450

    # initialize array to store data every 10 timeSteps
    simData = np.zeros((int(maxTime/10), SIZE), dtype=float)

    # define arrays to store time steps and ez[50] values
    timeSteps = np.linspace(0,maxTime,maxTime)
    ez50Values = np.zeros(maxTime, dtype=float)
    # time stepping
    for qTime in timeSteps:
        #add a magnetic field ABC to right side of grid
        hy[SIZE-1] = hy[SIZE-2]

        #update magnetic field
        for mm in range(0,SIZE-1):
            hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) /imp0

        # correction for Hy adjacent to TFSF boundary
        hy[49] -= np.exp(-(qTime -30.0)*(qTime-30.0)/100) /imp0

        #add an electric field ABC to left side of grid
        ez[0] = ez[1]

        #update electric field
        for mm in range(1,SIZE):
            ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0

        # use additive source at node 50 and correct Ez adjacent to TFSF boundary
        ez[50] += np.exp(-(qTime + 1-30.0) * (qTime+1 -30.0) /100.0)

        # append current value of ez[50] to array
        currentIndex = np.where(timeSteps == qTime)[0]
        ez50Values[currentIndex] = ez[50]
        if currentIndex % 10==0:
            simData[int(currentIndex/10)] = ez
    # create a waterfall plot from the simulation data
    createWaterfall(simData, 0.5, maxTime, '1Dtfsf plot')

main()