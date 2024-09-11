# robotic_arm_node.py
import rclpy
from rclpy.node import Node
from custom_interfaces.msg import ObjectMetadata


class RoboticArmNode(Node):
    def __init__(self):
        super().__init__('robotic_arm_node')
        self.subscription = self.create_subscription(
            ObjectMetadata,
            'object_metadata',
            self.object_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def object_callback(self, msg):
        self.get_logger().info(f'Received Object ID: {msg.id}, Type: {msg.type}')
        if msg.graspable:
            self.get_logger().info(f'Object {msg.id} is graspable.')
        else:
            self.get_logger().info(f'Object {msg.id} is not graspable.')

def main(args=None):
    rclpy.init(args=args)
    node = RoboticArmNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

