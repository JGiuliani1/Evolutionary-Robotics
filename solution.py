import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

class SOLUTION:
    def __init__(self, myID):
        self.weights = np.random.rand(3, 2)
        self.weights = self.weights * 2 - 1
        self.myID = myID
    

    def Evaluate(self, directOrGUI):
        pass
    

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))


    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        file = open(fitnessFile, "r")
        self.fitness = float(file.read())
        file.close()
        os.system("del " + fitnessFile)
    

    def Create_World(self):
        # create file to information about link
        pyrosim.Start_SDF("world.sdf")

        # generate box
        pyrosim.Send_Cube(name="Box", pos=[-2,-2,.5] , size=[1,1,1])

        # end program and close sdf file
        pyrosim.End()


    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")

        # torso
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[1,1,1])
        # joint to connect torso to back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1,0,1])
        # back leg
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5])
        # joint to connect torso to front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2,0,1])
        # front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5])

        pyrosim.End()


    def Generate_Brain(self):
        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)

        # sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        # motor neurons
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        # synapses
        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + 3 , weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()
    

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1


    def Set_ID(self, newID):
        self.myID = newID