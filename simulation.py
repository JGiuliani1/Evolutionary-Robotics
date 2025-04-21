import constants as c
import numpy as np
import pybullet as p
import pybullet_data
from robot import ROBOT
import time
from world import WORLD

class SIMULATION:

    def __init__(self, directOrGUI, solutionID):
        # create client to connect with pybullet
        save = False
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            self.sleepTime = 1/1000
        else:
            self.physicsClient = p.connect(p.GUI)
            self.sleepTime = c.SLEEP_TIME
            save = True
        # path for pybullet_data
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # add gravity
        p.setGravity(0,0,c.FORCE_GRAVITY)
        self.world = WORLD(solutionID, save)
        self.robot = ROBOT(solutionID, save)


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
            self.robot.SaveZ()
            self.robot.SaveX()
            time.sleep(self.sleepTime)

    
    def Save_Values(self):
        for sensor in self.robot.sensors:
            fileName = "data/" + sensor + "SensorValues.npy"
            np.save(fileName, self.robot.sensors[sensor].values)


    # CHANGE HERE FOR A/B TESTING
    def Get_Fitness(self):
        #self.robot.Get_Fitness_A()
        self.robot.Get_Fitness_B()