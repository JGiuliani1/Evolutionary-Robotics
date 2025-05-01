import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

class SOLUTION:
    def __init__(self, myID):
        self.weights = np.random.rand(c.NUM_SENSOR_NEURONS, c.NUM_MOTOR_NEURONS)
        self.weights = self.weights * 2 - 1
        self.myID = myID
    

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " 2>&1 &")


    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"
        while True:
            if os.path.exists(fitnessFile):
                try:
                    file = open(fitnessFile, "r")
                    self.fitness = float(file.read())
                    file.close()
                    os.system("del " + fitnessFile)
                    break
                except PermissionError:
                    time.sleep(0.01)
            else:
                time.sleep(0.01)
    

    def Create_World(self):
        # create file to information about link
        worldFile = "world" + str(self.myID) + ".sdf"
        pyrosim.Start_SDF(worldFile)

        # end program and close sdf file
        pyrosim.End()


    def Generate_Body(self):
        bodyFile = "body" + str(self.myID) + ".urdf"
        pyrosim.Start_URDF(bodyFile)

        # torso
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,1,1])
        
        # joint to connect torso to back leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0,-0.5,1], jointAxis="1 0 0")
        # back leg
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0], size=[0.2,1,0.2])
        # joint to connect back leg to lower back leg
        pyrosim.Send_Joint("BackLeg_LowerBackLeg", parent="BackLeg", child="LowerBackLeg", type="revolute", position=[0,-1,0], jointAxis="0 1 0")
        # lower back leg
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        
        # joint to connect torso to front leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0,0.5,1], jointAxis="1 0 0")
        # front leg
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0], size=[0.2,1,0.2])
        # joint to connect front leg to lower front leg
        pyrosim.Send_Joint("FrontLeg_LowerFrontLeg", parent="FrontLeg", child="LowerFrontLeg", type="revolute", position=[0,1,0], jointAxis="0 1 0")
        # lower front leg
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])
        
        # joint to connect torso to left leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5,0,1], jointAxis="0 1 0")
        # left leg
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0], size=[1,0.2,0.2])
        # joint to connect left leg to lower left leg
        pyrosim.Send_Joint("LeftLeg_LowerLeftLeg", parent="LeftLeg", child="LowerLeftLeg", type="revolute", position=[-1,0,0], jointAxis="0 1 0")
        # lower left leg
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

        # joint to connect torso to right leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5,0,1], jointAxis="0 1 0")
        # right leg
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0], size=[1,0.2,0.2])
        # joint to connect right leg to lower right leg
        pyrosim.Send_Joint("RightLeg_LowerRightLeg", parent="RightLeg", child="LowerRightLeg", type="revolute", position=[1,0,0], jointAxis="0 1 0")
        # lower right leg
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[0,0,-0.5], size=[0.2,0.2,1])

        pyrosim.End()


    def Generate_Brain(self):
        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)

        # sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerRightLeg")

        # motor neurons
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_LowerRightLeg")

        # synapses
        for currentRow in range(0, c.NUM_SENSOR_NEURONS):
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.NUM_SENSOR_NEURONS , weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()
    

    def Mutate(self):
        randomRow = random.randint(0, c.NUM_SENSOR_NEURONS - 1)
        randomColumn = random.randint(0, c.NUM_MOTOR_NEURONS - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1


    def Set_ID(self, newID):
        self.myID = newID