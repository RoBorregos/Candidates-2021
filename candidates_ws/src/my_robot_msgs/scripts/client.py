#!/usr/bin/env python3
import roslib
roslib.load_manifest('my_robot_msgs')
import rospy
import actionlib

from my_robot_msgs.msg import WorkstationAction, WorkstationGoal

if __name__ == '__main__':
    rospy.init_node('workstation_client')
    client = actionlib.SimpleActionClient('workstation', WorkstationAction)
    print("Waiting for action server...")
    client.wait_for_server()
    print("Workstation ready! Sending goal")
    
    goal = WorkstationGoal()
    goal.batch_size = 5
    client.send_goal(goal)
    print("Goal sent...")
    
    # rospy.sleep(3)
    # client.canccel_goal()
    # goal.batch_size = 10
    # client.send_goal(goal)
    
    client.wait_for_result()
    print("\nResults")
    print("Accuracy: ", client.get_result().accuracy_percentage)
    print("Anomalies: ", client.get_result().anomalies)