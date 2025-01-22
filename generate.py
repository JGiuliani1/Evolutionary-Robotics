import pyrosim.pyrosim as pyrosim

# create file to store information about world
pyrosim.Start_SDF("box.sdf")
# store box position
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
# end simulation and close sdf file
pyrosim.End()