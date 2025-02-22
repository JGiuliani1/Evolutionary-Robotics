import constants as c
import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.PHASE_OFFSET
        input_array = np.linspace(c.INPUT_ARRAY_LOWER, c.INPUT_ARRAY_UPPER, c.NUM_ITERATIONS)
        self.motorValues = self.amplitude*np.sin(self.frequency * input_array + self.offset)


    def Set_Value(self, step, robot):
        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = self.motorValues[step],
                maxForce = c.MAX_MOTOR_FORCE)