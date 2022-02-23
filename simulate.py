"""import numpy as np
import pybullet as p
import pybullet_data
import numpy
import time
import pyrosim.pyrosim as pyrosim
import constants as c
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(c.MAX_ITERATIONS)
frontLegSensorValues = numpy.zeros(c.MAX_ITERATIONS)

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, c.MAX_ITERATIONS)
targetAnglesBack = numpy.zeros(c.MAX_ITERATIONS)
targetAnglesFront = numpy.zeros(c.MAX_ITERATIONS)

for i in range(c.MAX_ITERATIONS):
    targetAnglesBack[i] = c.amplitude_BackLeg * np.sin(c.frequency_BackLeg * targetAngles[i] + c.phaseOffset_BackLeg)
    targetAnglesFront[i] = c.amplitude_FrontLeg * np.sin(c.frequency_FrontLeg * targetAngles[i] + c.phaseOffset_FrontLeg)

np.save("data/targetAnglesFront", targetAnglesFront)
np.save("data/targetAnglesBack", targetAnglesBack)

for x in range(c.MAX_ITERATIONS):
    p.stepSimulation()
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesBack[x],
        maxForce=30)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=targetAnglesFront[x],
        maxForce=30)
    time.sleep(1 / 60)

p.disconnect()

# np.save("data/targetAngles", targetAngles)
# np.save("data/backLegSensorValues", backLegSensorValues)
# np.save("data/frontLegSensorValues", frontLegSensorValues)
"""
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()
