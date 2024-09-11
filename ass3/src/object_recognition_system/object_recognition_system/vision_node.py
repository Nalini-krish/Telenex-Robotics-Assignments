# vision_node.py
import rclpy
from rclpy.node import Node
from custom_interfaces.msg import ObjectMetadata

import random

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')
        self.publisher_ = self.create_publisher(ObjectMetadata, 'object_metadata', 10)
        self.timer = self.create_timer(1.0, self.publish_object_data)

    def publish_object_data(self):
        msg = ObjectMetadata()
        msg.id = random.randint(1, 100)
        msg.type = random.choice(['box', 'cylinder', 'sphere'])
        msg.length = random.uniform(0.1, 0.5)
        msg.width = random.uniform(0.1, 0.5)
        msg.height = random.uniform(0.1, 0.5)
        msg.position = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
        msg.orientation = [random.uniform(0, 180), random.uniform(0, 180), random.uniform(0, 180)]
        msg.graspable = self.check_graspability(msg)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing Object ID: {msg.id}, Type: {msg.type}, Graspable: {msg.graspable}')

    def check_graspability(self, msg):
        if msg.type == 'sphere':
            return True
        elif msg.type == 'box' and msg.width < 0.4 and msg.height < 0.4:
            return True
        return False

def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

