import constants as c
import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import os
import time

class ROBOT:

    def __init__(self, solutionID, save):
        # create robot ID
        self.solutionID = solutionID
        self.z_values = []

        bodyFile = "body" + str(self.solutionID) + ".urdf"
        while not os.path.exists(bodyFile):
            time.sleep(0.01)
        self.robotID = p.loadURDF(bodyFile)
        if save == False:
            os.system("del " + bodyFile)

        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        brainFile = "brain" + str(self.solutionID) + ".nndf"
        while not os.path.exists(brainFile):
            time.sleep(0.01)
        self.nn = NEURAL_NETWORK(brainFile)
        if save == False:
            os.system("del " + brainFile)
    

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    
    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    
    def Sense(self, step):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(step)

    
    def Act(self, step):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Nuerons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.MOTOR_JOINT_RANGE
                self.motors[jointName].Set_Value(desiredAngle, self.robotID)

    
    def SaveZ(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotID)
        basePosition = basePositionAndOrientation[0]
        zPosition = basePosition[2]
        self.z_values.append(zPosition)


    def Think(self):
        self.nn.Update()


    def Get_Fitness(self):
        current_num_steps_in_air = 0
        max_num_steps_in_air = 0
        current_total_z_value = 0
        max_avg_z_value = 0
        for i in range(c.NUM_ITERATIONS):
            if self.sensors["LowerFrontLeg"].values[i] == -1 and self.sensors["LowerBackLeg"].values[i] == -1 and self.sensors["LowerRightLeg"].values[i] == -1 and self.sensors["LowerLeftLeg"].values[i] == -1:
                current_num_steps_in_air += 1
                current_total_z_value += self.z_values[i]
                if current_num_steps_in_air > max_num_steps_in_air:
                    max_num_steps_in_air = current_num_steps_in_air
                if current_total_z_value/current_num_steps_in_air > max_avg_z_value:
                    max_avg_z_value = current_total_z_value/current_num_steps_in_air
            else:
                current_num_steps_in_air = 0
                current_total_z_value = 0

        #fitness_value = max_num_steps_in_air * max_avg_z_value # normal fitness
        fitness_value = str(max_num_steps_in_air) + ", " + str(max_avg_z_value) # MOO
        tempFile = "tmp" + str(self.solutionID) + ".txt"
        fitnessFile = "fitness" + str(self.solutionID) + ".txt"
        file = open(tempFile, "w")
        file.write(str(fitness_value))
        file.close()
        os.system("rename " + tempFile + " " + fitnessFile)
        exit()