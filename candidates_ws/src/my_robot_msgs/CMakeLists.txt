cmake_minimum_required(VERSION 3.0.2)
project(my_robot_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  moveit_msgs
  actionlib
  actionlib_msgs
  message_generation
  message_runtime
  roscpp
  rospy
  std_msgs           
)
  
add_action_files(
  DIRECTORY action
  FILES Workstation.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS actionlib actionlib_msgs message_generation message_runtime roscpp rospy std_msgs 
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)