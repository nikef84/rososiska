#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('my_num_topic', String, queue_size=10)
pub1 = rospy.Publisher('overflov_num_topic', String, queue_size=10)
rate = rospy.Rate(10)


def start_talker():
    msg = String()
    current_pub = pub
    i = 0
    while not rospy.is_shutdown():
        hello_str = str(i)
        rospy.loginfo(hello_str)
        msg.data = hello_str
        current_pub.publish(msg)
        rate.sleep()
        i += 2
        if (i>100):
            i = 0
            current_pub = pub1 if current_pub == pub else pub
        

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')