import matplotlib.pyplot as plt
import numpy
import constants as c

resultsA = numpy.load("resultsA.npy")
resultsA2 = numpy.load("resultsA2.npy")
resultsB = numpy.load("resultsB.npy")
resultsC = numpy.load("resultsC.npy")

resultsACollapsed = numpy.zeros(c.numberOfGenerations)
resultsA2Collapsed = numpy.zeros(c.numberOfGenerations)
resultsBCollapsed = numpy.zeros(c.numberOfGenerations)

for g in range(c.numberOfGenerations):
    resultsACollapsed[g] = numpy.mean(resultsA[:, g])
    resultsA2Collapsed[g] = numpy.mean(resultsA2[:, g])
    resultsBCollapsed[g] = numpy.mean(resultsB[:, g])

#plotA = plt.plot(resultsACollapsed, linewidth=4, label='CPG 10 Fitness Values', color='blue')
plotA = plt.plot(resultsA[:,5], linewidth=2, label='No CPG', color='blue')

plotA2 = plt.plot(resultsA2[:,5], linewidth=2, label='CPG 10 Fitness Values 2', color='purple')

#plotB = plt.plot(resultsBCollapsed, linewidth=2, label="CPG 1 Fitness Values", color='orange')
plotB = plt.plot(resultsB[:,5], linewidth=2, label='CPG 1 Fitness Values', color='orange')

plotC = plt.plot(resultsC[:,5], linewidth=2, label='CPG 10 Fitness Values', color='green')

plt.xlabel('Generation')
plt.ylabel('Fitness')

plt.title('A/B CPG Test for Best Values in Population')

plt.legend()
plt.show()
