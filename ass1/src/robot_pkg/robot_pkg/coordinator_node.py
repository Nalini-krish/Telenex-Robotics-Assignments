# robot_pkg/coordinator_node.py
import rclpy
from rclpy.node import Node
from custom_interfaces.msg import Telemetry

class CoordinatorNode(Node):
    def __init__(self):
        super().__init__('coordinator_node')
        self.subscription = self.create_subscription(
            Telemetry,
            'robot_telemetry',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info(f'Received data: Robot Battery: {msg.battery_level}, Position: ({msg.x_coordinate}, {msg.y_coordinate}), Status: {msg.task_status}')

def main(args=None):
    rclpy.init(args=args)
    coordinator_node = CoordinatorNode()
    rclpy.spin(coordinator_node)
    coordinator_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

