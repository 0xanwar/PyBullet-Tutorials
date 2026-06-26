import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

plane = p.loadURDF("plane.urdf")
robot = p.loadURDF("r2d2.urdf", [0, 0, 1])

yaw_slider = p.addUserDebugParameter("Camera Yaw", -180, 180, 45)
pitch_slider = p.addUserDebugParameter("Camera Pitch", -89, 89, -30)
dist_slider = p.addUserDebugParameter("Camera Distance", 0.3, 3.0, 1.2)

while p.isConnected():
    yaw = p.readUserDebugParameter(yaw_slider)
    pitch = p.readUserDebugParameter(pitch_slider)
    dist = p.readUserDebugParameter(dist_slider)

    view_matrix = p.computeViewMatrixFromYawPitchRoll(
        cameraTargetPosition=[0, 0, 0.5],
        distance=dist,
        yaw=yaw,
        pitch=pitch,
        roll=0,
        upAxisIndex=2,
    )

    proj_matrix = p.computeProjectionMatrixFOV(
        fov=60, aspect=1.0, nearVal=0.1, farVal=3.0
    )

    p.getCameraImage(320, 320, view_matrix, proj_matrix)

    p.addUserDebugText(
        f"Yaw: {yaw:.1f}, Pitch: {pitch:.1f}, Dist: {dist:.2f}",
        [0, 0, 1.7],
        textColorRGB=[1, 1, 0],
        textSize=1.2,
        lifeTime=0.1,
    )

    p.stepSimulation()
    time.sleep(1 / 240)
