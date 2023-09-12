# import parent file to sys path
import sys
sys.path.append('../')
import numpy
from matplotlib import pyplot as plt
from generateWaterfall import *

SIZE = 200

def main():
    # initialize Ez and Hy arrays with zeros
    ez = numpy.zeros(SIZE, dtype=float)
    hy = numpy.zeros(SIZE, dtype=float)
    # define constants
    imp0 = 377.0
    maxTime = 200

    # initialize array to store data every 10 timeSteps
    simData = numpy.zeros((int(maxTime/10), SIZE), dtype=float)

    # define arrays to store time steps and ez[50] values
    timeSteps = numpy.linspace(0,maxTime,maxTime)
    ez50Values = numpy.zeros(maxTime, dtype=float)
    # time stepping
    for qTime in timeSteps:
        #add a magnetic field ABC to right side of grid
        hy[SIZE-1] = hy[SIZE-2]

        #update magnetic field
        for mm in range(0,SIZE-1):
            hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) /imp0

        #add an electric field ABC to left side of grid
        ez[0] = ez[1]

        #update electric field
        for mm in range(1,SIZE):
            ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0

        # use additive source at node 50
        ez[50] += numpy.exp(-1.0*(qTime -30.0) * (qTime -30.0) /100.0)

        # append current value of ez[50] to array
        currentIndex = numpy.where(timeSteps == qTime)[0]
        ez50Values[currentIndex] = ez[50]
        if currentIndex % 10==0:
            simData[int(currentIndex/10)] = ez
    createWaterfall(simData, 0.5, maxTime, '1Dadditive plot')
    # create and display plot of ez[50] values
    # plt.plot(timeSteps, ez50Values)
    # plt.xlabel('Time Step')
    # plt.ylabel('Ez[50] (V/m)')
    # plt.minorticks_on()
    # plt.grid(which='major', linestyle='-')
    # plt.grid(which='minor', linestyle=':')
    # plt.title("1Dadditive (Program 3.4)")
    # plt.show()

main()