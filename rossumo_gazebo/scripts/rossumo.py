#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Empty
from geometry_msgs.msg import PoseStamped, Twist, Wrench, Point
from gazebo_msgs.srv import DeleteModel, ApplyBodyWrench, GetLinkState, GetModelState, ApplyJointEffort, ApplyJointEffortRequest, JointRequest

def callback(self):
    apply_wrench_server = rospy.ServiceProxy('gazebo/apply_body_wrench', ApplyBodyWrench)
     #rosservice call /gazebo/apply_body_wrench '{body_name: "chassis", reference_frame: "chassis", wrench: { force: { x: 0, y: 0, z: 200.0 } }, start_time: 0, duration: -1 }'
    rospy.loginfo(rospy.get_caller_id() + "Jump") #, data.data)
    wrench = Wrench() # Message to apply forces in Gazebo
    dt = 0.03         # impulse duration

    wrench.force.x = 0
    wrench.force.y = 0
    wrench.force.z = 0.7/dt

    try:

	resp1 = apply_wrench_server('chassis', '',
			            Point(0,0,0), wrench,
			            rospy.Time.now(), rospy.Duration(dt))

    except rospy.ServiceException, e:
        print "Service did not process request: %s"%str(e)
    
def listener():
    apply_wrench_server = rospy.ServiceProxy('gazebo/apply_body_wrench', ApplyBodyWrench)
  
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("high_jump", Empty, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
