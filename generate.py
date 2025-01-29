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

    # link 0
    pyrosim.Send_Cube(name="Link0", pos=[0,0,.5] , size=[1,1,1])
    # joint to connect links 0 and 1
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0,0,1])
    # link1
    pyrosim.Send_Cube(name="Link1", pos=[0,0,.5], size=[1,1,1])
    # joint to connect links 1 and 2
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0,0,1])
    # link 2
    pyrosim.Send_Cube(name="Link2", pos=[0,0,.5], size=[1,1,1])
    # joint to connect links 2 and 3
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0,.5,.5])
    # link 3
    pyrosim.Send_Cube(name="Link3", pos=[0,.5,0], size=[1,1,1])
    # joint to connect links 3 and 4
    pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0,1,0])
    # link 4
    pyrosim.Send_Cube(name="Link4", pos=[0,.5,0], size=[1,1,1])
    # joint to connect links 4 and 5
    pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0,.5,-.5])
    # link 5
    pyrosim.Send_Cube(name="Link5", pos=[0,0,-.5], size=[1,1,1])
    # joint to connect links 5 and 6
    pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0,0,-1])
    # link 6
    pyrosim.Send_Cube(name="Link6", pos=[0,0,-.5], size=[1,1,1])


    pyrosim.End()


main()