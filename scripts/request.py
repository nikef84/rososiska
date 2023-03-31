#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32
import time

rospy.init_node('request_node')
pub = rospy.Publisher('to_poly', Int32MultiArray, queue_size=10)
msg_in = Int32MultiArray()
msg_in.data = (2, 4, 5)
time.sleep(1)
pub.publish(msg_in)

def callback(msg_out):
	print('0')
	rospy.loginfo(f'Sum is: {msg_out.data}')

rospy.Subscriber('to_request', Int32, callback, queue_size=10)
rospy.spin()