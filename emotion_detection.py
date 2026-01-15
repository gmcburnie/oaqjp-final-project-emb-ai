import requests # Import the requests library to handle HTTP requests
import json # Import the json library to parse HTTP responses

def emotion_detector(text_to_analyze):
    # URL of the emotional prediction service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analysed
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    max_value = None        emotions = prediction['emotion']
        for emotion, score in emotions.items():
            if max_value is None or score > max_value:
                max_value = score
                dominant_emotion = emotion


        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        break

   # anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
   # disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']

    emotional_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    return emotional_response