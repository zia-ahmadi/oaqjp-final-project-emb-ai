from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    # Get text from request
    text_to_analyze = request.form['text']
    
    # Run emotion detection
    result = emotion_detector(text_to_analyze)
    
    # Format response string
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response_text

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
