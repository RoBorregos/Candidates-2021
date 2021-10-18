#!/usr/bin/env python3
# license removed for brevity
import rospy
import time
from std_msgs.msg import UInt16

if __name__ == '__main__':
    try:
        rospy.init_node('mock_shutdown_system', anonymous=True)
        pub = rospy.Publisher('system_health', UInt16, queue_size=10)
        pub.publish(1)
        rospy.loginfo("System error published.")
    except rospy.ROSInterruptException:
        pass