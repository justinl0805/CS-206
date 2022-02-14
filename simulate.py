import numpy as np
import pybullet as p
import pybullet_data
import numpy
import time
import pyrosim.pyrosim as pyrosim
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

MAX_ITERATIONS = 1000

amplitude_BackLeg = np.pi / 2
frequency_BackLeg = 10
phaseOffset_BackLeg = 0

amplitude_FrontLeg = np.pi / 4
frequency_FrontLeg = 20
phaseOffset_FrontLeg = np.pi / 8

backLegSensorValues = numpy.zeros(MAX_ITERATIONS)
frontLegSensorValues = numpy.zeros(MAX_ITERATIONS)
# targetAngles = np.sin(np.linspace(0, 2 * np.pi, MAX_ITERATIONS)) * amplitude

targetAngles = numpy.linspace(-numpy.pi, numpy.pi, MAX_ITERATIONS)
targetAnglesBack = numpy.zeros(MAX_ITERATIONS)
targetAnglesFront = numpy.zeros(MAX_ITERATIONS)

for i in range(MAX_ITERATIONS):
    targetAnglesBack[i] = amplitude_BackLeg * np.sin(frequency_BackLeg * targetAngles[i] + phaseOffset_BackLeg)
    targetAnglesFront[i] = amplitude_FrontLeg * np.sin(frequency_FrontLeg * targetAngles[i] + phaseOffset_FrontLeg)

np.save("data/targetAnglesFront", targetAnglesFront)
np.save("data/targetAnglesBack", targetAnglesBack)

for x in range(MAX_ITERATIONS):
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
    # print(x)
    time.sleep(1 / 60)

p.disconnect()

# np.save("data/targetAngles", targetAngles)
# np.save("data/backLegSensorValues", backLegSensorValues)
# np.save("data/frontLegSensorValues", frontLegSensorValues)

# print(backLegSensorValues)
