#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Bool
import time

flag = Bool()
result = Int32MultiArray()
flag.data = False

pub = rospy.Publisher('to_sum', Int32MultiArray, queue_size=10, latch=True)
def callback(msg):
	
	flag.data = True
	result.data = msg.data

def send_to_sum():
	while not rospy.is_shutdown():
		if flag.data == True:
			next_tup = [0]*3
			for i in range(len(result.data), 0, -1):
				next_tup[i-1] = result.data[i-1]**(len(result.data)-i+1)
			#time.sleep(0.1)
			result.data = next_tup
			pub.publish(result)
			print(result.data)
			flag.data = False

rospy.init_node('polynomical_node')
rospy.Subscriber('to_poly', Int32MultiArray, callback,queue_size=10)

try:
    send_to_sum()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')