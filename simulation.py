import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

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
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
# step the physics 10000 times
for i in range(0, 1000):
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
        targetPosition = -3.141519/4.0,
        maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = 3.141519/4.0,
        maxForce = 500)
    
# store numpy data
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# disconnect pybullet client
p.disconnect()