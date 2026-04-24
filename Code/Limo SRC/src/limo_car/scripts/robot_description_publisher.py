#!/usr/bin/env python3

import subprocess
import time

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy
from std_msgs.msg import String


class RobotDescriptionPublisher(Node):
    def __init__(self):
        super().__init__('robot_description_publisher')

        self.declare_parameter('xacro_file', '')
        xacro_file = self.get_parameter('xacro_file').get_parameter_value().string_value

        if not xacro_file:
            raise RuntimeError("xacro_file parameter is empty")

        xml = subprocess.check_output(['xacro', xacro_file]).decode('utf-8')

        qos = QoSProfile(depth=1)
        qos.durability = DurabilityPolicy.TRANSIENT_LOCAL
        qos.reliability = ReliabilityPolicy.RELIABLE

        self.pub = self.create_publisher(String, 'robot_description', qos)

        msg = String()
        msg.data = xml

        # Publish a few times in case the spawner starts slightly later
        for _ in range(10):
            self.pub.publish(msg)
            time.sleep(0.2)

        self.get_logger().info("Published robot_description")
        rclpy.shutdown()


def main():
    rclpy.init()
    node = RobotDescriptionPublisher()


if __name__ == '__main__':
    main()