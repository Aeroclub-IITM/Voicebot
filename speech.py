# Import the required module for text  
# to speech conversion 
import rospy
from std_msgs.msg import String
from gtts import gTTS 
from playsound import playsound
  
# This module is imported so that we can  
# play the converted audio 
import os 

rospy.init_node('real_talker', anonymous=True)

def callback(data1):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data1.data)
    data = str(data1.data)
    print(data)
    assign(data)

rospy.Subscriber("/chat", String, callback)

def assign(data):
  # Language in which you want to convert 
    language = 'en'
    
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=data, lang=language, slow=False) 
   
    myobj.save("welcome.mp3") 
  
    playsound('welcome.mp3') 

rospy.spin()
