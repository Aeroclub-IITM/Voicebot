# Voicebot

A small ML based interactable software to control drone

## Introduction

This repo aims to develop a software which accepts speech from user and process it to follow comands and to speak back.

[speech_recog.py](https://github.com/Aeroclub-IITM/Voicebot/blob/master/speech_recog.py)  gets the input from user and publishes to 'direction' topic, 'voice' topic and 'chat' topic depends on the string.

[chatbot.py](https://github.com/Aeroclub-IITM/Voicebot/blob/master/chatbot.py)  subscribes values from 'voice' topic ,runs a classifier and publishes the values to 'chat' topic.

[speech.py](https://github.com/Aeroclub-IITM/Voicebot/blob/master/speech.py)  subscibes values from 'chat' topic and converts to voice.

[speech_drone](https://github.com/Aeroclub-IITM/Voicebot/blob/master/speech_drone.py)  subscribes values from 'direction' topic and converts to mavros messages.

[intents.json](https://github.com/Aeroclub-IITM/Voicebot/blob/master/intents.json)  is the dataset.

[chatgui.py](https://github.com/Aeroclub-IITM/Voicebot/blob/master/chatgui.py)  is a chatbot in which you can type in to get response.This program is to check if your chatbot is working properly.

## Installation

Install ros, sitl and mavros. Follow these steps.

Install these libraries.

sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio

pip3 install SpeechRecognition

pip3 install gTTS

pip3 install playsound

pip3 install keras

pip3 install tensorflow

python3 -m nltk.downloader all


## To train your voicebot

To train your own model, first delete 'chatbot_model.h5','classes.pkl' and 'words.pkl'.

Now you need to add label,sample inputs and set of outputs in intends.json. Install a json editor or just drag and drop on to your browser and copy.Now create a text file and paste it. After editing your text file rename file as intends.json.

Now place this file with the rest of the codes and run [train_chatbot.py](https://github.com/Aeroclub-IITM/Voicebot/blob/master/train_chatbot.py).You will see the deleted files popping up.Now check if the chatbot working properly with chatgui.py.

## Launch 

Run  speech_recog.py , speech_drone.py , speech.py , chatbot.py along with mavros and sitl with gazebo to get your interactable chatbot drone.
