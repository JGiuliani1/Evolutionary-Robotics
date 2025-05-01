import constants as c
import numpy as np
import os
import pyrosim.pyrosim as pyrosim
import random
import time

class SOLUTION_HEX:
    def __init__(self, myID):
        self.weights = np.random.rand(c.NUM_SENSOR_NEURONS_HEX, c.NUM_MOTOR_NEURONS_HEX)
        self.weights = self.weights * 2 - 1
        self.myID = myID
    

    def Start_Simulation(self, directOrGUI, save):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " " + str(save) + " 2>&1 &")


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
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[1,2,1])
        
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
        
        # joint to connect torso to left leg 1
        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[-.5,-.3,1], jointAxis="0 1 0")
        # left leg 1
        pyrosim.Send_Cube(name="LeftLeg1", pos=[-.5,-.3,0], size=[1,0.2,0.2])
        # joint to connect left leg 1 to lower left leg 1
        pyrosim.Send_Joint("LeftLeg1_LowerLeftLeg1", parent="LeftLeg1", child="LowerLeftLeg1", type="revolute", position=[-1,0,0], jointAxis="0 1 0")
        # lower left leg 1
        pyrosim.Send_Cube(name="LowerLeftLeg1", pos=[0,-.3,-0.5], size=[0.2,0.2,1])

        # joint to connect torso to left leg 2
        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[-.5,.3,1], jointAxis="0 1 0")
        # left leg 2
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-.5,.3,0], size=[1,0.2,0.2])
        # joint to connect left leg 2 to lower left leg 2
        pyrosim.Send_Joint("LeftLeg2_LowerLeftLeg2", parent="LeftLeg2", child="LowerLeftLeg2", type="revolute", position=[-1,0,0], jointAxis="0 1 0")
        # lower left leg 2
        pyrosim.Send_Cube(name="LowerLeftLeg2", pos=[0,.3,-0.5], size=[0.2,0.2,1])

        # joint to connect torso to right leg 1
        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[.5,-.3,1], jointAxis="0 1 0")
        # right leg 1
        pyrosim.Send_Cube(name="RightLeg1", pos=[.5,-.3,0], size=[1,0.2,0.2])
        # joint to connect right leg 1 to lower right leg 1
        pyrosim.Send_Joint("RightLeg1_LowerRightLeg1", parent="RightLeg1", child="LowerRightLeg1", type="revolute", position=[1,0,0], jointAxis="0 1 0")
        # lower right leg 1
        pyrosim.Send_Cube(name="LowerRightLeg1", pos=[0,-.3,-0.5], size=[0.2,0.2,1])

        # joint to connect torso to right leg 2
        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[.5,.3,1], jointAxis="0 1 0")
        # right leg 2
        pyrosim.Send_Cube(name="RightLeg2", pos=[.5,.3,0], size=[1,0.2,0.2])
        # joint to connect right leg 2 to lower right leg 2
        pyrosim.Send_Joint("RightLeg2_LowerRightLeg2", parent="RightLeg2", child="LowerRightLeg2", type="revolute", position=[1,0,0], jointAxis="0 1 0")
        # lower right leg 2
        pyrosim.Send_Cube(name="LowerRightLeg2", pos=[0,.3,-0.5], size=[0.2,0.2,1])

        pyrosim.End()


    def Generate_Brain(self):
        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)

        # sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "LowerBackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LowerLeftLeg1")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LowerLeftLeg2")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LowerRightLeg1")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LowerRightLeg2")

        # motor neurons
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_LeftLeg1")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_LeftLeg2")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_RightLeg1")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_RightLeg2")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_LowerBackLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "LeftLeg1_LowerLeftLeg1")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg2_LowerLeftLeg2")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg1_LowerRightLeg1")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "RightLeg2_LowerRightLeg2")

        # synapses
        for currentRow in range(0, c.NUM_SENSOR_NEURONS_HEX):
            for currentColumn in range(0, c.NUM_MOTOR_NEURONS_HEX):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.NUM_SENSOR_NEURONS_HEX , weight = self.weights[currentRow][currentColumn] )
        
        pyrosim.End()
    

    def Mutate(self):
        randomRow = random.randint(0, c.NUM_SENSOR_NEURONS_HEX - 1)
        randomColumn = random.randint(0, c.NUM_MOTOR_NEURONS_HEX - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1


    def Set_ID(self, newID):
        self.myID = newID