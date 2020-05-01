import speech_recognition as sr
import rospy
from std_msgs.msg import String

print(sr.__version__)

def return_speech():
    input("Press Enter for next input : ")
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Speak up")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print("recognizing")
    data = r.recognize_google(audio)
    print(data)
    return data

rospy.init_node('talker', anonymous=True)
pub1 = rospy.Publisher('/voice', String,queue_size=10)
pub2 = rospy.Publisher('chat', String,queue_size=10)
pub3 = rospy.Publisher('direction', String,queue_size=10)

#while True:
def talker():
    text=String()
    text = return_speech()
    print("You said {}\n\n".format(text))
    t = text.split(" ")
    k="terminate"
    if str(t[0]) in ("right","left","ascend","down","take","spin","come","go","position"):
        m="Ginni going to "
        pub3.publish(text)
        text=m+" "+text
        pub2.publish(text) 
    elif str(t[0])==k:
        m="with pleasure"
        pub2.publish(m)        
    else:
        pub1.publish(text)
while True:
    try:
        talker()
    except Exception:
        print(Exception)
        pass
