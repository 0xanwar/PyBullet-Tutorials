import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

plane = p.loadURDF("plane.urdf")
box = p.loadURDF("r2d2.urdf", [0, 0, 1])
sphere = p.loadURDF("sphere2.urdf", [0.5, 0, 2])

while True:
    p.stepSimulation()
    time.sleep(1 / 240)
