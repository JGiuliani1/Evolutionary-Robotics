import pyrosim.pyrosim as pyrosim

# create file to information about link
pyrosim.Start_SDF("box.sdf")
# store box size and position
length = 1
width = 2
height = 3
x = 0
y = 0
z = 1.5
pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# end program and close sdf file
pyrosim.End()