import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

plane = p.loadURDF("plane.urdf")
robot = p.loadURDF("kuka_iiwa/model.urdf", useFixedBase=True)

joint_sliders = []
for i in range(p.getNumJoints(robot)):
    joint_sliders.append(p.addUserDebugParameter(f"Joint {i}", -3.14, 3.14, 0))

while p.isConnected():
    for i in range(p.getNumJoints(robot)):
        target = p.readUserDebugParameter(joint_sliders[i])
        p.setJointMotorControl2(robot, i, p.POSITION_CONTROL, targetPosition=target)

    p.addUserDebugText(
        "Control the robot joints using the right panel",
        [0, 0, 1.5],
        textColorRGB=[1, 0, 0],
        textSize=1.5,
        lifeTime=0.1,
    )
    p.stepSimulation()
    time.sleep(1 / 240)
