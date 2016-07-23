#!/usr/bin/env python

"""
    moveit_fk_demo.py - Version 0.1

    Use forward kinemtatics to move the arm to a specified set of joint angles

    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2014 Patrick Goebel.  All rights reserved.

    Adapted for the so_arm: marco@sonic.net

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.5

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:

    http://www.gnu.org/licenses/gpl.html
"""

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItDemo:
    def __init__(self):
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the ROS node
        rospy.init_node('moveit_demo', anonymous=True)

        GRIPPER_OPEN = [0.015, 0.015]
        GRIPPER_CLOSED = [0.003, 0.003]
        GRIPPER_NEUTRAL = [0.01, 0.01]

        # Connect to the arm move group
        arm = moveit_commander.MoveGroupCommander('arm')

        # Connect to the gripper move group
        gripper = moveit_commander.MoveGroupCommander('gripper')

        rospy.loginfo("mw gripper name= " + gripper.get_name())
        rospy.loginfo("mw gripper active joints= " + str(gripper.get_active_joints()))
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        # Get the name of the end-effector link
        end_effector_link = arm.get_end_effector_link()

        # Display the name of the end_effector link
        rospy.loginfo("The end effector link is: " + str(end_effector_link))

        # Set a small tolerance on joint angles
        arm.set_goal_joint_tolerance(0.001)
        gripper.set_goal_joint_tolerance(0.002)

        # Start the arm target in "start" pose stored in the SRDF file
        arm.set_named_target('start')

        # Plan a trajectory to the goal configuration
        traj = arm.plan()

        # Execute the planned trajectory
        arm.execute(traj)

        # Pause for a moment
        rospy.sleep(1)

        # Set the gripper target to neutal position using a joint value target
        gripper.set_joint_value_target(GRIPPER_NEUTRAL)

        # Plan and execute the gripper motion
        gripper.go()
        rospy.sleep(1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        # Close the gripper as if picking something up
        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        # Set the arm target to the named "t1" pose stored in the SRDF file
        arm.set_named_target('t1')

        # Plan and execute the motion
        arm.go()
        rospy.sleep(1)

        # Open the gripper as if letting something go
        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        # Return the arm to the named "start" pose stored in the SRDF file
        arm.set_named_target('start')
        arm.go()
        rospy.sleep(1)

        # Return the gripper target to neutral position
        gripper.set_joint_value_target(GRIPPER_NEUTRAL)
        gripper.go()
        rospy.sleep(1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        # Cleanly shut down MoveIt
        moveit_commander.roscpp_shutdown()

        # Exit the script
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItDemo()
    except rospy.ROSInterruptException:
        pass
