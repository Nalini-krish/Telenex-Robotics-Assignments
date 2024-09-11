import rclpy
from rclpy.node import Node
from cus_pkg.srv import HarvestSchedule  # Import your service
import time

class HarvestClient(Node):
    def __init__(self):
        super().__init__('harvest_client')
        self.client = self.create_client(HarvestSchedule, 'schedule_harvest')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

    def send_request(self):
        request = HarvestSchedule.Request()
        request.robot_id = "robot_1"  # Sample robot ID
        request.crop_yield = 150  # Sample crop yield in kg
        request.status = "harvesting"  # Sample status

        self.get_logger().info('Sending request...')
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'Response from server: Schedule - {future.result().schedule}')
        else:
            self.get_logger().error('Exception while calling service: {}'.format(future.exception()))

def main(args=None):
    rclpy.init(args=args)
    client = HarvestClient()
    
    try:
        while rclpy.ok():  # Keep running until interrupted
            client.send_request()  # Send request
            time.sleep(5)  # Adjust the delay between requests as needed
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()  # Ensure shutdown occurs

if __name__ == '__main__':
    main()

