import rclpy
from rclpy.node import Node
from cus_pkg.srv import HarvestSchedule  # Ensure this import is correct

class HarvestServer(Node):
    def __init__(self):
        super().__init__('harvest_server')
        self.srv = self.create_service(HarvestSchedule, 'schedule_harvest', self.schedule_callback)
        self.get_logger().info('Harvest server is up and running...')  # This will confirm the server is started

    def schedule_callback(self, request, response):
        self.get_logger().info("Callback triggered.")  # Add this line for debugging
        self.get_logger().info(f'Received request from Robot ID: {request.robot_id}, Crop Yield: {request.crop_yield}kg, Status: {request.status}')

        # Logic to determine the schedule based on the request
        if request.status == "harvesting" and request.crop_yield > 100:
            response.schedule = "nextfield"
        elif request.status == "maintenance":
            response.schedule = "maintenance"
        else:
            response.schedule = "idle"

        return response

def main(args=None):
    rclpy.init(args=args)
    server = HarvestServer()  # Instantiate the server
    rclpy.spin(server)  # Keep the server running
    rclpy.shutdown()

if __name__ == '__main__':
    main()

