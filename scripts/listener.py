#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def callback(msg):
    rospy.loginfo(msg.data)

rospy.init_node('listener')
rospy.Subscriber('to_poly', Int32MultiArray, callback, queue_size=10)
rospy.spin()