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
    text_to_analyze = request.args.get('textToAnalyze')
    res = emotion_detector(text_to_analyze)

    # Error handling, bad request
    if res['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    # Return response with emotion scores
    return (
            "For the given statement, the system response is "
            f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
            f"'fear': {res['fear']}, 'joy': {res['joy']}, "
            f"'sadness': {res['sadness']}. "
            f"The dominant emotion is {res['dominant_emotion']}."
        )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
