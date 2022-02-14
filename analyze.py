import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")
targetAnglesFront = numpy.load("data/targetAnglesFront.npy")
targetAnglesBack = numpy.load("data/targetAnglesBack.npy")

matplotlib.pyplot.plot(targetAnglesFront, label='Front Leg')
matplotlib.pyplot.plot(targetAnglesBack, label='Back Leg')

# matplotlib.pyplot.plot(backLegSensorValues, linewidth=4, label='Back Leg')
# matplotlib.pyplot.plot(frontLegSensorValues, label='Front Leg')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
print(backLegSensorValues)
