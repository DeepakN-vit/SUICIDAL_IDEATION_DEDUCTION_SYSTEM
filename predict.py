from transformers import ElectraTokenizer, ElectraForSequenceClassification
import torch
import pandas as pd
from datetime import date

# Load model and tokenizer
model_path = "TRAINING\MODELS"
tokenizer = ElectraTokenizer.from_pretrained(model_path)
model = ElectraForSequenceClassification.from_pretrained(model_path, num_labels=2)
model.eval()

def predict_suicidal(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        label = torch.argmax(probs).item()
        suicide_score = probs[0][1].item()
    return ("suicide" if label == 1 else "non-suicide"), suicide_score

def append_user_data(text, log_speech=False):
    label, score = predict_suicidal(text)
    today = str(date.today())
    new_row = pd.DataFrame([{
        "date": today,
        "text": text,
        "prediction": label,
        "score": round(score, 3)
    }])

    try:
        df = pd.read_csv("user_data.csv")
        df = pd.concat([df, new_row], ignore_index=True)
    except FileNotFoundError:
        df = new_row

    df.to_csv("user_data.csv", index=False)

    if log_speech:
        with open("user_speech_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{today}: {text}\n")

    return label, round(score, 3)
