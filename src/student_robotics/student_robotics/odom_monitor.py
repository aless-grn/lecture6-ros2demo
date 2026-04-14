#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomMonitor(Node):
    def __init__(self):
        super().__init__('odom_monitor')
        
        # Create subscriber: message type, topic name, callback function, queue size
        self.subscription = self.create_subscription(
            Odometry,               # Message type
            '/odom',                # Topic name
            self.odom_callback,     # Callback function
            10                      # Queue size
        )
        
        self.get_logger().info('Odom Monitor started! Listening to /odom')
    
    def odom_callback(self, msg):
        # Extract position
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        # Extract linear velocity
        linear_x = msg.twist.twist.linear.x
        angular_z = msg.twist.twist.angular.z
        
        self.get_logger().info(
            f'Position: x={x:.2f}, y={y:.2f} | Velocity: linear.x={linear_x:.2f}, angular.z={angular_z:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdomMonitor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()