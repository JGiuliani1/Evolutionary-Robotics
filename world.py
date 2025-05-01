import os
import pybullet as p

class WORLD:

    def __init__(self, solutionID, save):
        # set floor
        self.planeID = p.loadURDF("plane.urdf")
        self.solutionID = solutionID
        # read world from box.sdf
        worldFile = "world" + str(self.solutionID) + ".sdf"
        p.loadSDF(worldFile)
        if save == "False":
            os.system("del " + worldFile)