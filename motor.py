import numpy
import numpy as np

import constants as c
from pyrosim import pyrosim


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        self.motorValues = numpy.ones(c.MAX_ITERATIONS)

        targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.MAX_ITERATIONS)
        for i in range(c.MAX_ITERATIONS):
            if self.jointName == "Torso_Backleg":
                self.motorValues[i] = self.amplitude * np.sin(
                    self.frequency * i / (c.MAX_ITERATIONS / (2 * np.pi)) + self.offset)
            else:
                self.motorValues[i] = self.amplitude * np.sin(
                    self.frequency / 2 * i / (c.MAX_ITERATIONS / (2 * np.pi)) + self.offset)

    def Set_Value(self, t, robotId, p):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.maxForceConst)
