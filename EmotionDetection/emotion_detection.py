import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    response_dict = json.loads(response.text)

    emotion = response_dict["emotionPredictions"][0]["emotion"]

    anger_score = emotion["anger"]
    disgust_score = emotion["disgust"]
    fear_score = emotion["fear"]
    joy_score = emotion["joy"]
    sadness_score = emotion["sadness"]

    emotion_scores = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }