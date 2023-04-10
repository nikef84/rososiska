#!/usr/bin/env python3
import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math
from geometry_msgs.msg import Twist

# Register node / fake node name - we will rename =)
rospy.init_node('tf_carrot')
# Get private parameter / make it global variable
carrotname = rospy.get_param('~carrot_tf_name')
# Callback function
msg = Twist()

def handle_carrot_pose():
    # Get broadcaster object
    br = tf.TransformBroadcaster()
    # Broadcast TF trasform (world -> turtlename)
    time = 0
    amp = 0.5
    w = 10
    while not rospy.is_shutdown():
        msg.linear.x = amp*math.cos(w*time)
        msg.linear.y = amp*math.sin(w*time)
        time += 0.01
        br.sendTransform((msg.linear.x, msg.linear.y, 0),
                        quaternion_from_euler(0, 0, 0),
                        rospy.Time.now(),
                        carrotname,
                        "turtle1")

try:
    handle_carrot_pose()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')