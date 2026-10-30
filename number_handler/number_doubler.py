#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class NumberDoubler(Node):
    def __init__(self):
        super().__init__('number_doubler')
        
        self.subscription = self.create_subscription(
            Int32,
            '/number',
            self.listener_callback,
            10
        )
        
        self.publisher_ = self.create_publisher(Int32, '/number_doubled', 10)
        self.get_logger().info('Number Doubler has been started!')

    def listener_callback(self, msg):
        doubled_msg = Int32()
        doubled_msg.data = msg.data * 2
        
        self.publisher_.publish(doubled_msg)
        self.get_logger().info(f'Received Number: {msg.data} --> Doubled: {doubled_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberDoubler()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()