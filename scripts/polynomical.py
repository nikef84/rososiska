#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

rospy.init_node('polynomical_node')
pub = rospy.Publisher('to_sum', Int32MultiArray, queue_size=10)

def callback(msg):
	rospy.loginfo('ebashu')
	for i in range(len(msg.data), 0, -1):
		msg.data[i] = msg.data[i]^(i)
	pub.publish(msg)


rospy.Subscriber('to_poly', Int32MultiArray, callback, queue_size=10)
rospy.spin()