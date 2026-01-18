''' Executing this function initiates the application of emotion 
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package 
# Import the emotion_detector function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using the emotion_detector()
        function. The output shows the score for each emotion detected
        and the "dominant" emotion with the highest score.
    '''

