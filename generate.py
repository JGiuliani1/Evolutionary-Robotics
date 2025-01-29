import pyrosim.pyrosim as pyrosim


def main():
    Create_World()
    Create_Robot()


def Create_World():
    # create file to information about link
    pyrosim.Start_SDF("world.sdf")

    # generate box
    pyrosim.Send_Cube(name="Box", pos=[-2,-2,.5] , size=[1,1,1])

    # end program and close sdf file
    pyrosim.End()


def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    # generate torso
    pyrosim.Send_Cube(name="Torso", pos=[0,0,.5] , size=[1,1,1])
    # joint to connect leg and torso
    pyrosim.Send_Joint(name="Torso_Leg", parent="Torso", child="Leg", type="revolute", position=[0,0,1])
    # generate leg
    pyrosim.Send_Cube(name="Leg", pos=[0,0,.5], size=[1,1,1])


    pyrosim.End()


main()