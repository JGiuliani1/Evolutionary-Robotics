import numpy
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

NUM_ITERATIONS = 1000

# create client to connect with pybullet
physicsClient = p.connect(p.GUI)
# path for pybullet_data
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# hide sidebar
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# variables to modify oscillation values
frontAmplitude = numpy.pi/4
frontFrequency = 10
frontPhaseOffset = 0
backAmplitude = numpy.pi/4
backFrequency = 30
backPhaseOffset = numpy.pi

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
# create sin values for motors
input_array = numpy.linspace(0, 2*numpy.pi, NUM_ITERATIONS)
frontTargetAngles = frontAmplitude*numpy.sin(frontFrequency * input_array + frontPhaseOffset)
backTargetAngles = backAmplitude*numpy.sin(backFrequency* input_array + backPhaseOffset)
# step the physics NUM_ITERATIONS times
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
        targetPosition = frontTargetAngles[i],
        maxForce = 25)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotID,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = backTargetAngles[i],
        maxForce = 25)
    
# disconnect pybullet client
p.disconnect()