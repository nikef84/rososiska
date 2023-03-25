#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

rospy.init_node('sum_mode')
pub = rospy.Publisher('to_request', Int32, queue_size=10)


def callback(msg):
    rospy.loginfo('ebashu')
    pub.publish(sum(msg))


rospy.Subscriber('to_sum', Int32MultiArray, callback, queue_size=10)
rospy.spin()