#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

import pybullet as p
import pybullet_data


class PyBulletSim(Node):

    def __init__(self):

        super().__init__('pybullet_sim')

        # Start PyBullet GUI
        p.connect(p.GUI)

        # Add default PyBullet models path
        p.setAdditionalSearchPath(
            pybullet_data.getDataPath()
        )

        # Set gravity
        p.setGravity(0, 0, -9.81)

        # Load the ground plane
        p.loadURDF("plane.urdf")

        # Load Husky robot
        self.robot = p.loadURDF(
            "husky/husky.urdf",
            [0, 0, 0.1]
        )

        # Store the latest command
        self.linear_x = 0.0
        self.angular_z = 0.0

        # Subscribe to /cmd_vel
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        # Timer for simulation updates
        self.timer = self.create_timer(
            1.0 / 240.0,
            self.update_sim
        )

        self.get_logger().info(
            "Simulation Started"
        )

        # Print all joints once (optional for debugging)
        for i in range(p.getNumJoints(self.robot)):
            self.get_logger().info(
                str(p.getJointInfo(self.robot, i))
            )

    def cmd_callback(self, msg):

        self.linear_x = msg.linear.x
        self.angular_z = msg.angular.z

        self.get_logger().info(
            f"Received: linear={self.linear_x}, angular={self.angular_z}"
        )

    def update_sim(self):

        # Differential drive equations
        left_speed = self.linear_x - self.angular_z
        right_speed = self.linear_x + self.angular_z

        # Left wheels
        p.setJointMotorControlArray(
            bodyUniqueId=self.robot,
            jointIndices=[2, 4],
            controlMode=p.VELOCITY_CONTROL,
            targetVelocities=[left_speed, left_speed],
            forces=[100, 100]
        )

        # Right wheels
        p.setJointMotorControlArray(
            bodyUniqueId=self.robot,
            jointIndices=[3, 5],
            controlMode=p.VELOCITY_CONTROL,
            targetVelocities=[right_speed, right_speed],
            forces=[100, 100]
        )

        p.stepSimulation()


def main(args=None):

    rclpy.init(args=args)

    node = PyBulletSim()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()