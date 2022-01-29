import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

'''x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1

pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])'''

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

            pyrosim.Send_Cube(name="Box2", pos=[z, x, y], size=[length, width, height])

'''x = 1
y = 0
z = 1.5

length = 1
width = 1
height = 1

pyrosim.Send_Cube(name="Box2", pos=[x, y, z], size=[length, width, height])
'''

pyrosim.End()

