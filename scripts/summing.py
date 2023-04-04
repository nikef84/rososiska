#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32, Bool

rospy.init_node('sum_node')
pub = rospy.Publisher('to_request', Int32, queue_size=10, latch=True)
flag = Bool()
result = Int32MultiArray()
flag.data = False

def callback(msg):
	
	flag.data = True
	result.data = msg.data
        

def send_to_req():
	while not rospy.is_shutdown():
		
		if flag.data == True:
			msg2 = Int32()
			msg2.data =sum(result.data)
			pub.publish(msg2)
			flag.data = False


rospy.Subscriber('to_sum', Int32MultiArray, callback, queue_size=10)



try:
    send_to_req()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    
    rospy.logerr('Exception catched')