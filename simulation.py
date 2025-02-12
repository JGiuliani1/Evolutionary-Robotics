import math
import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import random
import time

NUM_ITERATIONS = 1000

# create client to connect with pybullet
physicsClient = p.connect(p.GUI)
# path for pybullet_data
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# hide sidebar
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# add gravity
p.setGravity(0,0,-9.8)
# set floor
planeID = p.loadURDF("plane.urdf")
# create robot ID
robotID = p.loadURDF("body.urdf")
# read world from box.sdf
p.loadSDF("world.sdf")
# prepare sensor
pyrosim.Prepare_To_Simulate(robotID)
# prepare numpy arrays
backLegSensorValues = numpy.zeros(NUM_ITERATIONS)
frontLegSensorValues = numpy.zeros(NUM_ITERATIONS)
#
input_array = numpy.linspace(0, 2*numpy.pi, NUM_ITERATIONS)
targetAngles = numpy.sin(input_array)
numpy.save("data/sinValues.npy", targetAngles)
exit()
# step the physics 10000 times
for i in range(0, NUM_ITERATIONS):
    p.stepSimulation()
    time.sleep(1/60)
    # touch sensor for back and front legs
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # motor for joint
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.triangular(-(math.pi/2.0), math.pi/2.0),
        maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.triangular(-(math.pi/2.0), math.pi/2.0),
        maxForce = 25)
    
# store numpy data
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# disconnect pybullet client
p.disconnect()