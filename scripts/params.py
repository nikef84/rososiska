#!/usr/bin/env python3
import rospy
rospy.init_node('params_study')

# Мы этот параметр ставили ранее
param_name_2_delete = '/ros_glob_param'

# Проверим список параметров, только уже через Python
param_list = rospy.get_param_names()
rospy.loginfo(param_list)

# Наличие можно проверить через функционал ROS    
if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')
    
# И с проверкой удаляем его
if rospy.has_param(param_name_2_delete):
    rospy.delete_param(param_name_2_delete)
    
# Еще раз проверим:
if rospy.has_param(param_name_2_delete):
    rospy.loginfo('[ROSWay] Parameter exist')
else:
    rospy.loginfo('[ROSWay] Parameter not exist')