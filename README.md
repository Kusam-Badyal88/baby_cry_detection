# 👶 **Baby Cry Detection System** 🔊  
An intelligent audio classification web application that detects **various types of baby cries** using machine learning.  
This project helps identify the reason behind a baby's cry, such as **hunger**, **burping**, or **discomfort**, by analyzing real-time audio signals.  
It is useful for **parents**, **caregivers**, and **healthcare providers** to understand baby needs better through sound analysis.

---

## 🚀 **Key Features**

- 🎯 **Real-time Cry Detection**: Identifies cries related to **hunger**, **discomfort**, and **burping**.
- 🎤 **Audio Classification**: Uses ML models to classify baby cry audio signals.
- 🧠 **Multi-Model Support**: Includes **Random Forest**, **SVM**, **Gradient Boosting**, and **KNN**.
- 📊 **Accuracy Displayed**: Each prediction shows corresponding model accuracy.
- 📁 **Web Interface**: Built using **Flask** for a smooth user experience.
- 🧩 **Feature Extraction**: Uses **MFCC**, **Chroma**, and **Mel Spectrogram** with **Librosa**.

---

## 🧠 **Machine Learning Pipeline**

> **Audio Input** → `.wav` files  
> **Preprocessing** → Silence removal, normalization  
> **Feature Extraction** → MFCC, Chroma, Mel Spectrogram  
> **Model Training** → SVM, RF, KNN, GB using scikit-learn  
> **Prediction** → Flask-based interface to classify cry type

---

## 🖼️ **Demo Screenshots**

| Audio Upload Page | Prediction Result |
|-------------------|-------------------|
| ![Upload Page](https://github.com/Kusam-Badyal88/baby_cry_detection/blob/master/baby_cry_detection/upload.png?raw=true) | ![Result Page](https://github.com/Kusam-Badyal88/baby_cry_detection/blob/master/baby_cry_detection/result.png?raw=true) |

---

## 🔍 **How It Works**

1. 🎵 User uploads a baby cry **`.wav` audio file**.
2. 🧪 Audio is processed and features are extracted:
   - MFCC (Mel Frequency Cepstral Coefficients)
   - Chroma Frequencies
   - Mel Spectrogram
3. 🧠 The selected ML model predicts the **reason behind the cry**.
4. ✅ **Prediction and model accuracy** are shown on screen.

---

## 🧠 **Model Predictions**

| Label | Meaning                                        |
|-------|------------------------------------------------|
| 0     | Tired or lack of sleep                         |
| 1     | Burping                                        |
| 2     | Hunger or exhaustion                           |
| 3     | Discomfort or lack of affection and attention  |
| 4     | Belly pain or colic                            |

---

## 🛠️ **Tech Stack**

| Tool / Library    | Purpose                      |
|-------------------|------------------------------|
| Python 🐍         | Programming Language          |
| Flask 🌐          | Web Framework                |
| Librosa 🎵        | Audio Signal Processing      |
| NumPy 📈          | Numerical Operations          |
| Scikit-learn 🤖   | ML Models & Training         |
| HTML/CSS          | Frontend UI Design           |
| Pickle 🧪         | Model Saving & Loading       |

---

## ⚙️ **How to Run the Project**

```bash
# Step 1: Clone the repository
git clone https://github.com/Kusam-Badyal88/baby_cry_detection.git

# Step 2: Navigate to project folder
cd baby_cry_detection

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
python app.py
🎤 Upload your .wav file and get an instant prediction!

📂 Project Structure
bash
Copy
Edit
baby_cry_detection/
├── static/
│   └── style.css
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
Model	   Accuracy
Random Forest 🌲	78%
SVM 📊	64%
Gradient Boosting 🔺	75%
KNN 🤝	79%

✨ Future Improvements
🧠 Add deep learning models (e.g., CNN, LSTM)

📱 Mobile app integration (Android/iOS)

🎙️ Real-time microphone-based cry detection

📊 Expand dataset for better generalization


