import numpy as np
from matplotlib import pyplot as plt

def createWaterfall(simData, offset, maxTime, plotTitle):
    counter = 0
    for sim in simData:
        plt.plot(sim+(counter*offset), linewidth=0.5)
        counter +=1
    plt.xlabel('Grid Point')
    plt.ylabel(f"Time Steps (up to {maxTime} time steps)")
    plt.xlim([0,200])
    plt.title(plotTitle)
    plt.show()



# testArray = [[1,2,3,4], [2,3,4,1], [3,3,3,4]]
# testArray = np.array(testArray)
# createWaterfall(testArray)