import constants as c
import numpy as np
import pybullet as p
import pybullet_data
from robot import ROBOT
import time
from world import WORLD

class SIMULATION:

    def __init__(self):
        # create client to connect with pybullet
        self.physicsClient = p.connect(p.GUI)
        # path for pybullet_data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # add gravity
        p.setGravity(0,0,c.FORCE_GRAVITY)
        self.world = WORLD()
        self.robot = ROBOT()


    def __del__(self):
        #self.Save_Values()
        p.disconnect()

    
    def Run(self):
        # step the physics NUM_ITERATIONS times
        for step in range(0, c.NUM_ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(step)
            self.robot.Think()
            self.robot.Act(step)
            time.sleep(c.SLEEP_TIME)

    
    def Save_Values(self):
        for sensor in self.robot.sensors:
            fileName = "data/" + sensor + "SensorValues.npy"
            np.save(fileName, self.robot.sensors[sensor].values)
            