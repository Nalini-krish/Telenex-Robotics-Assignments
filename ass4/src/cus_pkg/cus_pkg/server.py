# server.py
import rclpy
from rclpy.node import Node
from my_pkg.srv import CleaningStatus

class CleaningRobotService(Node):
    def __init__(self):
        super().__init__('cleaning_robot_service')
        self.srv = self.create_service(CleaningStatus, 'cleaning_status', self.handle_cleaning_status)
        self.get_logger().info('Service ready to accept requests.')

    def handle_cleaning_status(self, request, response):
        self.get_logger().info(f'Received: status={request.status}, area={request.area}')
        
        # Basic logic to allocate new status
        if request.status == 'cleaning':
            response.new_status = 'not_clean' if request.area < 50 else 'clean'
        else:
            response.new_status = 'clean' if request.status == 'idle' else 'not_clean'
        
        self.get_logger().info(f'Sending: new_status={response.new_status}')
        return response

def main(args=None):
    rclpy.init(args=args)
    cleaning_robot_service = CleaningRobotService()
    rclpy.spin(cleaning_robot_service)
    cleaning_robot_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

