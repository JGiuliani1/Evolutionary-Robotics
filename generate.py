import pyrosim.pyrosim as pyrosim

def main():
    Create_World()

def Create_World():
    # create file to information about link
    pyrosim.Start_SDF("world.sdf")
    # store box size and position
    length = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = .5

    # generate box at origin
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    # end program and close sdf file
    pyrosim.End()

main()