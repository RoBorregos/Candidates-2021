#!/usr/bin/env python3
# license removed for brevity
import rospy
import random
from std_msgs.msg import UInt16

def talker():
    ''' For the env_analysis_feedback messages:
        0 - There is no stimuli
        1 - Person asked for a drink
        2 - The cup is in front of you
    '''
    pub = rospy.Publisher('env_analysis_feedback', UInt16, queue_size=10)
    rospy.init_node('env_analysis_node', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        env_analysis = random.randint(0,2)
        rospy.loginfo(env_analysis)
        pub.publish(env_analysis)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass