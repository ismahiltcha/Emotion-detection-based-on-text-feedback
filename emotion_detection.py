import requests

def emotion_detector(text_to_analyze):
    # URL for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Making the POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # Checking if request was successful
    if response.status_code == 200:
        # Parsing the response
        response_json = response.json()
        # Extracting the emotion detected
        emotion_detected = response_json['emotion']['emotion']
        return emotion_detected , {
                                  'anger': anger_score,
                                  'disgust': disgust_score,
                                  'fear': fear_score,
                                  'joy': joy_score,
                                  'sadness': sadness_score,
                                  'dominant_emotion': '<name of the dominant emotion>'
}
    else:
        # If request was not successful, print error message
        print("Error occurred: ", response.text)
        return None

# Example usage:
text_to_analyze = "I am feeling happy today!"
emotion = emotion_detector(text_to_analyze)
print("Emotion detected:", emotion)
