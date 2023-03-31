#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32

rospy.init_node('sum_node')
pub = rospy.Publisher('to_request', Int32, queue_size=10)


def callback(msg):
    print('5')  
    msg2 = Int32()
    print(msg.data)
    msg2.data =sum(msg.data)
    print('7')
    pub.publish(msg2)
    print('8')


rospy.Subscriber('to_sum', Int32MultiArray, callback, queue_size=10)
rospy.spin()