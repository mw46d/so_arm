#!/usr/bin/env python

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand
import datetime

class MoveItSo:
    def __init__(self):
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        # Initialize the ROS node
        rospy.init_node('moveit_demo', anonymous=True)

        GRIPPER_OPEN = [0.030, 0.030]
        GRIPPER_DICE = [0.011, 0.011]
        GRIPPER_GRIPPER = [0.02, 0.02]
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
        rospy.sleep(2)

        # Set the gripper target to neutal position using a joint value target
        gripper.set_joint_value_target(GRIPPER_OPEN)

        # Plan and execute the gripper motion
        gripper.go()
        rospy.sleep(1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        start_time = datetime.datetime.now()

        # Turn the 1st Dice
        arm.set_named_target('G_1over')
        arm.go()
        rospy.sleep(2.2)

        arm.set_named_target('G_2grab')
        arm.go()
        rospy.sleep(0.4)

        gripper.set_joint_value_target(GRIPPER_GRIPPER)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('G_3pull')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Return the arm to the named "start" pose stored in the SRDF file
        arm.set_named_target('start')
        arm.go()
        rospy.sleep(0.1)

        stop_time = datetime.datetime.now()

        print "took: %s\n" % str(stop_time - start_time)

        # Cleanly shut down MoveIt
        moveit_commander.roscpp_shutdown()

        # Exit the script
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        MoveItSo()
    except rospy.ROSInterruptException:
        pass
