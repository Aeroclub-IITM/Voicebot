import rospy
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from std_msgs.msg import String
from tensorflow.keras.models import load_model
import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

rospy.init_node('chatbot', anonymous=True)
global data2

def callback(data1):
    msg=String()
    msg=data1
    data2 = str(msg.data)
    
    
    if data2 != '':
        print(data2)

        sentence_words = nltk.word_tokenize(str(data2))
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]

   
        bag = [0]*len(words)  
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1

        p= np.array(bag)
        res = model.predict(np.array([p]))[0]
        print(res)
        ERROR_THRESHOLD = 0.25
        results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        ints = return_list

        tag = ints[0]['intent']
        list_of_intents = intents['intents']
        for i in list_of_intents:
            if(i['tag']== tag):
                result = random.choice(i['responses'])
                break
        res= result


        pub = rospy.Publisher('/chat', String,queue_size=10)
        pub.publish(res)
        print(data2)

rospy.Subscriber("/voice", String, callback)
rospy.spin()
