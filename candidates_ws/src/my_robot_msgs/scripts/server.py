#!/usr/bin/env python3
import roslib
roslib.load_manifest('my_robot_msgs')
import rospy
import actionlib
import random
from my_robot_msgs.msg import WorkstationAction, WorkstationFeedback, WorkstationResult

class workstationServer:
    _feedback = WorkstationFeedback()
    _result = WorkstationResult()
    
    def __init__(self):
        self.server = actionlib.SimpleActionServer('workstation', WorkstationAction, self.execute, False)
        self.server.start()
        
    def execute(self, goal):
        if goal.batch_size > 100 or goal.batch_size < 1:
            print("Goal not accepted, limit of batch size exceeded")
            self.server.set_aborted()
            return
        
        r = rospy.Rate(1)
        success = True
        self._feedback.percentage_complete = 0.0
        anomalies = 0
        
        print('Checking batch of '+str(goal.batch_size)+' pieces')
        
        i = 0
        batch_size = goal.batch_size
        while i < batch_size:
            if self.server.is_preempt_requested():
                print('Server Preempted')
                self.server.set_preempted()
                success = False
                break
            
            if not random.randrange(3):
                anomalies += 1
                
            self._feedback.percentage_complete = (i+1)/goal.batch_size
            self.server.publish_feedback(self._feedback)
            
            i += 1
            r.sleep()
            
        if success:
            self._result.accuracy_percentage = 1 - anomalies/goal.batch_size
            self._result.anomalies = anomalies
            rospy.loginfo('Succeeded checking batch.')
            self.server.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('workstation_server')
    server = workstationServer()
    rospy.spin()