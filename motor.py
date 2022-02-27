import numpy
import numpy as np

import constants as c
from pyrosim import pyrosim


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robotId, p):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForceConst)
