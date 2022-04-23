import random
import time

import constants as c
import numpy as np
import os

from pyrosim import pyrosim


class SOLUTION:
    def __init__(self, myID):
        self.weights = (np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2) - 1
        self.myID = myID

    def Evaluate(self, directOrGUI):
        pass

    def Mutate(self):
        self.weights[random.randint(0, c.numMotorNeurons), random.randint(0, 1)] = (
                                                                                               random.random() * c.numMotorNeurons) - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        x = 0
        y = 1.5
        z = 0

        length = 30
        width = 3.5
        height = 3

        # pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        length = 1
        width = 1
        height = 1

        # Add to the initial joint around the torso to move the robot's limbs along the position
        # Torso
        z_position_offset = 0

        length_increase = .2#.5
        width_increase = .5#.5

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1 + z_position_offset], size=[length, width, height])

        # Back Leg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso",
                           child="BackLeg", type="revolute",
                           position=[0, -0.5, 1 + z_position_offset], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # Back Lower Leg
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg",
                           child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[length_increase, width_increase, 1])

        # Front Leg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso",
                           child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1 + z_position_offset], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # Front Lower Leg
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg",
                           child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")

        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[length_increase, width_increase, 1])

        # Left Leg
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso",
                           child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1 + z_position_offset], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # Left Lower Leg (FRONT)
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg",
                           child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -.2], size=[.2, .2, 0.6])

        # Right Leg
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso",
                           child="RightLeg", type="revolute",
                           position=[0.5, 0, 1 + z_position_offset], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1.0, 0.2, 0.2])

        # Right Lower Leg (BACK)
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg",
                           child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")

        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -.3], size=[.6, .6, 2])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_RightLowerLeg")

        for currentRow in range(0, c.numSensorNeurons):
            for currentColumn in range(0, c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFile = "fitness" + str(self.myID) + ".txt"

        while not os.path.exists(fitnessFile):
            time.sleep(0.01)

        with open(fitnessFile, "r") as f:
            self.fitness = float(f.read())

        os.system("del fitness" + str(self.myID) + ".txt")
