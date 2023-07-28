import numpy
from matplotlib import pyplot as plt

SIZE = 200

def main():
    # initialize Ez and Hy arrays with zeros
    ez = numpy.zeros(SIZE, dtype=float)
    hy = numpy.zeros(SIZE, dtype=float)

    # define constants
    imp0 = 377.0
    maxTime = 250
    timeSteps = numpy.linspace(0,maxTime,maxTime)
    ez50Values = numpy.empty(maxTime)

    # time stepping
    for qTime in timeSteps:
        #update magnetic field
        for mm in range(0,SIZE-1):
            hy[mm] = hy[mm] + (ez[mm + 1] - ez[mm]) /imp0

        #update electric field
        for mm in range(1,SIZE):
            ez[mm] = ez[mm] + (hy[mm] - hy[mm - 1]) * imp0

        # hardwire a source node
        ez[0] = numpy.exp(-(qTime -30) * (qTime -30) /10)
        ez50values = numpy.append(ez50Values, [ez[50]])
        #ez50Values += ez[50]
        #print(ez[50])
    #print(ez50Values)
    plt.plot(timeSteps, ez50Values)
    plt.show()

main()