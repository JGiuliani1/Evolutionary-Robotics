import pybullet as p

class WORLD:

    def __init__(self):
        # set floor
        self.planeID = p.loadURDF("plane.urdf")
        # read world from box.sdf
        p.loadSDF("world.sdf")