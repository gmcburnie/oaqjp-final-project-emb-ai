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
    
    '''
    Extract the dictionary of emotions and scores from the response.
    Loop through emotions, determine which one has the highest score,
    record this as dominant. 
    Add emotion and score to output dictionary.
    '''
    prediction = formatted_response['emotionPredictions'][0] # Get first item 
    emotions = prediction['emotion'] # Get dictionary of emotions and scores
    emotional_response = {} # Instantiate dictionary to be returned
    max_score = None # Set score for dominant emotion to None
    
    for emotion, score in emotions.items():
        if max_score is None or score > max_score: 
            max_score = score # record score as highest encountered so far
            dominant_emotion = emotion # record emotion as most dominant encountered so far
        emotional_response[emotion] = score # Add emotion and score to output dictionary
    
    # Add dominant emotion to output dictionary
    emotional_response["dominant_emotion"] = dominant_emotion 
    
    return emotional_response
