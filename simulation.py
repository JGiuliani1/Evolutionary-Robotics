import pybullet as p
import pybullet_data
import time

# create client to connect with pybullet
physicsClient = p.connect(p.GUI)
# path for pybullet_data
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# hide sidebar
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# add gravity
p.setGravity(0,0,-9.8)
# set floor
planeID = p.loadURDF("plane.urdf")
# create robot ID
robotID = p.loadURDF("body.urdf")
# read world from box.sdf
p.loadSDF("world.sdf")
# step the physics 1000 times
for i in range(0, 2000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

# disconnect pybullet client
p.disconnect()
