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
        rospy.sleep(0.1)

        # Set the gripper target to neutal position using a joint value target
        gripper.set_joint_value_target(GRIPPER_OPEN)

        # Plan and execute the gripper motion
        gripper.go()
        rospy.sleep(0.1)
        rospy.loginfo("mw gripper current joint values= " + str(gripper.get_current_joint_values()))

        start_time = datetime.datetime.now()

        # Grab 1st ball
        arm.set_named_target('B5_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('B5_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to E12
        arm.set_named_target('EBCdrop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 2nd ball
        arm.set_named_target('B4_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('B4_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to E6
        arm.set_named_target('EB6drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 3rd ball
        arm.set_named_target('B3_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('B3_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N12
        arm.set_named_target('NBCdrop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 4st ball
        arm.set_named_target('B2_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('B2_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N6
        arm.set_named_target('NB6drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 5th ball
        arm.set_named_target('B1_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('B1_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W8
        arm.set_named_target('WB8drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Loose the ball gripper
        arm.set_named_target('G_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('G_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('G_3pull')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Turn the 1st Dice
        arm.set_named_target('D1_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_3over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_4drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_5over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_6grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_7over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D1_8drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Turn the 2nd Dice
        arm.set_named_target('D2_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_3over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_4drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_5over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_6grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_7over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D2_8drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Turn the 3rd Dice
        arm.set_named_target('D3_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_3over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_4drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_5over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_6grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_7over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D3_8drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Turn the 4th Dice
        arm.set_named_target('D4_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_3over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_4drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_5over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_6grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_7over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('D4_8drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 1st Lego
        arm.set_named_target('L1_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('L1_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N1
        arm.set_named_target('NL1drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 2nd Lego
        arm.set_named_target('L2_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('L2_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N2
        arm.set_named_target('NL2drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 3rd Lego
        arm.set_named_target('L3_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('L3_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N3
        arm.set_named_target('NL3drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 4th Lego
        arm.set_named_target('L4_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('L4_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N10
        arm.set_named_target('NLAdrop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 5th Lego
        arm.set_named_target('L5_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('L5_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to N7
        arm.set_named_target('NL7drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 1st Pencil
        arm.set_named_target('P1_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('P1_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W1
        arm.set_named_target('WP1drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 2nd Pencil
        arm.set_named_target('P2_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('P2_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W1
        arm.set_named_target('WP1drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 3rd Pencil
        arm.set_named_target('P3_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('P3_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W1
        arm.set_named_target('WP1drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 4th Pencil
        arm.set_named_target('P4_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('P4_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W1
        arm.set_named_target('WP1drop')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_OPEN)
        gripper.go()
        rospy.sleep(0.1)

        # Grab 5th Pencil
        arm.set_named_target('P5_1over')
        arm.go()
        rospy.sleep(0.1)

        arm.set_named_target('P5_2grab')
        arm.go()
        rospy.sleep(0.1)

        gripper.set_joint_value_target(GRIPPER_CLOSED)
        gripper.go()
        rospy.sleep(0.1)

        # Bring to W1
        arm.set_named_target('WP1drop')
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
