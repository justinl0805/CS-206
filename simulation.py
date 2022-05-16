import time

import numpy
import numpy as np
import pybullet as p
import pybullet_data

import constants as c
import pyrosim.pyrosim
from robot import ROBOT
from world import WORLD


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        self.solutionID = solutionID

        self.backLegValues = np.zeros(c.MAX_ITERATIONS)
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

        p.setGravity(0, 0, -9.8)

    def Run(self):
        for x in range(c.MAX_ITERATIONS):
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(x, p)

            if self.directOrGUI == "GUI":
                time.sleep(1 / 480)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
