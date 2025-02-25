import pyrosim.pyrosim as pyrosim


def main():
    Create_World()
    Generate_Body()
    Generate_Brain()


def Create_World():
    # create file to information about link
    pyrosim.Start_SDF("world.sdf")

    # generate box
    pyrosim.Send_Cube(name="Box", pos=[-2,-2,.5] , size=[1,1,1])

    # end program and close sdf file
    pyrosim.End()


def Generate_Body():
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


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # sensor neurons
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

    # motor neurons
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    pyrosim.End()


main()