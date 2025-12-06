
# PyBullet Tutorials

This repository contains beginner-friendly PyBullet physics simulation examples. Each script demonstrates a different aspect of the PyBullet engine, from basic object simulation to interactive controls and camera manipulation.

---

## Files

### 01_falling_objects.py
- Demonstrates basic object dynamics with gravity.
- Loads a plane, a robot model (R2D2), and a sphere.
- Runs a continuous simulation with objects falling and colliding.
- Key functions: `p.loadURDF()`, `p.setGravity()`, `p.stepSimulation()`.

### 02_robot_arm_control.py
- Demonstrates controlling a KUKA robotic arm.
- Adds sliders for each joint to manually set joint positions.
- Displays on-screen instructions for control.
- Key functions: `p.setJointMotorControl2()`, `p.addUserDebugParameter()`, `p.addUserDebugText()`.

### 03_interactive_forces.py
- Demonstrates applying random external forces to cubes.
- Users can adjust force magnitude via a slider.
- Visual feedback shows current force.
- Key functions: `p.applyExternalForce()`, `random.uniform()`, `p.readUserDebugParameter()`.

### 04_camera_sensor.py
- Demonstrates camera control and visualization in PyBullet.
- Adds sliders to adjust camera yaw, pitch, and distance.
- Renders images from the camera perspective.
- Key functions: `p.computeViewMatrixFromYawPitchRoll()`, `p.computeProjectionMatrixFOV()`, `p.getCameraImage()`.

---

## Requirements

- Python 3.8+
- PyBullet
- pybullet_data (comes with PyBullet)
  
Install PyBullet with:
```bash
pip install pybullet
````

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/0xanwar/PyBullet-Tutorials.git
cd PyBullet-Tutorials
```

2. Run any tutorial:

```bash
python 01_falling_objects.py
```

3. Use sliders or interact with the GUI as instructed for each tutorial.

---

## Notes

* All simulations run at ~240 Hz.
* Infinite loops are used in most scripts for continuous simulation. Use `Ctrl+C` in terminal to exit.
* URDF files are loaded from `pybullet_data`.


Happy simulating!
