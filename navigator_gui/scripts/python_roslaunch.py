#!/usr/bin/env python

import rospy
import roslaunch
import time
import sys

# print(sys.argv[1])

uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

robot_ = roslaunch.rlutil.resolve_launch_arguments(['navigator_bringup', 'robot_standalone.launch'])
slam_ = roslaunch.rlutil.resolve_launch_arguments(['navigator_slam', 'mapping.launch'])
auto_ = roslaunch.rlutil.resolve_launch_arguments(['navigator_navigation', 'auto.launch'])
sman_ = roslaunch.rlutil.resolve_launch_arguments(['navigator_navigation', 'sman.launch'])

robot = roslaunch.parent.ROSLaunchParent(uuid, robot_)
slam = roslaunch.parent.ROSLaunchParent(uuid, slam_)
auto = roslaunch.parent.ROSLaunchParent(uuid, auto_)
sman = roslaunch.parent.ROSLaunchParent(uuid, sman_)

robot.start()

try:
    robot.spin()

finally:
    robot.shutdown()


