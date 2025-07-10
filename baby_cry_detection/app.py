import os
import numpy as np
import librosa
import pickle
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Load the classifiers
model_paths = {
    "random_forest": "rf_model.pkl",
    "svm": "svm_model.pkl",
    "gradient_boosting": "gb_model.pkl",
    "knn": "knn_model.pkl"
}
classifiers = {}

for model_name, model_path in model_paths.items():
    with open(model_path, 'rb') as f:
        classifiers[model_name] = pickle.load(f)

# Accuracy values for each model
model_accuracies = {
    "random_forest": 0.78,
    "svm": 0.64,
    "gradient_boosting": 0.75,
    "knn": 0.79
}

# Function to extract features from audio file
def extract_features(file_path, mfcc=True, chroma=True, mel=True):
    y, sr = librosa.load(file_path)
    features = []
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T, axis=0)
        features.extend(mfccs)
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(y=y, sr=sr).T, axis=0)
        features.extend(chroma)
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=y, sr=sr).T, axis=0)
        features.extend(mel)
    return features

# Function to classify audio file and provide reason
# Function to classify audio file and provide reason
def classify_audio(audio_file, classifier):
    features = extract_features(audio_file)
    prediction = classifier.predict([features])[0]
    class_mapping = {
        0: "tired or lack of sleep",
        1: "burping",
        2: "hunger or exhaustion",
        3: "discomfort or lack of affection and attention",
        4: "belly pain or colic"
    }
    return class_mapping[prediction]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'audio' not in request.files or 'algorithm' not in request.form:
        return redirect(request.url)
    file = request.files['audio']
    algorithm = request.form['algorithm']
    if file.filename == '':
        return redirect(request.url)
    if file and algorithm in classifiers:
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)
        classifier = classifiers[algorithm]
        prediction = classify_audio(file_path, classifier)
        accuracy = model_accuracies[algorithm] * 100  # Convert to percentage
        os.remove(file_path)
        # Capitalize the prediction value
        prediction = prediction.capitalize()
        return render_template('result.html', prediction=prediction, accuracy=accuracy)
    return redirect(request.url)

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)