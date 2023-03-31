#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray
import time


pub = rospy.Publisher('to_sum', Int32MultiArray, queue_size=10)
def callback(msg):
	global data
	print('AAA')
	data = msg.data

while not rospy.is_shutdown:
	next_tup = [0]*3
	for i in range(len(data), 0, -1):
		next_tup[i-1] = data[i-1]**(len(data)-i+1)
	#time.sleep(0.1)
	print('2')
	data = next_tup
	pub.publish(data)
	print('4')

rospy.init_node('polynomical_node')
rospy.Subscriber('to_poly', Int32MultiArray, callback,queue_size=10)