import pybullet as p
import pybullet_data
import time
import random

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
plane = p.loadURDF("plane.urdf")

blocks = [p.loadURDF("cube_small.urdf", [0, 0, 0.3 + i * 0.1]) for i in range(6)]
force_slider = p.addUserDebugParameter("Force Amount", 0, 50, 5)

while p.isConnected():
    F = p.readUserDebugParameter(force_slider)
    for block in blocks:
        fx = random.uniform(-F, F)
        fy = random.uniform(-F, F)
        p.applyExternalForce(block, -1, [fx, fy, 0], [0, 0, 0], p.WORLD_FRAME)

    p.addUserDebugText(
        f"Random Force: {F:.1f}",
        [0, 0, 0.5],
        textColorRGB=[0, 0, 1],
        textSize=1.3,
        lifeTime=0.1,
    )
    p.stepSimulation()
    time.sleep(1 / 240)
