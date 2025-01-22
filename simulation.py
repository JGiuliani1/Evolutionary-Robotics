import pybullet as p
import time

# create client to connect with pybullet
physicsClient = p.connect(p.GUI)
# hide sidebar
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# read world from box.sdf
p.loadSDF("box.sdf")
# step the physics 1000 times
for i in range(0, 1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

# disconnect pybullet client
p.disconnect()
