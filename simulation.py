import time

import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0, 0, -9.8)

    def Run(self):
        for x in range(c.MAX_ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x, p)

            time.sleep(1 / 60)

    def __del__(self):
        p.disconnect()
