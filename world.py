import os
import pybullet as p

class WORLD:

    def __init__(self, solutionID):
        # set floor
        self.planeID = p.loadURDF("plane.urdf")
        self.solutionID = solutionID
        # read world from box.sdf
        worldFile = "world" + str(self.solutionID) + ".sdf"
        p.loadSDF(worldFile)
        os.system("del " + worldFile)