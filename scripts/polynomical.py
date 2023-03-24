#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('polynomical_node')
pub = rospy.Publisher('toxic', Int32, queue_size=10)
sub = rospy.Subscriber('toxic', Int32, queue_size=10)
rate = rospy.Rate(1)

def start_talker():
	msg = Int32()
	while not rospy.is_shutdown():
		msg.data = 
		pub.publish(msg)
		rate.sleep()
		i += 2

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')