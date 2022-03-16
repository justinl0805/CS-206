import random

import numpy as np
import os

from pyrosim import pyrosim


class SOLUTION:
    def __init__(self):
        self.weights = (np.random.rand(3, 2) * 2) - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("python simulate.py " + directOrGUI)

        fitnessFile = "fitness.txt"
        with open("data/" + fitnessFile, "r") as f:
            self.fitness = float(f.read())

    def Mutate(self):
        self.weights[random.randint(0, 2), random.randint(0, 1)] = (random.random() * 2) - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        x = -2
        y = 0.5
        z = 3

        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])

        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(0, 3):
            for currentColumn in range(0, 2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

