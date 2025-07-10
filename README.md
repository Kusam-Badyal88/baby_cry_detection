👶 Baby Cry Detection System 🔊
An intelligent audio classification web application that detects various types of baby cries using machine learning. This project helps identify the reason behind a baby's cry, such as hunger, burping, or discomfort, by analyzing real-time audio signals.

🚀 Key Features
🎯 Real-time Cry Detection: Identifies cries related to hunger, discomfort, and burping.
🎤 Audio Classification: Uses ML models to classify audio signals.
📊 Machine Learning Models: Includes SVM, Random Forest, KNN, and Gradient Boosting.
🌐 Web Interface: Built using Flask for easy user interaction.
🧠 Feature Extraction: Extracts MFCCs, Mel Spectrogram, Zero Crossing Rate, and Spectral Centroid using Librosa.

🖼️ Demo Screenshots
Audio Page	
https://github.com/Kusam-Badyal88/baby_cry_detection/blob/master/baby_cry_detection/upload.png?raw=true

Result Page 
https://github.com/Kusam-Badyal88/baby_cry_detection/blob/master/baby_cry_detection/result.png?raw=true



🔍 How It Works
User uploads a baby cry audio clip.

Audio is processed and features are extracted:

MFCC

Chroma Frequencies

Mel Spectrogram

Chosen ML model predicts the reason behind the cry.

Result is shown along with model accuracy.

🧠 Model Predictions
Label	Meaning
0	Tired or lack of sleep
1	Burping
2	Hunger or exhaustion
3	Discomfort or lack of affection
4	Belly pain or colic

🚀 Technologies Used
Python 🐍

Flask 🌐

Librosa 🎵

NumPy 📈

Scikit-learn 🤖

HTML/CSS for frontend

🛠️ Installation
bash
Copy
Edit
git clone https://github.com/yourusername/baby_cry_detection.git
cd baby_cry_detection
pip install -r requirements.txt
python app.py
Upload your .wav file and get the prediction!

📂 Project Structure
cpp
Copy
Edit
baby_cry_detection/
├── static/
├── templates/
│   ├── index.html
│   └── result.html
├── uploads/
├── images/
│   ├── upload.png
│   └── result.png
├── rf_model.pkl
├── svm_model.pkl
├── gb_model.pkl
├── knn_model.pkl
├── app.py
└── README.md
📈 Model Accuracies
Model	Accuracy
Random Forest	78%
SVM	64%
Gradient Boosting	75%
KNN	79%

✨ Future Improvements
Add deep learning models (e.g., CNN, LSTM)

Mobile app integration

Real-time microphone-based detection

Larger dataset for higher accuracy
