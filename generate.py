import pyrosim.pyrosim as pyrosim

# create file to information about link
pyrosim.Start_SDF("box.sdf")
# store box size and position
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
# end program and close sdf file
pyrosim.End()