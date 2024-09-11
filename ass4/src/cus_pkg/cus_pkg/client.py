# client.py
import sys
import rclpy
from rclpy.node import Node
from my_pkg.srv import CleaningStatus

class CleaningRobotClient(Node):
    def __init__(self):
        super().__init__('cleaning_robot_client')
        self.cli = self.create_client(CleaningStatus, 'cleaning_status')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')

    def send_request(self, status, area):
        request = CleaningStatus.Request()
        request.status = status
        request.area = area
        future = self.cli.call_async(request)
        future.add_done_callback(self.callback)

    def callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Response: new_status={response.new_status}')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    client = CleaningRobotClient()
    client.send_request('cleaning', 30.0)  # Sending a request with status 'cleaning' and area 30.0
    rclpy.spin(client)

if __name__ == '__main__':
    main()

