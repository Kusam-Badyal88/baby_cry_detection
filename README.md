# 👶 Baby Cry Detection System 🔊

An intelligent **audio classification web app** that detects and interprets different types of baby cries using **Machine Learning**. This project helps parents and caregivers understand a baby’s needs (e.g., hunger, discomfort, tiredness) by analyzing cry sounds in real time.

---

## 🌟 Key Features
- 🎧 **Real-time audio classification** of baby cries
- 🧠 **Multi-Model Support**: SVM, Random Forest, KNN, Gradient Boosting
- 📊 **Model Accuracy Display** after each prediction
- 🌐 **User-friendly Web Interface** built with Flask
- 🧩 **Feature Extraction** using MFCC, Chroma, and Mel Spectrogram
- 🖼️ **Visual Output** with prediction reason and confidence

---

## 🔍 How It Works
1. User uploads a `.wav` baby cry audio file
2. Audio features are extracted:
   - MFCC
   - Chroma Frequencies
   - Mel Spectrogram
3. Chosen ML model classifies the sound
4. Result and model accuracy are displayed

---

## 📂 Labels Used for Classification
| Label Code | Description                                  |
|------------|----------------------------------------------|
| 0          | Tired or lack of sleep 💤                   |
| 1          | Burping 💨                                   |
| 2          | Hunger or exhaustion 🍼                     |
| 3          | Discomfort or lack of attention 😟          |
| 4          | Belly pain or colic 🤕                      |

---

## 🛠️ Tech Stack
| Tool           | Usage                            |
|----------------|----------------------------------|
| Python 🐍       | Core programming language         |
| Flask 🌐        | Web framework                    |
| Librosa 🎵      | Audio signal processing           |
| Scikit-learn 🤖 | Machine learning models           |
| HTML/CSS 🖥️     | Frontend interface               |
| Pickle 🧃       | Model storage/loading             |

---

## 🚀 Run This Project Locally

```bash
git clone https://github.com/Kusam-Badyal88/baby-cry-detection.git
cd baby-cry-detection
pip install -r requirements.txt
python app.py
➡️ Open browser and go to: http://127.0.0.1:5000

🖼️ Screenshots
Upload Page:


Result Page:


📈 Model Accuracy
Model	Accuracy
Random Forest 🌲	78%
SVM 📊	64%
Gradient Boosting 🔺	75%
KNN 🤝	79%

✨ Future Enhancements
🤖 Integrate Deep Learning models (e.g., CNN, LSTM)

📱 Mobile app version

🎙️ Real-time cry detection using microphone

📊 Expand dataset for improved accuracy



