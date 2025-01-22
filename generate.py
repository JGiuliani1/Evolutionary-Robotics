import pyrosim.pyrosim as pyrosim

# create file to information about link
pyrosim.Start_SDF("boxes.sdf")
# store box size and position
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5

# create 10 boxes stacked ontop of one another
for i in range(0, 10):
    pyrosim.Send_Cube(name="Box", pos=[x,y,z+i] , size=[length,width,height])
    length = length * .9
    width = width * .9
    height = height * .9
# end program and close sdf file
pyrosim.End()