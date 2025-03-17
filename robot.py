import pybullet as p
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import os

class ROBOT:

    def __init__(self, solutionID):
        # create robot ID
        self.robotID = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotID)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.solutionID = solutionID
        brainFile = "brain" + str(self.solutionID) + ".nndf"
        self.nn = NEURAL_NETWORK(brainFile)
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
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle, self.robotID)


    def Think(self):
        self.nn.Update()


    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        tempFile = "tmp" + str(self.solutionID) + ".txt"
        fitnessFile = "fitness" + str(self.solutionID) + ".txt"
        file = open(tempFile, "w")
        file.write(str(xCoordinateOfLinkZero))
        file.close()
        os.system("rename " + tempFile + " " + fitnessFile)
        exit()