import pyrosim.pyrosim as pyrosim


def Create_World():
    pyrosim.Start_SDF("world.sdf")

    x = -2
    y = 0.5
    z = 3

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Box", pos=[x, z, y], size=[length, width, height])
    pyrosim.End()


def Create_Robot():
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


Create_World()
Create_Robot()

'''
for k in range(0, 5):
    x_offset = 1.1 * k
    for j in range(0, 5):
        z_offset = 1.1 * j

        stored = 1
        for i in range(0, 10):
            y_offset = 1.1 * i

            x = 0 + x_offset
            y = 0.5 + y_offset
            z = 0 + z_offset

            stored = stored * 0.9

            length = stored
            width = stored
            height = stored

            pyrosim.Send_Cube(name="Box2", pos=[z, x, y], size=[length, width, height])'''

'''x = 1
y = 0
z = 1.5

length = 1
width = 1
height = 1

pyrosim.Send_Cube(name="Box2", pos=[x, y, z], size=[length, width, height])
'''
