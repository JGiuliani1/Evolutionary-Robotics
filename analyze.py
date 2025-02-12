import matplotlib.pyplot
import numpy

# store numpy data
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
sinValues = numpy.load("data/sinValues.npy")

# plot numpy data
'''matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()'''
matplotlib.pyplot.plot(sinValues)
matplotlib.pyplot.show()