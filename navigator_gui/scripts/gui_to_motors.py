#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16, Bool

#############################################################
class gui_to_motors():
#############################################################
    
    #############################################################
    def __init__(self):
    #############################################################
        rospy.init_node("gui_to_phone")
        self.nodename = rospy.get_name()
        rospy.loginfo("-I- %s started" % self.nodename)  #10260
                
        # publishers
        self.left_pwm_pub = rospy.Publisher("motors/pwm/lwheel", Int16, queue_size = 10)
        self.right_pwm_pub = rospy.Publisher("motors/pwm/rwheel", Int16, queue_size = 10)
        
    #############################################################
    def send(self, l, r):
    #############################################################
        self.left_pwm_pub.publish(l)
        self.right_pwm_pub.publish(r)
    
    #############################################################
    def getcommands(self,intake):
    #############################################################
        if intake == 73:
            self.send(128, 128)
        elif intake == 75:
            self.send(-128, -128)
        elif intake == 74:
            self.send(-128, 128)
        elif intake == 76:
            self.send(128, -128)
        else:
            self.send(0, 0)