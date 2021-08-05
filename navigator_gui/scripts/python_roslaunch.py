#!/usr/bin/env python

import time
import sys
import roslaunch

# 0 mapping
# 1 auto
# 2 sman

def launch(launch1, launch2):
    launch1.start()
    time.sleep(5)
    launch2.start()
    try:
        launch1.spin()
        launch2.spin()
    finally:
        launch1.shutdown()
        launch2.shutdown()

if __name__ == '__main__':
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    launch_file1 = roslaunch.rlutil.resolve_launch_arguments(['navigator_bringup', 'robot_standalone.launch'])
    launch_file2 = roslaunch.rlutil.resolve_launch_arguments(['navigator_slam', 'slam.launch'])
    launch_file3 = roslaunch.rlutil.resolve_launch_arguments(['navigator_navigation', 'auto.launch'])
    launch_file4 = roslaunch.rlutil.resolve_launch_arguments(['navigator_navigation', 'sman.launch'])

    launch_parent1 = roslaunch.parent.ROSLaunchParent(uuid, launch_file1)
    launch_parent2 = roslaunch.parent.ROSLaunchParent(uuid, launch_file2)
    launch_parent3 = roslaunch.parent.ROSLaunchParent(uuid, launch_file3)
    launch_parent4 = roslaunch.parent.ROSLaunchParent(uuid, launch_file4)

    if sys.argv[1] == '0':
        launch(launch_parent1, launch_parent2)

    elif sys.argv[1] == '1':
        launch(launch_parent1, launch_parent3)

    elif sys.argv[1] == '2':
        launch(launch_parent1, launch_parent4)



