#!usr/bin/env python3 

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String 
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

class SubscriberNode(Node):

    def __init__(self, name):
        super().__init__(name)

        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.sub = self.create_subscription(String, 
            "chatter", self.listener_callback, qos_profile)

    def listener_callback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode("qos_helloworld_sub")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()