# 🧠 Suicidal Ideation Detection System

A deep learning-powered mental health monitoring system that detects suicidal ideation based on user text or speech input. Built using a fine-tuned **electra** transformer model and deployed through a **Streamlit** dashboard, this project enables users to monitor daily emotional health and track trends through weekly reports.

---

## 📌 Features

- 📝 Accepts **text** and **speech** input from users
- 🤖 Fine-tuned **electra** model for high-accuracy classification
- 📁 **No database required** — all data stored in CSV and TXT files
- 📊 7-day **stress trend visualization** using matplotlib
- 🧾 Weekly **emotional report** summarizing mental health risk
- 📦 Easy-to-run **Streamlit app** for real-time interaction

---

## 🧠 Model Overview

- **Model Used**: `roberta-base` from Hugging Face Transformers
- **Fine-tuning Dataset**: 1.5 million rows of suicidal and non-suicidal texts
- **Type**: Binary Classification (`suicide`, `non-suicide`)
- **Why RoBERTa?**: High language understanding, strong performance on nuanced emotional content

---

## 🏗️ Project Structure

SUICIDE_PROJECT/
│
├── TRAINING/
│ └── MODEL(Trained electra model)
│ ├── config.json
│ ├── pytorch_model.bin
│ └── tokenizer files...
│
├── user_data.csv # Logs input text, prediction, date
├── user_speech_log.txt # Logs speech-transcribed input
├── weekly_report.txt # 7-day emotional health summary
│
├── app.py # Streamlit UI + dashboard
├── predict.py # Prediction and logging
├── speech_to_text.py # Captures and converts speech to text
├── weekly_report_generator.py # Generates 7-day average report
├── requirements.txt # All project dependencies
└── README.md # Project documentation
 

## ⚙️ Installation & Setup

### 🔁 Clone the Repository

```bash
git clone https://github.com/yourusername/suicidal-ideation-detector.git
cd suicidal-ideation-detector
🧱 Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you're using Windows and get PyAudio errors:

 
pip install pipwin
pipwin install pyaudio
📦 Place the Trained Model
Put your trained RoBERTa model in:
 
TRAINING/roberta_model/
Make sure it includes:

pytorch_model.bin

config.json

tokenizer.json or equivalent vocab files

🚀 How to Run
Start the dashboard locally:

 
streamlit run app.py
🧪 How It Works
User submits input (typed or spoken)

Speech is converted to text using Google Speech Recognition

Input is classified by RoBERTa model as suicide or non-suicide

Result is logged to user_data.csv

A matplotlib graph shows daily predictions for the past 7 days

A weekly report is generated in weekly_report.txt

✨ Example Output
user_data.csv
Date	Input Text	Prediction	Probability
2025-07-10	I feel lost and hopeless.	suicide	0.93
2025-07-11	I’m finally feeling better today.	non-suicide	0.22

weekly_report.txt
 
🧾 Weekly Emotional Report (Jul 4 - Jul 10)

🔴 Day 1: At Risk
🟢 Day 2: Stable
🔴 Day 3: At Risk
🟢 Day 4: Stable
🟢 Day 5: Stable
🟢 Day 6: Stable
🟢 Day 7: Stable

📉 Weekly Mood Summary: Stable (5/7 days non-suicidal)
📊 Dashboard
Real-time predictions from text or mic

Graph of emotional state for the last 7 days

Weekly report generation button

📦 Requirements
transformers

torch

streamlit

pandas

matplotlib

speechrecognition

pyaudio

scikit-learn

📄 License
This project is licensed under the MIT License.

You are free to use, modify, and distribute this code, provided that you include the original copyright.

 
MIT License

Copyright (c) 2025 Deepak N.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction...

[Full License Text Here](https://opensource.org/licenses/MIT)
⚠️ Disclaimer
This project is intended for research and educational purposes only.
It is not a substitute for professional mental health support.
If you or someone you know is struggling, please contact a licensed therapist or helpline.

👨‍💻 Author
Deepak N.
Lead, NextGen Cloud Club | VIT-AP
Python & Machine Learning Developer

💡 Future Work
🔐 Add user authentication

📱 Build mobile interface

🧠 Add sentiment scoring from speech tone

☁️ Host on Streamlit Cloud or Hugging Face Spaces
