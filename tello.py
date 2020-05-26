#!/usr/bin/env python
import rospy
from easytello import tello

from std_msgs.msg import String, Float64


rospy.init_node('todrone', anonymous=True)
my_drone = tello.Tello()

def callback(data1):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data1.data)
    data = str(data1.data)
    print(data)
    assign(data)
rospy.Subscriber("direction", String, callback)


def assign(data):
    data = data.split(" ")
    print(data)

    if(data[0]=='take' and data[1]=='off'):
        my_drone.takeoff()    

    if(data[0]=='come'):
        my_drone.forward(100)    

    if(data[0]=='flip' and data[1]=='right'):
        my_drone.flip('right')

    if(data[0]=='flip' and data[1]=='left'):
        my_drone.flip('left')
          
    if(data[0]=='go'):
        my_drone.back(100)

    if(data[0]=='right'):
        my_drone.right(100)

    if(data[0]=='left'):
        my_drone.left(100)

    if(data[0]=='ascend'):
        my_drone.up(100)

    if(data[0]=='down'):
        my_drone.down(100)

    if(data[0]=='spin'):
        my_drone.ccw(180)
        
rospy.spin()


