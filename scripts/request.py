#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int32, Bool
import time

rospy.init_node('request_node')
pub = rospy.Publisher('to_poly', Int32MultiArray, queue_size=10, latch=True)

flag = Bool()
result = Int32()
flag.data = False

msg_in = Int32MultiArray()
msg_in.data = (2, 4, 5)
time.sleep(1)
pub.publish(msg_in)

def callback(msg_out):
    flag.data = True
    result.data = msg_out.data
        
def read_msg():
     while not rospy.is_shutdown():
          if flag.data == True:
               rospy.loginfo(f'Sum is: {result.data}')
               break
     

rospy.Subscriber('to_request', Int32, callback, queue_size=10)

try:
    read_msg()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')


