
# PyBullet Tutorials

This repository contains beginner-friendly PyBullet physics simulation examples. The tutorials are organized into two main folders:

- **Basics/**: Standalone PyBullet examples demonstrating core simulation concepts.
- **PyBullet-ROS2/**: Source files used in the ROS 2 + PyBullet tutorial.

---

## Repository Structure

```text
PyBullet-Tutorials/
│
├── Basics/
│   ├── 01_falling_objects.py
│   ├── 02_robot_arm_control.py
│   ├── 03_interactive_forces.py
│   ├── 04_camera_sensor.py
│   └── README.md
│
├── PyBullet-ROS2/
│   ├── pybullet_ros2/
│   │   ├── __init__.py
│   │   └── sim_node.py
│   └── setup.py
│
└── README.md
```

---

## Basics Folder

The **Basics/** folder contains standalone PyBullet examples.

### 01_falling_objects.py

* Demonstrates basic object dynamics with gravity.
* Loads a plane, a robot model (R2D2), and a sphere.
* Runs a continuous simulation with objects falling and colliding.

### 02_robot_arm_control.py

* Demonstrates controlling a KUKA robotic arm.
* Adds sliders for each joint to manually set joint positions.

### 03_interactive_forces.py

* Demonstrates applying random external forces to cubes.
* Users can adjust force magnitude via a slider.

### 04_camera_sensor.py

* Demonstrates camera control and visualization in PyBullet.
* Renders images from the camera perspective.

---

## PyBullet-ROS2 Folder

The **PyBullet-ROS2/** folder contains the source files used in the ROS 2 + PyBullet tutorial.

⚠️ **Important:** These files are not meant to be run directly from this repository.

You should:

1. Create your own ROS 2 workspace.
2. Create a new ROS 2 Python package.
3. Copy the provided files into your package.
4. Build the workspace using `colcon`.

Example package creation:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

ros2 pkg create \
--build-type ament_python \
pybullet_ros2
```
Then copy the files from the `PyBullet-ROS2/` folder into your newly created package.

Build and run:

```bash
cd ~/ros2_ws

colcon build

source install/setup.bash

ros2 run pybullet_ros2 sim_node
```

Features demonstrated:

* ROS 2 publishers and subscribers
* `/cmd_vel` robot control
* PyBullet simulation as a ROS 2 node
* Mobile robot simulation
* Integration between ROS 2 and PyBullet

---

## Requirements

* Python 3.8+
* PyBullet
* `pybullet_data` (included with PyBullet)

For ROS 2 examples:

* ROS 2 (Humble/Jazzy or compatible)
* `rclpy`
* `geometry_msgs`

Install PyBullet:

```bash
pip install pybullet
```

---

## Usage

Run a basic tutorial:

```bash
cd Basics
python 01_falling_objects.py
```

---

## Notes

* All simulations run at approximately 240 Hz.
* Most examples use continuous loops. Press `Ctrl+C` to exit.
* URDF models are loaded from `pybullet_data`.

Happy simulating! 🚀
