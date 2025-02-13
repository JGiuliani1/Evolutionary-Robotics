import matplotlib.pyplot
import numpy

# store numpy data
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegSinValues = numpy.load("data/backLegSinValues.npy")
frontLegSinValues = numpy.load("data/frontLegSinValues.npy")

# plot numpy data
matplotlib.pyplot.plot(backLegSinValues, label="Back Leg", linewidth=3)
matplotlib.pyplot.plot(frontLegSinValues, label="Front Leg")
#matplotlib.pyplot.legend()
matplotlib.pyplot.show()