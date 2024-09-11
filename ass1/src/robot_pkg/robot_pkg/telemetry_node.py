import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Telemetry
import random

class RobotNode(Node):
    def __init__(self, robot_id):
        super().__init__('robot_node_' + str(robot_id))
        self.publisher_ = self.create_publisher(Telemetry, 'robot_telemetry', 10)
        self.timer = self.create_timer(1.0, self.publish_telemetry)
        self.robot_id = robot_id
        self.battery_level = random.uniform(50.0, 100.0)
        self.x = random.uniform(0.0, 100.0)
        self.y = random.uniform(0.0, 100.0)
        self.task_status = "idle"

    def publish_telemetry(self):
        msg = Telemetry()
        msg.battery_level = self.battery_level
        msg.x_coordinate = self.x
        msg.y_coordinate = self.y
        msg.task_status = self.task_status
        self.publisher_.publish(msg)
        self.get_logger().info(f'Robot {self.robot_id} published telemetry data')

def main(args=None):
    rclpy.init(args=args)
    robot_id = 1  # Unique identifier for the robot
    robot_node = RobotNode(robot_id)
    rclpy.spin(robot_node)
    robot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

